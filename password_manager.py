import local_opt

class password_system:
    def __init__(self):
        f_id = open(local_opt.ID_LIST_PATH, 'a+')
        f_id.close()
    
    def load_db_file(self):
        f_id = open(local_opt.ID_LIST_PATH, 'r')
        self.id_db_list = f_id.readlines()
        f_id.close()
    
    def insert_db_file(self,chat_id):
        f_id = open(local_opt.ID_LIST_PATH,"a")
        f_id.write(str(chat_id)+"\n")
        f_id.close()
    
    def check_id(self,chat_id):
        str_id = str(chat_id)+"\n"
        if (str_id in self.id_db_list):
            return True  
        else: 
            return False
    
    id_db_list = 0