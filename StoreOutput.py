import serial.tools.list_ports
import sys

ports =serial.tools.list_ports.comports()
serialTnst=serial.Serial()

portlist=[]

for onePort in ports:
    portlist.append(str(onePort))
    print(str(onePort))
    print(portlist)


importVal= input("Select port: COM")

for x in range (0,len(portlist)):
    if portlist[x].startswith("COM" +str(importVal)):
        portVal= "COM" + importVal
        print("Your slected port is:", portlist[x])
serialTnst.baudrate=9600
serialTnst.port= portVal
serialTnst.open()

# Άνοιγμα αρχείου για αποθήκευση δεδομένων
with open("data.txt", "w") as file:
    while True:
        if serialTnst.in_waiting:
            dataBits = serialTnst.readline()
            dataInt = int(dataBits.decode('utf').strip())
            print(dataInt)  
            file.write(str(dataInt) + "\n")  
    