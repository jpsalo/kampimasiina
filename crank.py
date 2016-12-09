import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/tty.usbmodem1411'  # NOTE: Change this to COM1


signal_strength = [0, 0, 0, 0, 1]
counter = 0


def read_serial():
    # ser.open()
    # value = float(ser.readline().strip())
    # ser.close()
    global counter
    value = signal_strength[counter]
    counter = 0 if counter == len(signal_strength) - 1 else counter + 1
    return value
