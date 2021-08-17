#!/bin/python3
import pyfiglet
import sys
import socket
from datetime import datetime as dt
print(pyfiglet.figlet_format("NetPortScanner"))
baner = pyfiglet.figlet_format("by li0day")
print(baner)
print("Autor = li0day")
print("E-mail = li0day@tutanota.com")
print("Instagram = https://www.instagram.com/li0day/")
print("Wersja = 1.1")

def nl():
 print('\n') 

  
if len(sys.argv) == 2: 
 target = socket.gethostbyname(sys.argv[1]) 
else:  
 nl()  
 print("Niepoprawnie zdefiniowany parametr wejścia:(")  
 print("Syntax --> python3 portscanner.py <IP Address>")
 nl()


nl() 
print("~" * 50) 
print("Skanowany host ~> {}".format(target)) 
print("Czas startu: {}".format(dt.now())) 
print("~" * 50) 
nl()

try:
 for port in range (1,999):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  socket.setdefaulttimeout(1) 
  result = s.connect_ex((target, port))
 
  if result == 0:
   print("<~ Port {} jest otwarty i niefiltrowany ~>".format(port))
  s.close

except KeyboardInterrupt:   
 print("<~ Przerwany Skan ~>")  
 sys.exit()  
except socket.gaierror: 
 print("<~ !Nazwa hosta niepoprawna! ~>")  
 sys.exit()   
except socket.gaierror:   
 print("<~ !Błąd połączenia! ~>")  
 sys.exit()
