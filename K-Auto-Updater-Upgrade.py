import os
import sys
import platform
import time
import random

colour=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m']
normal=('\033[1;m')

try:

	def banner():
		print('*'*80)
		print(random.choice(colour)+'Created by Pierce2r'+normal).center(80)	
		print(random.choice(colour)+'K-Auto Updater && Upgrade'+normal).center(80)
		print('*'*80)

	def platfrm():
		plat=platform.uname()
		platf = plat[2]
		print ('[*] Release Version: '+platf)
		print('')

	def directory():
		a=os.chdir('/etc/apt/')
		print('[*] changing directory to /etc/apt/')
		time.sleep(3)
		b=os.getcwd()	
		print('[*] currently in '+ b)
		print ('')
		file = open('sources.list','r')
		c=file.read()
		print ('[*] File Contains: '+c)
		print('')
		fil = open('sources.list','w')
		d=fil.write('#The kali-rolling repository\ndeb http://http.kali.org/kali kali-rolling main non-free contrib')
		fil.close()
		time.sleep(3)
		print('[*] Written to file completed...')
		print('')
		fi=open('sources.list','r')
		e=fi.read()
		print  ('[+] Current File Content '+e)
		print('')
		fi.close()
	
	def update():
		print('[*] System about to update and upgrade')
		print('')
		time.sleep(3)
		os.system('apt update')
		print('[*] System update')
		print('')
		os.system('apt dist-upgrade -y')
		print('')
		print('[*] System upgrade completed')
		print('')
		reb=raw_input('Would you like to reboot [y/n]:')
		re=reb.lower()
		if re is 'y':
			print('[*] System about to reboot')
			time.sleep(3)
			os.system('reboot')
		else:
			print(random.choice(colour)+'Rebooting your system would be much better'+normal)
			print('')
	banner()
	platfrm()
	directory()
	update()


except KeyboardInterrupt:
	os.system('clear')
	sys.exit()
		





