#!/usr/bin/python

# Implements a unit-test for the Protobuf 
# CAN Master/Slave
import unittest, logging, sys, SocketServer, time, threading
sys.path.append("../")
from Master import Master
from Slave import Slave
import sample_packet_pb2
from CmdDefinitions import *

class CommCheckout(unittest.TestCase):

    def setUp(self):
        self.testArticle = Slave(frequencyHz=TEST_COMM_FREQ_HZ)
        self.SuccessTransmissionCount = 0
        self.FailTransmissionCount = 0
        self.NumTestsToRun = 10
    
    def test_sendCommands(self):
    	for testNum in range(1, self.NumTestsToRun+1):
            logging.info("\r\n")
            logging.info("#############################################")
            logging.info("## TEST NUMBER " + str(testNum))
            logging.info("#############################################")
            logging.info("\r\n")
            cmd_packet = sample_packet_pb2.CommandPacket()
            control_signal_cmd = cmd_packet.RoverCmds.add()
            control_signal_cmd.Id = DO_STUFF
            control_signal_cmd.Value = 0.1 * testNum
            # Use the helper function to send the command packet and
            # check that we got a response
            response = self.helper_SendOneCmdPacket(cmd_packet)
            time.sleep(20.0/TEST_COMM_FREQ_HZ)
            self.helper_checkResponse(response)

        if self.SuccessTransmissionCount != self.NumTestsToRun:
            print self.SuccessTransmissionCount
            print self.NumTestsToRun
            self.assertTrue(False)

    def helper_SendOneCmdPacket(self, cmd_packet):
        try:
            response = self.testArticle.sendCmd(cmd_packet)
            return response
        except IOError:
            # Fail the test. No response
            self.assertTrue(False)
            return None

    def helper_checkResponse(self, response):
        if response:
            self.SuccessTransmissionCount += 1
            logging.info("Success Packet # : " + str(self.SuccessTransmissionCount))
        else:
            self.FailTransmissionCount += 1
            logging.info("Failed Packet # : " + str(self.FailTransmissionCount))

TEST_COMM_FREQ_HZ = 100
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(levelname)s:%(message)s')
    # Instantiate a test Master device. Used for doing Slave to Master and Master to Slave 
    # virtual CAN comm testing
    testMaster = Master(channel="vcan0", bustype="socketcan_ctypes", frequencyHz=TEST_COMM_FREQ_HZ)
    testMaster.run()
    # Give the test master device time to startup before running the tests.
    time.sleep(1.0)
    # Run the unit-tests
    suite = unittest.TestLoader().loadTestsFromTestCase(CommCheckout)
    unittest.TextTestRunner(verbosity=2).run(suite)