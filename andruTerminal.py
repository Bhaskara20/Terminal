from shutil import move
from pyfiglet import Figlet
import subprocess
import platform
import socket
import time
import os
import sys
import wmi
import wget
import youtube_dl
import colorama
from colorama import Fore
from colorama import Style
import datetime
import pafy
import shutil

e = datetime.datetime.now()
computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]
os_name = os_info.Name.encode('utf-8').split(b'|')[0]
os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576

download= {}
def downloader_funct():
    with youtube_dl.YoutubeDL(download) as dwnld:
        dwnld.download([dld])


#file = open("art.txt", "r")
#print (file.read())

print("""\
  __.......__
            .-:::::::::::::-.
          .:::''':::::::''':::.
        .:::'     `:::'     `:::. 
   .'\  ::'   ^^^  `:'  ^^^   '::  /`.
  :   \ ::   _.__       __._   :: /   ;                                 
 :     \`: .' ___\     /___ `. :'/     ; 
:       /\   (_|_)\   /(_|_)   /\       ;
:      / .\   __.' ) ( `.__   /. \      ;  
:      \ (        {   }        ) /      ;   
 :      `-(     .  ^"^  .     )-'      ;
  `.       \  .'<`-._.-'>'.  /       .'
    `.      \    \;`.';/    /      .'
 jgs  `._    `-._       _.-'    _.'
       .'`-.__ .'`-._.-'`. __.-'`.
     .'       `.         .'       `.
   .'           `-.   .-'           `. 
    """)
print("""\
 ___   _   _____________ _   _   _____ ______________  ________ _   _   ___   _     
 / _ \ | \ | |  _  \ ___ \ | | | |_   _|  ___| ___ \  \/  |_   _| \ | | / _ \ | |    
/ /_\ \|  \| | | | | |_/ / | | |   | | | |__ | |_/ / .  . | | | |  \| |/ /_\ \| |    
|  _  || . ` | | | |    /| | | |   | | |  __||    /| |\/| | | | | . ` ||  _  || |    
| | | || |\  | |/ /| |\ \| |_| |   | | | |___| |\ \| |  | |_| |_| |\  || | | || |____
\_| |_/\_| \_/___/ \_| \_|\___/    \_/ \____/\_| \_\_|  |_/\___/\_| \_/\_| |_/\_____/ [Version 1.0.0]
""")



path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
while True:
	#print("["+host_name +"@"+host_ip+"]")
	print( "["+host_name +" @ "+host_ip+"]")
	code = input(">> ")
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
	if code == 'time':
		print ("Local Time : %s" % e)
	if code == 'list':
		os.system("dir")
	if code == 'move to':
		moveto = input("move to ")
		os.chdir(moveto)
	if code == 'echo':
		echo = input("echo ")
		print(echo)
	if code == 'help':
		print("info - to show terminal info")
		print("ping  -  to ping website")
		print("local -  to show host information")
		print("time  -  to show date")
		print("list  -  to show list in yout directory")
		print("move to -  change directory")
		print("current - to show current directory path")
		print("echo  -  to print something")
		print("help  -  to show command list")
		print("banner - print banner")
		print("create file - create a file")
		print("read file - read a file")
		print("write file - write a file")
		print("copy file - copy a file")
		print("hardware  -  to show hardware info")
		print("shutdown  -  to shutdown your pc")
		print("restart  -  to restart your pc")
		print("get  -  to download a file from website")
		print("get mp4  -  to download video from youtube")
		print("get audio  -  to download video from youtube")
		print("kill me  -  to end terminal")
	if code == 'banner':
		#file = open("art.txt", "r")
		#print (file.read())
		print("""\
		 ___   _   _____________ _   _   _____ ______________  ________ _   _   ___   _     
		 / _ \ | \ | |  _  \ ___ \ | | | |_   _|  ___| ___ \  \/  |_   _| \ | | / _ \ | |    
		/ /_\ \|  \| | | | | |_/ / | | |   | | | |__ | |_/ / .  . | | | |  \| |/ /_\ \| |    
		|  _  || . ` | | | |    /| | | |   | | |  __||    /| |\/| | | | | . ` ||  _  || |    
		| | | || |\  | |/ /| |\ \| |_| |   | | | |___| |\ \| |  | |_| |_| |\  || | | || |____
		\_| |_/\_| \_/___/ \_| \_|\___/    \_/ \____/\_| \_\_|  |_/\___/\_| \_/\_| |_/\_____/
			""")
	if code =='kill me':
		sys.exit()
	if code == 'create file':
		text = input("file name : ")
		file = open(text, "w")
		file.close()
	if code == 'hardware':
		print('OS : {0}'.format(os_name))
		print('OS Version : {0}'.format(os_version))
		print('CPU : {0}'.format(proc_info.Name))
		print('RAM : {0} GB'.format(system_ram))
		print('GPU : {0}'.format(gpu_info.Name))
	if code == 'shutdown':
		os.system("shutdown /s /t 0")
	if code == 'restart':
		os.system("shutdown /r /t 0")
	if code == 'get':
		url = input("get ")
		filename = wget.download(url)
	if code == 'get mp4':
		YTurl = input("get mp4 ");
		dld=YTurl.strip() 
		downloader_funct()
	if code == 'get audio':
		url = input("get audio ")
		video = pafy.new(url)
		bestaudio =video.getbestaudio()
		bestaudio.download()
	if code == 'current':
		print(os.getcwd())
		#print(os.getcwd()+"\\haha")
	if code == 'copy':
		source = input("copy ")
		destination = input("to ")
		try:
			shutil.copy(source,destination)
		except shutil.SameFileError:
			print("Source and destination represents the same file!")
		except PermissionError:
			print("Permission denied!")
		except:
			print("Failed copying file! Please contact us on instagram @filsuf_mengembara")
	if code == 'info':
		print("Andru Terminal [Version 1.0.0]")
		print("Open Source Terminal created by Andru Baskara")
	if code == 'read file':
		test= input("file to read ")
		file = open(test, "r")
		output=file.read()
		print(output)
		file.close()
	if code == 'write file':
		test = input("file to write ")
		file = open(test, "w")
		edit= input("")
		file.write(edit)
		file.close()
	if code == 'remove file':
		text=input("delete ")
		os.remove(text)

	
		