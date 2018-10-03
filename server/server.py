import socket, threading, os


HOST = ''
PORT = 8888
LISTENERS = 100
MEMORY = 1024
ADDR = False
CONN = False


class Server(threading.Thread): 
    def __init__(self, addr, conn):
        self.sock = socket.socket()
        self.addr = addr
        self.conn = conn
        threading.Thread.__init__(self)
        self.visitors = set()
        self.clients = []
        self.file = open('COMMANDS.txt')
        
        
        self.sock.bind(('', PORT))
        self.sock.listen(LISTENERS)  
        
    def treat(self): 
        self.conn, self.addr = self.sock.accept()
        print('Connected from', self.addr)
        
        self.commands = self.file.read()
        self.visitors.update((self.conn, self.addr))
        self.clients.append([self.conn, self.addr])
        
        for client in self.clients:
            identificate = self.clients.index(client) 
            self.treating = True
            try:
                while self.treating:
                    self.data = self.clients[identificate][0].recv(MEMORY)
                    if not self.data:
                        pass
                    
                    print('Recieved from'  + str(self.clients[identificate][1]) + ':', end = ' ')
                    print(self.data.decode('utf-8'))
                    
                    self.message = input('Server: ', )
                    if self.message == self.commands[: 10]:
                        self.data = b''
                        self.conn.sendto(b'DATA HAS CLEARED', self.clients[identificate][1])
                        
                    elif self.message == self.commands[11:23]:
                        os._exit(0)
                        
                    else:
                        self.data = bytes(self.message, encoding = 'utf-8')
                        self.clients[identificate][0].sendto(self.data, self.clients[identificate][1])       

            except BaseException:  
                print('Connection has lost' + ':' + str(self.clients[identificate][1]))       
                del self.clients[self.clients.index(client)]
                
        return False


def fix_it():
    try:
        for i in range(LISTENERS):
            thread = Server(ADDR, CONN).treat()
            thread.setDaemon(True)
            thread.start()    
    except AttributeError:
        print('Waiting for new connection...')
    return fix_it()

if __name__ == '__main__':
    fix_it()