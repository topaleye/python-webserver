# import socket module
import socket
from socket import *
# In order to terminate the program
import sys

SERVER = gethostbyname(gethostname())

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(('', port))

    # Fill in start
    serverSocket.listen()
    print(f"[LISTENING ON] {gethostbyname(gethostname())}\r\n")

    # Fill in end

    while True:
        # Establish the connection

        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Fill in start -are you accepting connections?     #Fill in end

        try:
            # receive message from client
            message = connectionSocket.recv(1024)  # Fill in start -a client is sending you a message   #Fill in end
            print(f"[MESSAGE] {message}")
            # taking the 2nd part of the HTTP header
            filename = message.split()[1]

            # opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], 'r')  # fill in start #fill in end)
            # store the contents of the file
            # fill in end
            print(f"[REQUESTED FILE NAME] {filename[1:]}")

            outputdata = f.read().encode()
            # outputdata += b"Content-Type: text/html; charset=UTF-8\r\n"\
            # Fill in start -This variable can store your headers you want to send for any valid or invalid request.
            # Content-Type above is an example on how to send a header as bytes
            # send the filename and filesize
            # connectionSocket.send(f"{filename}{SEPARATOR}{filesize}".encode())
            # Fill in end

            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            # Fill in start
            # connectionSocket.send(b"HTTP 1.1 200 OK \r\n\r\n")
            response = b'HTTP/1.0 200 OK\n\n' + outputdata
            connectionSocket.sendall(response)
            # Fill in end

            # Send the content of the requested file to the client
            # for i in f: #for line in file
            # for i in f:
            #   connectionSocket.send(outputdata)
            # connectionSocket.send(b"\r\n")
            # Fill in start - send your html file contents #Fill in end
            f.close()
            connectionSocket.close()  # closing the connection socket

        except IOError:
            # Send response message for invalid request due to the file not being found (404)
            # Fill in start
            connectionSocket.send(b"HTTP 1.1 400 Not Found\r\n\r\n")
            connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
            connectionSocket.close()  # closing the connection socket
            # Fill in end

            # Close client socket
            # Fill in start

            # Fill in end

    serverSocket.close()
    print(f"[CLOSED SOCKET]\r\n")
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
