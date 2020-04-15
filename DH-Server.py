import socket
import ShiftCipher

def server_program(q, alpha, Xa):
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    conn.send(str(q).encode())
    conn.send(str(alpha).encode())
    Ya = (alpha ** Xa) % q

    conn.send(str(Ya).encode())
    Yb = int(conn.recv(4096).decode())
    Ka = (Yb ** Xa) % q
    print(f'Ka->{Ka}')
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(4096).decode()
        data = ShiftCipher.shift_decrypt(data, Ka)
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        data = ShiftCipher.shift(data, Ka)
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    from sympy import isprime

    q = int(input('Enter the value of q: '))
    alpha = int(input('Enter the value of alpha: '))

    if not isprime(q):
        # print(f'{q} is prime No.')
        # print()
    # else:
        print(f'{q} is not a prime no.\n terminating the execution')
        exit(0)
    
    if not alpha < q:
        # print(f'{alpha} < {q}')
        # print()
    # else:
        print(f'{alpha} >= {q}')
        exit(0)
    
    alphanmodq = 0
    zeroltnltq = 0
    for n in range(1, q):
        zeroltnltq += n
        alphanmodq += (alpha ** n) % q
        # print(f'{n} | {alpha ** n} | {alphanmodq}')

    if not alphanmodq == zeroltnltq: 
        # print('No repetions')
        # print()
    # else: 
        print('There are repetitions, hence stopping')
        exit(0)
    
    Xa = int(input(f'Enter the value of Xa less than {q}: '))
    if not Xa < q:
        # print(f'{Xa} < {q}')
        # print()
    # else:
        print(f'{Xa} >= {q}')
        exit(0)

    server_program(q, alpha, Xa)
