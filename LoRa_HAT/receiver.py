#!/usr/bin/env python
import mraa
import time
# Initialise UART
lora = mraa.Uart(0)

# Set UART parameters
lora.setBaudRate(9600)
lora.setMode(8, mraa.UART_PARITY_NONE, 1)
lora.setFlowcontrol(False, False)

# Start a neverending loop waiting for data to arrive.
# Press Ctrl+C to get out of it.
while True:
    if lora.dataAvailable():
        # We are doing 10-byte reads here
        data_byte = lora.readStr(10)
        print("Data = ",data_byte)
        time.sleep(1)
        

