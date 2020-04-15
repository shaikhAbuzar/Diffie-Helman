import socket
import ShiftCipher

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    q = int(client_socket.recv(4096).decode())
    alpha = int(client_socket.recv(4096).decode())
    Xb = int(input(f'Enter the value of Xb less than {q}: '))
    if not Xb < q:
        # print(f'{Xb} < {q}')
        # print()
    # else:
        print(f'{Xb} >= {q}')

    Yb = (alpha ** Xb) % q
    Ya = int(client_socket.recv(4096).decode())
    client_socket.send(str(Yb).encode())
    Kb = (Ya ** Xb) % q
    print(f'Kb->{Kb}')
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        message = ShiftCipher.shift(message, Kb)
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(4096).decode()  # receive response
        data = ShiftCipher.shift_decrypt(data, Kb)

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
