class file:
    
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
                
    def load_file(self, name):
        file = open(f"filess/{name}.txt", 'r')
        return file.read()
    
    def load_name_files(self):
        files = open("filess/files.txt", 'r')
        file = files.read()
        for name in file:
            if name == ' ':
                continue 
            else: 
                self.files_name.append(name) 
        files.close()  
           
    def create_dic_files(self):    
        for name in self.files_name:
            self.files_data[name] =  self.load_file(name)

    
    
f = file()




