import socket
import json

def Send(jsn , path, port): 
	if( type(jsn)!= json): return 0
	sock = socket.socket()
	sock.bind((path,port))
	sock.send(jsn)
	data = sock.recv(1024)
	sock.close()
	return data