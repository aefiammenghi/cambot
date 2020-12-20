
import telepot
import picamera
import local_opt
import cambot

my_cam=cambot.c_cambot()
my_cam.token = local_opt.CAMBOT_TOKEN
my_cam.img_path = local_opt.IMG_PATH 
my_cam.camera = picamera.PiCamera()
my_cam.camera.rotation=180
my_cam.bot = telepot.Bot(my_cam.token)
my_cam.bot.message_loop(my_cam.handle)
my_cam.tick()

print ('Ready for commands ...')
