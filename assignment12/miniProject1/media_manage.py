from db import Data_base


db = Data_base("assignment12\miniProject1.txt")

class MediaManagement:
    def __init__(self, id, name, media_type, media):
        self.id = id
        self.name = name
        self.media_type = media_type
        self.media = media
        
    @staticmethod
    def add():
        id = input("enter code: ")
        name = input("enter name: ")
        media_type = input("enter price: ")
        media = input("enter count: ")
        new_MediaManagement = MediaManagement(code, name, price, count)
        db.data.append(new_MediaManagement)

    def edit(self):...
    @staticmethod
    def search():
        ...
    def remove(self):
        ...
    def show(self):
        ...
    @staticmethod
    def show_list():
        ...
    def buy(self):
        ...

