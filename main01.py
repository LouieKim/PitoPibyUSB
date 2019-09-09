import serial
import sys
import time

RECEIVE = "R"
SEND = "S"

f = open("test_txt.txt", 'a')
ser = serial.Serial('/dev/ttyUSB0', 9600)

def record_data(data):
    try:
        f.write(data)
        print("Input Data: %s" % data)
    except Exception as e:
        print(e)
    finally:
        pass

def main(argv):
    FILE_NAME = argv[0]
    OPTION = argv[1]

    print("Start %s \n" % OPTION)
    print(ser.name)

    while(1):

        data = ser.read(1)
        print("compete read")

        record_data(str(data, "utf-8"))
        print("compete record Data")

        ser.write(bytes(data, 'UTF-8'))
        print("SEND DATA")

        time.sleep(1)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        f.close()
        ser.close()
        print("Exit")
        exit()
