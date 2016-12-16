import serial

ser = serial.Serial()
ser.baudrate = 9600
# ser.port = '/dev/tty.usbmodem1411'    # For MacBook
ser.port = 'COM4'


# signal_strength = [0] * 110
# signal_strength.append(1)
# counter = 0


def read_serial():
    ser.open()
    value = float(ser.readline().strip())
    ser.close()
#    global counter
#    value = signal_strength[counter]
#    counter = 0 if counter == len(signal_strength) - 1 else counter + 1
    return value
