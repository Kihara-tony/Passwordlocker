#!/usr/bin/env python3
import pyperclip
from user import User, Credential
def create_user(fname,lname,password):
    '''
    Function to create  a new account
    '''
    new_user = User(fname,lname,password)
    return new_user
def save_user(user):
    '''
    Function to save a new account
    '''
    User.save_user(user)
def verify_user(first_name,password):
    '''
    Function to verify user before creating password
    '''
    checking_user = Credential.check_user(first_name,password)
    return  checking_user
def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential
def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
def copy_credential(site_name):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(site_name)
def main():
	print(' ')
	print('Hi!!! Welcome to password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use the choices to navigate:\n ca-To Create An Account \n l-To Log In To Your Account  \n x-To Exit')
		short_code = input('Choose: ').lower().strip()
		if short_code == 'x':
			print(' ')
			print(f'Goodbye \n  hope to see you soon \n It was nice interacting with you dear .')
			break
		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account')
			first_name = input('Input your First Name: ').strip()
			last_name = input('Input Your Last Name: ').strip()
			password = input('Input Your Password: ').strip()
			save_user(create_user(first_name,last_name,password))
			print(' ')
			print(f'A New Account Was Created \n For {first_name} {last_name} \n using password {password}')
		
		
		elif short_code == 'l':
			print("-"*60)
			print(' ')
			print('To Log In Follow The Instructions: ')
			user_name = input('Input Your First Name: ').strip()
			password = str(input('Input Your Password: '))
			user_exists = verify_user(user_name,password)
			if user_exists == user_name:
				print(" ")
				print(f'Welcome {user_name}!! \n PLease Choose To Continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigate By: \n c-To Create A Credential \n d-To Display Credentials  \n cp-To Copy Password \n x- To Exit')
					short_code = input('Enter A Choice: ').lower().strip()
					print("-"*60)
					if short_code == 'x':
						print(" ")
						print(f'Goodbye \n {user_name} hope to see you soon \n It was nice interacting with you dear {user_name}.')
						break
					elif short_code == 'c':
						print(' ')
						print('Enter your Details: ')
						site_name = input ('Enter The Name Of Your Site:  ').strip()
						account_name = input('Enter Your Account\'s name: ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose One Option: \n p-To Enter Existing Password \n g-Generate A Password \n x-To Exit')
							psw_choice = input('Enter an Option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'p':
								print(" ")
								password = input('Enter Your Password: ').strip()
								break
							elif psw_choice == 'g':
								password = generate_password()
								break
							elif psw_choice == 'x':
								print(" ")
								print(f'Goodbye \n {user_name} hope to see you soon \n It was nice interacting with you dear {user_name}.')
								break
							else:
								print('You Entered A Wrong Option!!! \n Please Try Again.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(" ")
						print(f'Credential Created. \n Site Name: {site_name} \n Account Name: {account_name} \n Password: {password}')
						print(' ')
					elif short_code == 'd':
						print(' ')
						if display_credentials(user_name):
							print('Here is a list of your credentials')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} \n Account Name: {credential.account_name} \n Password: {credential.password}')
							print(' ')
						else:
							print(' ')
							print('You don\'t seem to contain any credentials saved yet' )
							print(' ')
					elif short_code == 'cp':
						print(' ')
						choosen_site = input('To copy password \n Enter the name of the site')
						copy_credential(choosen_site)
						print(' ')
					else:
						print('Sorry You Entered A Wrong Option \n Could You PLease Try Again.')
				else:
					print("-"*60)
					print(' ')
					print('Sorry You Entered A Wrong Option \n Could You PLease Try Again.')

if __name__ == '__main__':
	main()



