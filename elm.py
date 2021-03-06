# elm.py
import socket
import random
# get hostname
host = socket.gethostname()
# get ip from hostname
hostIP = socket.gethostbyname(host)
# args for commands
arg1 = '1'
arg2 = '1'
# startup text
print(host,'@',hostIP, '\n','WELCOME TO ELM A LIGHTWEIGHT CONSOLE')
print('Type "help" (without quatation) for a list of commands')
# help func
def elmHelp():
    print('Elm is a multipurpose CLI that takes the best of bash and cmd.')
    print('Commands:')
    print('exit - exits elm')
    print('cls - clears the screen')
    print('ip - gets local ip')
    print('hostname - get local hostname')
    print('rand - generates a random number')
# clear output func
def cls():
    print('\n' * 12)
# getip func
def getIp():
    print(hostIP)
# gethostname func
def getHostname():
    print(host)
# rand func
def Rand(minimum, maximum):
    minimum = input('min: ')
    maximum = input('max: ')
    print(random.randint(int(minimum), int(maximum)))
def helpCommand():
        # check if the command is help
    if command == 'help':
        cls()
        elmHelp()
def exitCommand():
    # check if the command is exit and if it is exit elm
    if command == 'exit':
        exit()
def clsCommand():
    # check if command is cls
    if command == 'cls':
        cls()
def getIpCommand():
    # check if command is ip
    if command == 'ip':
        getIp()
def getHostnameCommand():
    # check if command is hostname
    if command == 'hostname':
        getHostname()
def randCommand():
    # check if command is rand
    if command == 'rand':
        Rand(arg1, arg2)
while True:
    command = input()
    helpCommand()
    exitCommand()
    clsCommand()
    getIpCommand()
    getHostnameCommand()
    randCommand()
