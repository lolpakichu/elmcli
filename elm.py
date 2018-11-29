import socket

host = socket.gethostname()
hostIP = socket.gethostbyname(host)

print(hostIP, host, '\n','WELCOME TO ELM A LIGHTWEIGHT CLI')

print('Type "help" (without quatation) for a list of commands')
#help func
def elmHelp():
    print('exit- exits elm cli')
#clear output func
def cls():
    print('\n' * 50)
while True:
    command = input()
    #check if the command is help
    if command == 'help':
        cls()
        elmHelp()
    #check if the command is exit and if it is exit the CLI
    if command == 'exit':
        exit()

