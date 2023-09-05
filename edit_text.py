import os
from file_s import filesss 

f = filesss()

def add_text():
    
    while 1:
        try:
            name = input('please enter name file :')
            text = input("text :")
            f.add_text(name, text)
            f.files_data[name] += text
            break
        except:
            again = input("not found. again(y/n):")
            if again.lower() == 'n':
                break
            else:
                continue

def delete_file():
    while 1:
        try:
            name = input('please enter name file :')
            os.remove(f'filess/{name}.txt')
            break
        except:
            again = input("not found. again(y/n):")
            if again.lower() == 'n':
                break
            else:
                continue
    
    
def edit_name():
    while 1:
        try:
            name = input('please enter name file :')
            new_name = input('please enter new name file :')
            os.rename(f'filess/{name}.txt',f'filess/{new_name}.txt' )
            break
        except:
            again = input("not found. again(y/n):")
            if again.lower() == 'n':
                break
            else:
                continue