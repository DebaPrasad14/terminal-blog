__author__ = "Deba M"


from database import Database
from models.blog import Blog



class Menu(object):

    def __init__(self):
        # ask user for author name
        # check if they've already got an account
        # if not prompt them to create one
        self.user = input("Enter the author name: ")
        if self._user_has_account():
            print("welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()


    def _user_has_account(self):
        blog = Database.find_one('blogs',{'author': self.user})
        if blog is not None:
            self.user_blog= Blog.from_mongo(blog['id'])
            return True
        else:
            return False


    def _prompt_user_for_account(self):
        title = input("Enter blog tilte: ")
        description = input("Enter blog description: ")
        blog = Blog(author=self.user, title=title, description=description)

        blog.save_to_mongo()
        self.user_blog = blog


    def run_menu(self):
        #user read or write blogs ?
        #if read:
            #list blogs in db
            #allow user to pick one
            #display posts
        # if write:
            #check if user has a blog ?
            # if they do, prompt to write blog
            #if not , prompt to create new blog

        read_or_write = input("Do u want to read (R) or write (W) blogs ?" )
        if read_or_write == 'R':
            # list blogs in db
            # allow user to pick one
            # display posts
            self._list_blogs()
            self._view_blogs()

        elif read_or_write == 'W':
            #prompt to write post
            self.user_blog_new_post()
        else:
            print("Thank you for beginning!")



    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))


    def _view_blog(self):
        blog_to_see = input("Enter the ID of blog u'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        for post in posts:
            print("Dare: {}, Title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))

