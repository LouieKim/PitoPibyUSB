from socket import *
import serial
import sys
import time

RECEIVE = "R"
SEND = "S"

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.10.4', 8080))
print('Success Connecting Server')

f = open("test_txt.txt", 'a')
recive_ser = serial.Serial('/dev/ttyUSB0', 9600)
send_ser = serial.Serial('/dev/ttyUSB1', 9600)

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
    print("Recive_ser: %s \n" % recive_ser.name)
    print("Send_ser: %s \n" % send_ser.name)

    while(1):

        data = recive_ser.read(1)
        print("compete read")

        record_data(str(data, "utf-8"))
        print("compete record Data")

        send_ser.write(data)
        print("SEND DATA To USB")

        clientSock.send('I am a client'.encode('utf-8'))
        print('Send message to Server')
        data = clientSock.recv(1024)
        print('Receive Data from Server : ', data.decode('utf-8'))

        #time.sleep(1)

if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        f.close()
        recive_ser.close()
        send_ser.close()
        print("Exit")
        exit()
