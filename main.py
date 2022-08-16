import serial
from time import sleep

def main():

    # Edit port for your environment
    port = '/dev/tty.usbserial-0001'
    ser = serial.Serial(port, 9600, timeout=None)

    while True:
        line = ser.read_all()
        if line != b'':
            print(line)
        sleep(0.01) # second

    ser.close()

if __name__ == '__main__':
    main()
