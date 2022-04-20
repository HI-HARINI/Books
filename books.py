from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry("600x600")
root.title("Canvas Using Functions")

class Citizen():
    def __init__(self,name,author,price,published):
        self.citizen_name=name
        self.citizen_author=author
        self.citizen_price=price
        self.citizen_published=published
    
    def add_citizen(self):
        print("Book Name:"+self.citizen_name)
        print("Book Author:"+self.citizen_author)
        print("Book Price:"+self.citizen_price)
        print("Published:"+self.citizen_published)
        print("Book Added")

c1=Citizen("It Ends with us","Colleen Hoover","25$","22,November,1995")
c1.add_citizen()
c2=Citizen("The Spanish Love Deception","Elena Armas","25$","13,April,2021")
c2.add_citizen()