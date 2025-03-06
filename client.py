import socket

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_client.connect(('127.0.0.1',11111))

print(f"Connected to server at {'0.0.0.0'}:{11111}")

if __name__ == '__main__':

    while True:
        message = input("Enter a message:  type 'exit' to close connection\n")
        if message == 'exit':
            break
        socket_client.sendall(message.encode())
        response = socket_client.recv(1024).decode().strip()
        print(f"Response: {response}")
    socket_client.close()
    print("Connection closed")

