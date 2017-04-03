from socket import *
#serverName = 'localhost'
#serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("localhost",8080))
sentence = "GET / HTTP/1.1\n\n\n"
clientSocket.sendall(sentence)
print clientSocket.recv(1024)
#print 'From Server:', modifiedSentence
clientSocket.close()