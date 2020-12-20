import datetime
import local_opt

class logger:
    def __init__(self):
        pass
    
    def do_log(self,chat_id,data):
        log_time = datetime.datetime.now()
        file = open(local_opt.LOG_PATH,"a")
        log_line = log_time.strftime("%Y-%m-%d %H:%M:%S") + " ID:"+str(chat_id) + "  CMD:" + data + "\n"
        file.write(log_line);
        