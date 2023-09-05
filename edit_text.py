import os
from file_s import filesss 

f = filesss()

def add_text():
    name = input('please enter name file :')
    text = input("text :")
    f.add_text(name, text)
    f.files_data[name] += text

def delete_file():
    name = input('please enter name file :')
    os.remove(f'filess/{name}.txt')
    
def edit_name():
    name = input('please enter name file :')
    new_name = input('please enter name file :')
    os.rename(f'filess/{name}.txt',f'filess/{new_name}.txt' )
    