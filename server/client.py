import socket, threading


HOST = 'localhost'
PORT = 8888


class Client:
    def __init__(self):
        self.sock = socket.socket()
        self.sock.connect((HOST, PORT))
        
    def connection(self):        
        print('Connected successfully')
        while True: 
            self.strr = input('You: ', )
            self.history = set()
            
            if self.strr == '':
                self.strr = input()
                self.history.update(self.strr)
                self.sock.send(bytes(self.strr, encoding = 'utf-8')) 
            else:
                self.sock.send(bytes(self.strr, encoding = 'utf-8')) 
                
            for elem in self.history:
                if self.data.decode('utf-8') == elem:
                    pass
                else:
                    print(self.data.decode('utf-8'))
                    
            self.data = self.sock.recv(1024)
            print('Server' + ': ' + self.data.decode('utf-8'))


if __name__ == '__main__':
    Client().connection()