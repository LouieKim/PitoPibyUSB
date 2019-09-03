import serial

if __name__ == "__main__":
    print("Start\n")
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    print(ser.read())
    print("compete read")
    ser.write("A")
    print("write Data")
    ser.close()
