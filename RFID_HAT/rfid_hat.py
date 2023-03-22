#!/usr/bin/env python
import mraa
import time
# Initialise UART
u = mraa.Uart(0)

# Set UART parameters
u.setBaudRate(9600)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)

# Start a neverending loop waiting for data to arrive.
# Press Ctrl+C to get out of it.
while True:
    if u.dataAvailable():
        # We are doing 1-byte reads here
        data_byte = u.readStr(12)
        print("Dtata = ",data_byte)
        time.sleep(0.5)
        

