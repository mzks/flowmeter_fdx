import serial
from time import sleep

def main():

    out_filename = 'output.csv'

    # Edit port for your environment
    port = '/dev/tty.usbserial-0001'
    ser = serial.Serial(port, 9600, timeout=None)

    print('Waiting data...')
    while True:
        line = ser.read_all()
        if line != b'':
            with open(out_filename, 'a') as f:
                f.write(line.decode('utf-8'))

        sleep(0.01) # unit: second

    ser.close()

if __name__ == '__main__':
    main()
