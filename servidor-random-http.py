#!/usr/bin/python3

import socket
import random	

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.bind(('localhost', 1237))
mysocket.listen(5)


try:
	while True:
		print('Waiting a request')
		(recvSocket, address) = mysocket.accept()
		print('HTTP request received:')
		print(recvSocket.recv(1024))
		next_url = random.randint(1,100000)
		recvSocket.send(bytes('HTTP/1.1 200 OK \r\n\r\n' +
                        '<html><title>URLs Aleatorias</title>' +
                        '<body>Hola.  ' +
                        '<a href="http://localhost:1237/' +
						 str(next_url) +
                        '">Dame otra</a>' +
                        '</body></html>'+
						'\r\n', 'utf-8'))
		recvSocket.close()
except KeyboardInterrupt:
    print('Closing binded socket')
    mysocket.close()
