import sys 
from file_s import filesss
import edit_text as edit 
import time 

f = filesss()

def print_menu():
   
    print('1_ Edit_Note:')
    print('2_ New_Note :')
    print('3_ Exit:')
    print("4_ Show")


def edit_note():
    
    print('1_Delete')
    print('2_Add text')
    print('3_Change Name')
    
    number_input = int(input("please enter number : "))
    while number_input not in [1, 2, 3]:
        number_input = int(input("please enter number in range (1 , 2 , 3 ): "))
        
    if number_input == 1 :
        edit.delete_file()
    elif number_input == 2:
        edit.add_text()
        while 1:
            time.sleep(0.5)
            q = input("wait? (y/n):")
            if q == 'n':
                menu()        
    elif number_input == 3:
        edit.edit_name()



def new_note():
    name = input("please enter name : ")
    note = input('please enter note :')
    f.new_file(name, note)

def show_note():
    name = input


def input_menu():
    number_input = 0
    while number_input not in [1, 2, 3, 4]:
        number_input = int(input("please enter number (1 , 2 , 3 , 4): "))
    
    if number_input == 1:
        edit_note()
    if number_input == 2:
        new_note()
        while 1:
            time.sleep(0.5)
            q = input("wait? (y/n):")
            if q == 'n':
                menu() 
    if number_input == 4:
        show_note()
    if number_input == 3:
        print('good byyy !!!')
        sys.exit()
            
        
            
    
    
def menu():
    print_menu()
    input_menu()
    
menu()