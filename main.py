import serial

if __name__ == "__main__":
    print("Start\n")
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    data = ser.read()
    print(data)
    print("compete read")
    ser.write(data)
    print("write Data")
    ser.close()
