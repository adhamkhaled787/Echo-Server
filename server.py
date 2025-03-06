import socket 

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket_server.bind(('0.0.0.0',11111))

socket_server.listen(5)
print("Server is listening on port 11111...")



def process_message(message):
    if len(message) < 2:
        return message
    first, rest = message[0], message[1:]
    
    if first == 'A':
        return ''.join(sorted(rest,reverse = True))
    elif first == 'C':
        return ''.join(sorted(rest))
    elif first == 'D':
        return rest.upper()
    else:
        return message
    

if __name__ == '__main__':
    while True:
         client_socket, client_address = socket_server.accept()
         print(f"Connection established with {client_address}")

         while True:
            data = client_socket.recv(1024).decode().strip() 
            if not data:
                break  
            
            print(f"Received: {data}")
            response = process_message(data)  
            client_socket.sendall(response.encode())  

         client_socket.close()
         print(f"Connection closed with {client_address}")