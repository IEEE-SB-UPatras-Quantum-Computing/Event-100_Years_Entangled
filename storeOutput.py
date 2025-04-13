import serial.tools.list_ports

FILE_NAME = "data.txt"

ports = serial.tools.list_ports.comports()
serialTnst = serial.Serial()

serialTnst.baudrate = 9600
serialTnst.port = 'COM3'
serialTnst.open()

with open(FILE_NAME, "w") as file:
    while True:
        if serialTnst.in_waiting:
            dataBits = serialTnst.readline()
            dataInt = int(dataBits.decode('utf').strip())
            file.write(str(dataInt))
