import pyperclip
import string
import random
class User:
    '''
    Class to create user accounts and save their credentials
    '''
    users_list = []
    def __init__(self,first_name,last_name,password):
        '''
        Methods to define each user object properties
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    def save_user(self):
        '''
        Function to save a new user
        '''
        User.users_list.append(self)
class Credential:
    '''
    Class to create a password account,generate password and save
    '''
    credentials_list =[]
    user_credentials_list = []
    def __init__(self,user_name,site_name,account_name,password):
        '''
        Method to define the properties for each userobject holds
        '''
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password
    def save_credentials(self):
        '''
        Function to save a newly created user instance
        '''
        Credential.credentials_list.append(self)
    def delete_credentials(self):
        '''
        Function to delete saved credentials
        '''
        Credential.credential_list.remove(self)
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass 
    @classmethod
    def display_credentials(cls,user_name):
        '''
        Class method to display the list of credentials saved
        '''
        user_credentials_list = []
        for credential in cls.credentials_list:
            if credential.user_name == user_name:
                user_credentials_list.append(credential)
        return user_credentials_list
    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method that takes in a site_name and returns a credential that matches that site_name.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential
    @classmethod
    def copy_credential(cls,site_name):
        '''
        Class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_site_name(site_name)
        return pyperclip.copy(find_credential.password)
