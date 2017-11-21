
from time import sleep
from ctypes import *
from string import *
from PCANBasic import *


print("Initializing adapter...")

m_objPCANBasic = PCANBasic()
m_PcanHandle = PCAN_USBBUS1
baudrate = PCAN_BAUD_1M
#hwtype = PCAN_TYPE_ISA_SJA
hwtype = PCAN_TYPE_ISA
ioport = 0x02a0
interrupt = 11

#result =  m_objPCANBasic.Initialize(m_PcanHandle,baudrate,hwtype,ioport,interrupt)


## Processes a received message, in order to show it in the Message-ListView
##
def ProcessMessage(*args):        
    # Split the arguments. [0] TPCANMsg, [1] TPCANTimestamp
    #
    theMsg = args[0][0]
    itsTimeStamp = args[0][1]    

    newMsg = TPCANMsg()
    newMsg.ID = theMsg.ID
    print(newMsg.ID)
    newMsg.DLC = theMsg.LEN
    for i in range(8 if (theMsg.LEN > 8) else theMsg.LEN):
        newMsg.DATA[i] = theMsg.DATA[i]
    newMsg.MSGTYPE = theMsg.MSGTYPE
    newTimestamp = TPCANTimestamp()
    newTimestamp.value = (itsTimeStamp.micros + 1000 * itsTimeStamp.millis + 0x100000000 * 1000 * itsTimeStamp.millis_overflow)

while True:
    print("Read...")

    # We execute the "Read" function of the PCANBasic
    #
    result = m_objPCANBasic.Read(m_PcanHandle)

    if result[0] == PCAN_ERROR_OK:
        # We show the received message
        #
        ProcessMessage(result[1:])

    sleep(1)
