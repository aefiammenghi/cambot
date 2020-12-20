import sys
import time
import random
import datetime
import telepot
import picamera
import threading
import log
import local_opt
import password_manager
import os

class c_cambot:
    
    def __init__(self):
        
        if (not os.path.exists(local_opt.LOG_DIR_PATH)):
            os.mkdir(local_opt.LOG_DIR_PATH)
            
        if (not os.path.exists(local_opt.PSWD_DIR_PATH)):
            os.mkdir(local_opt.PSWD_DIR_PATH)
            
        if (not os.path.exists(local_opt.TMP_DIR_PATH)):
            os.mkdir(local_opt.TMP_DIR_PATH)
                     
        self.password=password_manager.password_system()
        self.password.load_db_file()  #Loads the list of registered passwords
        
    
    def img_take(self,chat_id):
        self.camera.capture(self.img_path)
        self.bot.sendMessage(self.chat_id, 'Invio foto in corso...')
        self.bot.sendPhoto(self.chat_id, photo=open(self.img_path, 'rb'))

    def tick(self):
        
        if self.send_periodic == True:
            self.img_take(self.chat_id)
        
        threading.Timer(1.0, self.tick).start()
              
    def handle(self,msg):
        
        self.chat_id = msg['chat']['id'] #WTF?
        self.command = msg['text']
      
        print(self.command, self.chat_id)
        
        data_logger=log.logger()
        data_logger.do_log(self.chat_id,self.command)
        
        #Check if this ID is registered
        if (self.password.check_id(self.chat_id)==True):
            print("Id rilevato in lista")
            self.id_check = 1
        else:
            self.id_check = 0
        

        if (self.id_check == 0):
            if (self.command == local_opt.PSWD):
                self.bot.sendMessage(self.chat_id, 'Chat registrata!')
                self.password.insert_db_file(self.chat_id)
                self.password.load_db_file()  
            else:
                self.bot.sendMessage(self.chat_id, 'Chat non registrata. Inserire password')
                
        elif self.id_check == 1:
            if self.command == '/get':
                self.img_take(self.chat_id)
                
            if self.command == '/start':
                self.send_periodic = True
                
            if self.command == '/stop':
                self.send_periodic = False
        
    chat_id = 0
    send_periodic = False
    id_check = 0
    camera = 0
    img_path = 0
    chat_id = 0
    command = 0
    bot = 0
    password = 0