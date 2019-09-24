import socket
from threading import Thread
import time

HOST ='192.168.10.4'
PORT = 9009

def rcvMsg(sock):
   while True:
      try:
         data = sock.recv(1024)
         if not data:
            break

         print(str(data))
         hlist=[data[i:i+1] for i in range(0,len(data),1)]

         print(hlist)
         #print(data.decode())

      except:
         pass

def runChat():
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.connect((HOST, PORT))
      t = Thread(target=rcvMsg, args=(sock,))
      t.daemon = True
      t.start()

      while True:
         msg = b'0301060879128753'
         if msg =='/quit':
            sock.send(msg.encode())
            break
         sock.send(msg)
         time.sleep(1)
         #sock.send(msg.encode())

runChat()
