import serial.tools.list_ports
port = serial.tools.list_ports.comports();
serialIns = serial.Serial()

portList = []

for oneport in port:
    portList.append(str(oneport))
    print(portList)

data = input("select port: /dev/cu.usbserial-")
url = '/dev/cu.usbserial-' +str(data)

for x in range(0, len(portList)):
    if portList[x].startswith(url):
        print(portList[x])

serialIns.baudrate = 9600
serialIns.port = url
serialIns.open()

while True:
    if serialIns.in_waiting:
        datas = serialIns.readline()
        print(datas.decode("utf-8").rstrip("\n"))
