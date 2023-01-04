import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    # Receive two numbers from the server
    num1 = int(sock.recv(16).decode())
    num2 = int(sock.recv(16).decode())

    # Send the summation of the two numbers back to the server
    sum = num1 + num2
    sock.sendall(str(sum).encode())

    # Receive the result from the server
    result = sock.recv(16).decode()
    print(result)
finally:
    # Clean up the connection
    sock.close()

