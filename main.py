import serial
import curses
import sys

def write_data(data):
    f = open("test_txt.txt", 'a')
    f.write(data)
    print("Input Data: %s" % data)

    f.close()

def main(argv):

    FILE_NAME = argv[0]
    OPTION = argv[1]

    print("Start %s \n" % OPTION)
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    while(1):
        data = ser.read(1)
        print(data)
        print("compete read")
        write_data(str(data, "utf-8"))
        print("write Data")
    ser.close()

if __name__ == "__main__":
    main(sys.argv)
