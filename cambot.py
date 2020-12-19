import sys
import time
import random
import datetime
import telepot
import picamera
import threading
import log
import local_opt

token = local_opt.CAMBOT_TOKEN
img_path = local_opt.IMG_PATH 

chat_id = 0
send_periodic = False
id_check = 0

def img_take(chat_id):
    camera.capture(img_path)
    countdown_timer = 30
    bot.sendMessage(chat_id, 'Invio foto in corso...')
    bot.sendPhoto(chat_id, photo=open(img_path, 'rb'))


def tick():
    global send_periodic #Qua saremmo in ambito locale, quindi bisogna specificare che  che si fa ririferimento a una variabile locale
    global chat_id
    
    if send_periodic == True:
        img_take(chat_id)
        
    
    threading.Timer(1.0, tick).start()
    
    
    
    
def handle(msg):
    global send_periodic
    global chat_id
    global id_check
    chat_id = msg['chat']['id'] #Che notazione e'questa?
    command = msg['text']
  
    print(command, chat_id)
    
    data_logger=log.logger()
    data_logger.do_log(command)
    
    id_list = open(local_opt.ID_LIST_PATH, 'r') 
    id_listed = id_list.readlines()
    
    for i in id_listed:
        print(i,str(chat_id))
        if(i == str(chat_id)):
            print("Id rilevato in lista")
            id_check = 1

    if id_check == 0:
        if command == local_opt.PSWD:
            bot.sendMessage(chat_id, 'Chat registrata!')
            data_logger.log_new_chat_id(chat_id)
            
        else:
            bot.sendMessage(chat_id, 'Chat non registrata. Inserire password')
            
    elif id_check == 1:
        if command == '/get':
            img_take(chat_id)
            
        if command == '/start':
            send_periodic = True
            
        if command == '/stop':
            send_periodic = False
        
        
        
#TOKEN = sys.argv[1]  # get token from command-line
camera = picamera.PiCamera()
camera.rotation=180
bot = telepot.Bot(token)
bot.message_loop(handle)


tick()
print ('Ready for commands ...')


