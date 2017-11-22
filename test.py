
from time import sleep
#from ctypes import *
#from string import *

from PCAN_Basic.Include.PCANBasic import *

m_CHANNELS = {
                'PCAN_USBBUS1':PCAN_USBBUS1,
                'PCAN_USBBUS2':PCAN_USBBUS2,
                'PCAN_USBBUS3':PCAN_USBBUS3,
                'PCAN_USBBUS4':PCAN_USBBUS4,
                'PCAN_USBBUS5':PCAN_USBBUS5,
                'PCAN_USBBUS6':PCAN_USBBUS6,
                'PCAN_USBBUS7':PCAN_USBBUS7,
                'PCAN_USBBUS8':PCAN_USBBUS8,
                'PCAN_USBBUS9':PCAN_USBBUS9,
                'PCAN_USBBUS10':PCAN_USBBUS10,
                'PCAN_USBBUS11':PCAN_USBBUS11,
                'PCAN_USBBUS12':PCAN_USBBUS12,
                'PCAN_USBBUS13':PCAN_USBBUS13,
                'PCAN_USBBUS14':PCAN_USBBUS14,
                'PCAN_USBBUS15':PCAN_USBBUS15,
                'PCAN_USBBUS16':PCAN_USBBUS16
            }

print("Welcome!")
                           
m_objPCANBasic = PCANBasic()

print("Scanning for adapters...")

# Find available USB adapters
items = []
for name in m_CHANNELS.keys():
    value = m_CHANNELS[name]
    # Checks for a Plug&Play Handle and, according with the return value, includes it
    # into the list of available hardware channels.
    #
    result = m_objPCANBasic.GetValue(value, PCAN_CHANNEL_CONDITION)
    if  (result[0] == PCAN_ERROR_OK) and (result[1] & PCAN_CHANNEL_AVAILABLE):
        print("Channel available: ", name)
        result = m_objPCANBasic.GetValue(value, PCAN_CHANNEL_FEATURES)
        items.append(name)

print("Opening first PCAN-USB...")

m_PcanHandle = PCAN_USBBUS1
baudrate = PCAN_BAUD_1M
hwtype = PCAN_TYPE_ISA_SJA
# hwtype = PCAN_TYPE_ISA
ioport = 0x02a0
interrupt = 11

result = m_objPCANBasic.Initialize(m_PcanHandle, baudrate, hwtype, ioport, interrupt)


# # Processes a received message, in order to show it in the Message-ListView
# #
def ProcessMessage(*args):
    # Split the arguments. [0] TPCANMsg, [1] TPCANTimestamp
    #
    theMsg = args[0][0]
    itsTimeStamp = args[0][1]

    newMsg = TPCANMsg()
    newMsg.ID = theMsg.ID
    print("Received CAN frame from ID ", hex(newMsg.ID))
    newMsg.DLC = theMsg.LEN
    for i in range(8 if (theMsg.LEN > 8) else theMsg.LEN):
        newMsg.DATA[i] = theMsg.DATA[i]
    newMsg.MSGTYPE = theMsg.MSGTYPE
    newTimestamp = TPCANTimestamp()
    newTimestamp.value = (itsTimeStamp.micros + 1000 * itsTimeStamp.millis + 0x100000000 * 1000 * itsTimeStamp.millis_overflow)

for i in range(10):
#while True:
    # We execute the "Read" function of the PCANBasic
    #
    result = m_objPCANBasic.Read(m_PcanHandle)

    if result[0] == PCAN_ERROR_OK:
        # We show the received message
        #
        ProcessMessage(result[1:])
    else:
        sleep(1)
