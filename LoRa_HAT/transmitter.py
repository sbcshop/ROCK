#!/usr/bin/env python
import mraa
import time
# Initialise lora
lora = mraa.Uart(0)
import sys
# Set lora parameters
lora.setBaudRate(9600)
lora.setMode(8, mraa.UART_PARITY_NONE, 1)
lora.setFlowcontrol(False, False)

# Start a neverending loop waiting for data to arrive.
# Press Ctrl+C to get out of it.

msg_b = bytearray("Hello,from Rock\n", "ascii")

while True:
        print("Sending message as a byte array: '{0}'".format(msg_b))
        lora.write(msg_b)
        time.sleep(1)
        
        

