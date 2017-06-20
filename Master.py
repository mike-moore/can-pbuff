import can, logging, sys, time, threading
import sample_packet_pb2
from CmdDefinitions import *

class Master(object):

    def __init__(self, channel="vcan0", bustype="socketcan_ctypes", frequencyHz=10):
        self.Bus = can.interface.Bus(channel=channel, bustype=bustype)
        self.CommFrequencyHz = frequencyHz
        self.BusReader = can.BufferedReader()
        self.MsgNotifier = can.Notifier(self.Bus, [self.BusReader])
        self.listenThread = threading.Thread(target=self.listen)
        self.listenThread.daemon = True
        self.runListenThread = True

    def run(self):
        self.runListenThread = True
        self.listenThread.start()

    def listen(self):
        while self.runListenThread:
            recvd_cmds = self.readAllMessages()
            time.sleep(1.0/self.CommFrequencyHz)
            if recvd_cmds:
                logging.info("Commands received : " + str(recvd_cmds))
                self.sendResponse()

    def readAllMessages(self):
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
                cmds = self.unpackCmds(str(bytes_rcvd))
                return cmds
            else:
              raise IOError
        return None

    def readRawBytes(self):
         return self.BusReader.get_message(1.0/self.CommFrequencyHz).data

    def unpackCmds(self, raw_bytes):
         cmds = sample_packet_pb2.CommandPacket()
         logging.debug("Cmds to be unpacked :")
         logging.debug(":".join("{:02x}".format(ord(c)) for c in raw_bytes))
         try:
             cmds.ParseFromString(raw_bytes)
         except Exception:
             raise IOError
         return cmds

    def sendResponse(self):
         response = sample_packet_pb2.TelemetryPacket()
         response.MeasuredHeading = 5.0
         response.MeasuredDistance = 10.0
         status = response.RoverStatus.add()
         status.Id = CMD_ACCEPT
         self.tx(response)

    def packTlmAsMsgList(self, tlm):
        """
        Uses a list comprehension to split up the protobuf serialized telemetry
        into payloads of length 8 bytes (CAN max size)
        """
        raw_tlm = tlm.SerializeToString()
        can_max_data = 8 # 8 bytes max per message
        return [raw_tlm[index:index + can_max_data] for index in range(0, len(raw_tlm), can_max_data)]

    def tx(self, tlm):
        if (isinstance(tlm, sample_packet_pb2.TelemetryPacket)):
            # Send the serialized tlm to the CAN bus
            try:
                can_msgs = self.packTlmAsMsgList(tlm)
                for can_msg in can_msgs:
                    msg = can.Message(data=can_msg)
                    self.Bus.send(msg)
            except EncodeError:
                logging.error("Failed to encode telemetry packet. Are all required fields set?")
                raise IOError


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(levelname)s:%(message)s')
    master = Master(frequencyHz=10.0)
    master.run()
    time.sleep(10.0)
