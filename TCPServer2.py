from socket import *

serverPort = 12000
serverPort2 = 13000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.bind(('',serverPort2))
serverSocket2.listen(1)

print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	#connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
	connectionSocket, addr = serverSocket2.accept()
	connectionSocket.send(capitalizedSentence )
	connectionSocket.send("\n" )
	connectionSocket.close()
	
	
	print sentence
	print addr