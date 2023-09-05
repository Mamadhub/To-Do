class filesss:
    
    def __init__(self):
        self.files_name = []
        self.files_data = {}
        
    
    def files_read(self):
        files = open("filess/files.txt", 'r')
        print(files.read())
        
    def new_file(self, name_file:str, note):
        file = open(f'filess/{name_file}.txt', 'w')
        files = open("filess/files.txt", 'a')
        files.write(f'{name_file}')
        file.write(note)
        self.files_data[name_file] = note
                
    def load_file(self, name):
        file = open(f"filess/{name}.txt", 'r')
        return file.read()
    
    def load_name_files(self):
        i = ''
        files = open("filess/files.txt", 'r')
        file = files.read()
        for name in file:
            if name == ' ':
                self.files_name.append(i)
                i = ''
            else: 
                i += name 
            
        files.close()  
           
    def create_dic_files(self):    
        for name in self.files_name:
            self.files_data[name] =  self.load_file(name)

    def add_text(self, name, added_text):
        file = open(f'filess/{name}.txt', 'a')
        file.write(added_text)
        
    def show_text(self, name):
        self.load_name_files()
        self.create_dic_files()
        print(self.files_data[name])
       

    
    





