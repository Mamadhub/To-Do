import sys 
import file

def print_menu():
   
    print('1_ Edit_List:')
    print('2_ New_List :')
    print('3_ Add_Note:')
    print('4_ Exit:')


def edit_list():
    
    pass

def new_list():
    pass

def add_note():
    pass


def input_menu():
    number_input = 0
    while number_input not in [1, 2, 3, 4]:
        number_input = int(input("please enter number (1 , 2 , 3 , 4): "))
    
    if number_input == 1:
        edit_list()
    if number_input == 2:
        new_list()
    if number_input == 3:
        add_note()
    if number_input == 4:
        print('good byyy !!!')
        sys.exit()
            
        
            
    
    
def menu():
    print_menu()
    
    input_menu()
    
menu()