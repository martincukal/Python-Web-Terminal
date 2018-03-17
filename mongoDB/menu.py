__author__ = 'Martin Chukaleski'

from database import Database
from models.blog import Blog

class Menu(object):
    def __init__(self):
        self.user = input("Enter your name: ")
        self.user_blog = None
        if self.__user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        pass


    def __user_has_account(self):
        blog =  Database.find_one('blogs',{'author':self.user})

        if blog is not None:
            self.user_blog = blog
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = input("Enter blog title")
        description = input("Enter blog description")
        blog = Blog(self.user,title,description)
        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
       read_or_write = input("Do you want to read 'R' or write 'W' blogs")
       if read_or_write == 'R':

           pass
       elif read_or_write == 'W':
           pass
       else:
           print("Thank you gor blogging!")

