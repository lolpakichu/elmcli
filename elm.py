import socket

host = socket.gethostname()
hostIP = socket.gethostbyname(host)

print(hostIP, host, '\n','WELCOME TO ELM A LIGHTWEIGHT CONSOLE')

print('Type "help" (without quatation) for a list of commands')
#help func
def elmHelp():
    print('exit- exits elm')
    print('cls- clears the screen')
    print('ip- gets local ip')
    print('hostname- get local hostname')
#clear output func
def cls():
    print('\n' * 10)
#getip func
def getIp():
    print(hostIP)
#gethostname func
def getHostname():
    print(host)
while True:
    command = input()
    #check if the command is help
    if command == 'help':
        cls()
        elmHelp()
    #check if the command is exit and if it is exit elm
    if command == 'exit':
        exit()
    #check if command is cls
    if command == 'cls':
        cls()
    if command == 'ip':
        getIp()
    if command == 'hostname':
        getHostname()

