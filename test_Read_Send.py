import serial
import sys
import time

RECEIVE = "R"
SEND = "S"

f = open("test_txt.txt", 'a')
ser = serial.Serial('/dev/ttyUSB0', 9600)

def write_data(data):
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

    if OPTION == RECEIVE:
        while(1):
            data = ser.read(1)
            print("compete read")
            #write_data(str(data, "utf-8"))
            print(str(data))
            print("write Data")

    elif OPTION == SEND:
        while(1):
            ser.write(b'acacacac')
            print("SEND DATA")
            time.sleep(1)

    else:
        print("wrong args")

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        f.close()
        ser.close()
        print("Exit")
        exit()
