import socket

ip = 'google.com'

portas = (11, 10, 21, 22, 25, 3022, 80, 8080, 8090, 9843, 443, 8043, 9443, 110, 985, 9090, 9000)

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(2)
    conexao = cliente.connect_ex((ip, porta))

    if conexao == 0:
        print("Porta: " + str(porta) + "" + "<- aberta")
    else:
        print("Porta: " + str(porta) + " " + "<- fechada")
