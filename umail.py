import usocket as socket
import ubinascii

class SMTP:
    def __init__(self, host, port, user=None, password=None, ssl=False):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.ssl=ssl
        self.sock=None
        
    def login(self):
        self.sock =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        #aquie iria el handshake, para simplificar usaremos SMTP estandar
        self.sock.send(b'EHLO esp32\r\n')
        if self.user and self.password:
            self.sock.send(b'AUTH LOGIN\r\n')
            self.sock.send(ubinascii.b2a_base64(self.user.encode())+b'\r\n')
            self.sock.send(ubinascii.b2a_base64(self.password.encode())+b'\r\n')
            
    def send(self, to_email, subject, body):
        self.sock.send(b'MAIL FROM:<' + self.user.encode()+b'>\r\n')
        self.sock.send(b'RCPT TO:<'+ to_email.encode()+b'>\r\n')
        self.sock.send(b'DATA\r\n')
        self.sock.send(b'Subject: '+subject.encode()+b'>\r\n'+ body.encode() +b'>\r\n')
        self.sock.send(b'QUIT\r\n')
        
    def quit(self):
        self.sock.close()
