import serial
import curses

def write_data(data):
    f = open("test_txt.txt", 'a')
    f.write(data)
    print("Input Data: %s",%*data)

    f.close()

if __name__ == "__main__":
    print("Start\n")
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    while(1):
        data = ser.read(1)
        print(data)
        print("compete read")
        write_data(str(data, "utf-8"))
        print("write Data")

    ser.close()
