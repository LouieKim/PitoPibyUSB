import serial

if __name__ == "__main__":
    print("Start\n")
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    while(1):
        print(ser.readline())
        ser.write("A")
