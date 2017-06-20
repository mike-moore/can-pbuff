import can, logging, sys, time, binascii
import sample_packet_pb2
from CmdDefinitions import *
from google.protobuf.message import EncodeError

class Slave(object):
    def __init__(self, channel="vcan0", bustype="socketcan_ctypes", frequencyHz=10):
        self.Bus = can.interface.Bus(channel=channel, bustype=bustype)
        self.BusReader = can.BufferedReader()
        self.MsgNotifier = can.Notifier(self.Bus, [self.BusReader])
        self.CommFrequencyHz = frequencyHz

    def sendCmd(self, cmd):
        # Tx the command
        self.tx(cmd)
        # Give the device time to respond
        # TODO : define this magic 3.0. It's used to be sure
        #        the device has enough time to respond.
        time.sleep(3.0/self.CommFrequencyHz)
        # Rx the telemetry
        try:
            response = self.readTelemetry()
        except IOError:
        	logging.info("Failed to receive a response packet : " + str(cmd))
        if response:
            # Print out what we got back
            logging.info("Received response : " + str(response))
    	return response

    def packCmdsAsMsgList(self, cmd):
        """
        Uses a list comprehension to split up the protobuf serialized commands
        into payloads of length 8 bytes (CAN max size)
        """
        raw_cmds = cmd.SerializeToString()
        can_max_data = 8 # 8 bytes max per message
        return [raw_cmds[index:index + can_max_data] for index in range(0, len(raw_cmds), can_max_data)]

    def tx(self, cmd):
        if (isinstance(cmd, sample_packet_pb2.CommandPacket)):
            # Send the serialized cmds to the CAN bus
            try:
                can_msgs = self.packCmdsAsMsgList(cmd)
                for can_msg in can_msgs:
                    msg = can.Message(data=can_msg)
                    self.Bus.send(msg)
            except EncodeError:
                logging.error("Failed to encode command packet. Are all required fields set?")
                raise IOError

    def readTelemetry(self):
        num_msgs_to_read = self.BusReader.buffer.qsize()
        if num_msgs_to_read :
            msgs_read = 0
            bytes_rcvd = ''
            logging.debug("Num messages to read : " + str(num_msgs_to_read))
            while msgs_read < num_msgs_to_read:
                msgs_read +=1
                logging.debug("Reading message " + str(msgs_read) + " of " + str(num_msgs_to_read))
                bytes_rcvd += self.readRawBytes()
            if bytes_rcvd:
                tlm = self.unpackTelemetry(str(bytes_rcvd))
                return tlm
            else:
              raise IOError
        return None

    def readRawBytes(self):
         return self.BusReader.get_message(1.0/self.CommFrequencyHz).data

    def unpackTelemetry(self, raw_bytes):
        tlm = sample_packet_pb2.TelemetryPacket()
        logging.debug("Telemetry to be unpacked :")
        logging.debug(":".join("{:02x}".format(ord(c)) for c in raw_bytes))
        try:
            tlm.ParseFromString(raw_bytes)
        except Exception:
            raise IOError
        return tlm    	
