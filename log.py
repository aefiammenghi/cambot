import datetime
import local_opt

class logger:
    def __init__(self):
        pass
    
    def do_log(self, data):
        log_time = datetime.datetime.now()
        file = open(local_opt.LOG_PATH,"a")
        log_line = log_time.strftime("%Y-%m-%d %H:%M:%S") + "  " + data + "\n"
        file.write(log_line);
        
    def log_new_chat_id(self, chat_id):
        file = open(local_opt.ID_LIST_PATH,"a")
        log_line = chat_id 
        file.write(str(log_line));