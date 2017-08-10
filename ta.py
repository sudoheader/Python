import os
import time

def start(inv):
	print('\nYou are in front of the house. What are you doing?')
	print('\n1 Open  the door')
	print('2 Examine the mailbox')
	print('3 Look under the mat')
	print('4 Look through the window')

	selectionlist = ['1', '2', '3', '4']
	choice = selectchoice(selectionlist)

	if choice == '1':
		if 'key' in inv:
			os.system('clear')
			print('You open the door with the key')
			inside(inv)
		else:
			os.system('clear')
			print("The door is closed. You'll need a key.")
			time.sleep(2)
			start()
	elif choice == '2'
		os.system('choice')
		print('You open the mailbox and find a harddisk')
		time.sleep(1)
		print('What are you doing?')
		print('\n1 Take the harddisk and close the mailbox')
		print('\n2 Open the door')

		selectionlist = ['1', '2']
		choice = selectchoice(selectionlist)
		if choice == '1'
			inv.append('harddisk')
			print('You take the harddisk and close the mailbox')
			time.sleep(2)
			start()
		elif choice == '2'
			print('\nYou close the mailbox.')
			time.sleep(2)
			start()
	if choice == '3'
		os.system('choice')
		print('\nThere is a key under the mat')
		time.sleep(1)
		print('What are you doing')
		
		print('\n1 Take the harddisk and close the mailbox')
		print('\n2 Open the door')

		selectionlist = ['1', '2']
		choice = selectchoice(selectionlist)
		if choice == '1'
			inv.append('harddisk')
			print('You take the harddisk and close the mailbox')
			time.sleep(2)
			start()
		elif choice == '2'
			print('\nYou close the mailbox.')
			time.sleep(2)
			start()

def selectchoice(selectionlist):
	choice = input('\n?')
	if choice in selectionlist:
		return choice
	elif choice == 'quit':
		exit(0)
	else:
		print('Invalid input')
		return selectchoice(selectionlist)

def inside(inv):
	print('\nYou are inside the house')

os.system('clear')
inv=['']
start(inv)
