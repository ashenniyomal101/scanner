#!/usr/bin/python3
import socket
import sys
from time import sleep
import threading

def scanner(ports):
    for i in ports:
        s = socket.socket()
        socket.setdefaulttimeout(1)
        try:
            s.connect_ex((ipaddr, i))
            for p in protocols:
                print('''
    {}
    Port   : {}
    status : OPEN
    Service : {}'''.format(p,i,socket.getservbyport(i, p)))
                sleep(5)
                
        except:
            pass

def thred(x, y):
    thread1 = threading.Thread(target=scanner, args=(x,))
    thread1.start()
    thread2 = threading.Thread(target=scanner, args=(y,))
    thread2.start()

    
def check(ports):
    newports = []
    evenNewPorts = []
    for each in range(ports):
        if each % 2 == 1:
            newports.append(each)
        elif each % 2 == 0:
            evenNewPorts.append(each)
        else:
            print("bla")  
    print()       
    print()
    print()
    thred(newports, evenNewPorts)

if __name__ == "__main__":
    try:
        script, scanmode, ipaddr = sys.argv
    except Exception as e:
        print(e)
        
    if len(sys.argv) == 3:
        try:
            print('Hostname resolved :', socket.gethostbyaddr(ipaddr))
        except:
            print("Host not found")
                  
        print('+'* 50) 
            
        if sys.argv[1] == str('full_scan'):
            print("Scanning all ports... this might take some time..")
            ports = 65535
        elif sys.argv[1] == str('basic_scan'):
            ports = int(input("Enter the port range :"))
            print("Scanning %s ports" % ports)
        else:
            print("Enter valid scanning mode.")
        print('+'* 50)

    else:
        print("Invalid syntax ; syntax : scanner.py <full_scan / basic_scan> <ip>")
        sys.exit()
            
    protocols =['tcp', 'udp']
    #mainThread = threading.Thread(target=check)
    #mainThread.start()
    check(ports)