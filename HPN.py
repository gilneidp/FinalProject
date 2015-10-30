def GetPorts():
        motd = 'root:~$ Welcome to the SDN Manager'
        host = '10.0.0.2'
        port = 6633
        return (host, port, motd)

def writeLog(client, data=''):
        separator = '='*50
        fopen = open('./honey.mmh', 'a')
        fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), 
                    client[0], client[1], data, separator))
        fopen.close()

def main(host, port, motd):
            print 'Starting honeypot!'
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(10000)

            while True:
                 (insock, address) = s.accept()
                 print 'Connection from: %s:%d' % (address[0], address[1])
                 try:
                         insock.send('%s\n'%(motd))
                         data = insock.recv(1024)
                         insock.close()
                 except socket.error, e:
                         writeLog(address)
                 else:
                         writeLog(address, data)
