from socket import *

serverPort = 8080
#serverPort2 = 13000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
#serverSocket2 = socket(AF_INET,SOCK_STREAM)
#serverSocket2.bind(('',serverPort2))
#serverSocket2.listen(1)

print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	request = connectionSocket.recv(1024)
	print request
#	http_response = """\
#HTTP/1.1 200 OK
#
#Hello, World!
#"""
	mots=request.split(" ")
	page=mots[1]
	page = page[1:]
	print page
	f = open(page,"r+t")
	connectionSocket.sendall(f.read())
	#capitalizedSentence = sentence.upper()
	#connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
	#connectionSocket, addr = serverSocket2.accept()
	#connectionSocket.send(capitalizedSentence )
	#connectionSocket.send("\n" )
	#connectionSocket.close()
	
	
	#print sentence
	print addr