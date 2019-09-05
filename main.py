import serial

def write_data(data):
    f = open("test_txt.txt", 'a')
    f.write(data)
    f.close()

if __name__ == "__main__":
    print("Start\n")
    ser = serial.Serial('/dev/ttyUSB0', 9600)

    while(1):
        data = ser.read()
        print(data)
        print("compete read")
        write_data(str(data))
        print("write Data")

    ser.close()
