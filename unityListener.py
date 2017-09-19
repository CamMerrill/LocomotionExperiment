import socket 


def unityListen():
	UDP_RECV_UNITY_PORT = 25006
	UDP_IP = "130.126.181.238"

	recvSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	recvSock.bind((UDP_IP, UDP_RECV_UNITY_PORT))
	while True:
        	data, addr = recvSock.recvfrom(64) 
        	if len(data) > 0:
            		print data
            		recvSock.close()
            		break
