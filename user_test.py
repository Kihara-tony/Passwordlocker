import unittest
import pyperclip
from user import User,Credential
class TestUser(unittest.TestCase):
	'''
	Test class that user behaviours
	Args:
	     unittest.TestCase:helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account
		'''
		self.new_user = User('Tony','Kihara','tnkz000')
	def test__init__(self):
		'''
		Test to if check the initialization of user instances is done properly
		'''
		self.assertEqual(self.new_user.first_name,'Tony')
		self.assertEqual(self.new_user.last_name,'Kihara')
		self.assertEqual(self.new_user.password,'tnkz000')

	def test_save_user(self):
		'''
		Test to check if the users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

class TestCredintials(unittest.TestCase):
	'''
	Test class that defines test cases
	Args:
	     unittest.TestCase:helps in creating test cases
	'''

	def test_check_user(self):
		'''
		Function to test whether the login in function works
		'''
		self.new_user = User('Tony','Kihara','tnkz000')
		self.new_user.save_user()
		user2 = User('Poul','Njenga','tnkz000')
		user2.save_user()

		for user in User.users_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user
		self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))
	def setUp(self):
		'''
		Function to create an account's credentials before each test
		'''
		self.new_credential = Credential('Tony','Facebook','tonkin','tnkz000')	
	def test__init__(self):
		'''
		Test to check the initialization of credential instances
		'''
		self.assertEqual(self.new_credential.user_name,'Tony')
		self.assertEqual(self.new_credential.site_name,'Facebook')
		self.assertEqual(self.new_credential.account_name,'tonkin')
		self.assertEqual(self.new_credential.password,'tnkz000')
# 	def test_save_credentials(self):
# 		'''
# 		Test to check if the new credentials are  saved
# 		'''
# 		self.new_credential.save_credentials()
# 		twitter = Credential('Tony','Twitter','tonkin','tnkz000')
# 		twitter.save_credentials()
# 		self.assertEqual(len(Credential.credentials_list),2)
# 	def test_delete_credentials(self):
# 		'''
# 		Test to check if the saved credentials are deleted
# 		'''
# 		self.new_credential.delete_credentials()
# 		twitter =Credential('Tony','Twitter','tonkin','tnkz000')
# 		twitter.delete_credentials()
# 		self.assertEqual(remove(Credential.credentials_list),2)
# 	def tearDown(self):
# 		'''
# 		Function to clear the credentials list after every test
# 		'''
# 		Credential.credentials_list = []
# 		User.users_list = []
# 	def test_display_credentials(self):
# 		'''
# 		Test to check if the display_credentials method, displays the correct credentials
# 		'''
# 		self.new_credential.save_credentials()
# 		twitter = Credential('Tony','Twitter','tonkin','tnkz000')
# 		twitter.save_credentials()
# 		gmail = Credential('Mary','Gmail','Virginmary','tnkz000')	
# 		gmail.save_credentials()
# 		self.assertEqual(len(Credential.display_credentials(twitter.user_name)),2)
# 	def test_find_by_site_name(self):
# 		'''
# 		Test to check if the find_by_site_name method returns the correct credential
# 		'''
# 		self.new_credential.save_credentials()
# 		twitter = Credential('Tony','Twitter','tonkin','tnkz000')
# 		twitter.save_credentials()
# 		credential_exists = Credential.find_by_site_name('Twitter')
# 		self.assertEqual(credential_exists,twitter)
# 	def test_copy_credential(self):
# 		'''
# 		Test to check if the copy a credential method copies the correct credential
# 		'''
# 		self.new_credential.save_credentials()
# 		twitter = Credential('Tony','Twitter','tonkin','tnkz000')
# 		twitter.save_credentials()
# 		find_credential = None
# 		for credential in Credential.user_credentials_list:
# 			find_credential =Credential.find_by_site_name(credential.site_name)
# 			return pyperclip.copy(find_credential.password)
# 		Credential.copy_credential(self.new_credential.site_name)
# 		self.assertEqual('tnkz000',pyperclip.paste())
# 		print(pyperclip.paste())






	  


  