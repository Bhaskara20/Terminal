import subprocess
import platform
import socket
import time
import os
import sys

file = open("art.txt", "r")
print (file.read())

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
while True:
	code = input(">>> ")
	if code == 'ping':
		host = input("Enter Website To Ping: ")
		number = input("Enter How Many Times To Ping: ")

		def ping(host):
			param = '-n' if platform.system().lower() == 'windows' else '-c'
			command = ['ping', param, number, host]
			return subprocess.call(command)
		print(ping(host))
	if code == 'local':
		print("Your Local IPS Is: " + host_ip)
		print("Your Desktop Name Is: " + host_name)
	if code == 'date':
		print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
	if code == 'list':
		dir_list = os.listdir(path)
		print("Files and Directories in '", path, "' :")
		print(dir_list)
	if code == 'list -a':
		file = input("Enter The Direct File Path To Read: ")
		dir_list2 = os.listdir(file)
		print("Files and directories in '", file, "':")
		print(dir_list2)
	if code == 'echo':
		echo = input("What Do You Want Me To Echo: ")
		print(echo)
	if code == 'help':
		file = open("help.txt", "r")
		print (file.read())
	if code == 'banner':
		file = open("art.txt", "r")
		print (file.read())
	if code =='kill me':
		sys.exit()