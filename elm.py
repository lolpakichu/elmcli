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
    print('exit- exits elm')
    print('cls- clears the screen')
    print('ip- gets local ip')
    print('hostname- get local hostname')
    print('rand- generates a random number')
# clear output func
def cls():
    print('\n' * 8)
# getip func
def getIp():
    print(hostIP)
# gethostname func
def getHostname():
    print(host)
# rand func
def Rand(minimum, maximum):
    minimum = input('Input the minimum ')
    maximum = input('Input the maximum ')
    print(random.randint(int(minimum), int(maximum)))
while True:
    command = input()
    # check if the command is help
    if command == 'help':
        elmHelp()
        cls()
    # check if the command is exit and if it is exit elm
    if command == 'exit':
        exit()
    # check if command is cls
    if command == 'cls':
        cls()
    # check if command is ip
    if command == 'ip':
        getIp()
    # check if command is hostname
    if command == 'hostname':
        getHostname()
    # check if command is rand
    if command == 'rand':
        Rand(arg1, arg2)