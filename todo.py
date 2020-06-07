#!/usr/bin/python
#
# IMPORT MODULES
#
import Adafruit_SSD1306, subprocess, datetime, gpiozero, time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from signal import pause
from imapclient import IMAPClient

#
# OLED CONFIGURATION
#
RST = 24
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)

# LOAD FONTS
font0 = ImageFont.truetype('/root/OLED/fonts/monospace.ttf', 10)
font1 = ImageFont.load_default()

# Buttons and ledS  definition
led = gpiozero.LED(4)
RGBled = gpiozero.RGBLED(red=14,green=15,blue=18)

# DEFINO KEYPAD

Fila1 = gpiozero.Button(5)
Fila2 = gpiozero.Button(6)
Fila3 = gpiozero.Button(13)
Fila4 = gpiozero.Button(19)
Colu1 = gpiozero.LED(12)
Colu2 = gpiozero.LED(16)
Colu3 = gpiozero.LED(20)
Colu4 = gpiozero.LED(21)

# FUNCION CLEAR DISPLAY
def limpio():
 draw.rectangle((0,0,width,height), outline=0, fill=0)
 disp.clear()
 disp.display()

# FUNCTION SHOW DISPLAY
def muestra():
 disp.image(image)
 disp.display()

# Function blink led
def blink_led():
 led.on()
 time.sleep(1)
 led.off()

# Function blink RGBled
def blink_rgb():
 RGBled.color = (0, 0, 1)
 time.sleep(1)
 RGBled.color = (0, 1, 0)
 time.sleep(1)
 RGBled.color = (0, 1, 1)
 time.sleep(1)
 RGBled.color = (1, 0, 0)
 time.sleep(1)
 RGBled.color = (1, 0, 1)
 time.sleep(1)
 RGBled.color = (1, 1, 0)
 time.sleep(1)
 RGBled.color = (1, 1, 1)
 time.sleep(1)
 RGBled.color = (0, 0, 0)
 time.sleep(1)

# Function nula
def nula():
 time.sleep(.2)

# Function Ready
def Ready():
  limpio()
  draw.text((0, 0), "Program Ready!" , font=font0, fill=1)
  muestra()
  time.sleep(1)
  limpio()

# Funcion mailcheck
def mailcheck():
 HOSTNAME = 'imap.gmail.com'
 MAILBOX = 'Inbox'

 # check mail every 60 seconds
 MAIL_CHECK_FREQ = 600

 # The following three variables must be customized for this
 # script to work
 USERNAME = ''
 PASSWORD = ''

 # my unread messages never goes to zero, use this to override

 NEWMAIL_OFFSET = 1

 # login to mailserver
 server = IMAPClient(HOSTNAME,use_uid=True, ssl=True)
 server.login(USERNAME, PASSWORD)

 # select our MAILBOX and looked for unread messages
 unseen = server.folder_status(MAILBOX, ['UNSEEN'])

 # number of unread messages
 # print to console to determine NEWMAIL_OFFSET
 newmail_count = (unseen['UNSEEN'])
 # print('%d unseen messages' % newmail_count)
 if newmail_count > NEWMAIL_OFFSET:
      mailn =  str(newmail_count) + ' emails sin leer.'
 else:
      mailn = 'No hay email sin leer.'

 return mailn

# MAIN PROGRAM
Ready()
while True:
 Colu1.off()
 Colu2.on()
 Colu3.on()
 Colu4.on()
 if Fila1.is_pressed:
    limpio()
    # Fecha Inicio Cuarentena
    fecha1 = datetime.datetime(2020,3,13,21,00)
    fecha2 = datetime.datetime.now()
    diff = fecha2 - fecha1
    draw.text((0, 0), "Quarantine time:", font=font1, fill=255)
    draw.text((0, 15), str(diff)[:17], font=font0, fill=255)
    muestra()
    nula()
    limpio()
 elif Fila2.is_pressed:
    limpio()
    draw.text((0, 0), "Secuencia Led RGB.", font=font1, fill=255)
    muestra()
    nula()
    limpio()
    blink_rgb()
 elif Fila3.is_pressed:
    limpio()
    cmd = "hostname -I|awk '{print $1}'"
    IP = subprocess.check_output(cmd, shell = True )
    draw.text((0, 0), "Ip Address:", font=font1, fill=255)
    draw.text((0, 20), str(IP) , font=font0, fill=1)
    muestra()
    nula()
    limpio()
 elif Fila4.is_pressed:
    limpio()
    draw.text((0, 0), "Led on 1 second", font=font0, fill=1)
    muestra()
    nula()
    blink_led()
    limpio()
 Colu1.on()
 Colu2.off()
 Colu3.on()
 Colu4.on()
 if Fila1.is_pressed:
    limpio()
    image = Image.open('images/happycat_oled_64.ppm').convert('1')
    muestra()
    time.sleep(3)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    limpio()
 elif Fila2.is_pressed:
    limpio()
    texto = mailcheck()
    draw.text((0,0), str(texto), font=font1, fill=1)
    muestra()
    nula()
 elif Fila3.is_pressed:
    limpio()
    draw.text((0,0), "Fila 2, Columna 3", font=font1, fill=1)
    muestra()
    nula()
 elif Fila4.is_pressed:
    limpio()
    draw.text((0,0), "Fila 2, Columna 4", font=font1, fill=1)
    muestra()
    nula()
 Colu2.on()
 Colu3.off()
 if Fila1.is_pressed:
    limpio()
    draw.text((0,0), "Fila 3, Columna 1", font=font1, fill=1)
    muestra()
    nula()
 elif Fila2.is_pressed:
    limpio()
    draw.text((0,0), "Fila 3, Columna 2", font=font1, fill=1)
    muestra()
    nula()
 elif Fila3.is_pressed:
    limpio()
    draw.text((0,0), "Fila 3, Columna 3", font=font1, fill=1)
    muestra()
    nula()
 elif Fila4.is_pressed:
    limpio()
    draw.text((0,0), "Fila 3, Columna 4", font=font1, fill=1)
    muestra()
    nula()
 Colu3.on()
 Colu4.off()
 if Fila1.is_pressed:
    limpio()
    draw.text((0,0), "Fila 4, Columna 1", font=font1, fill=1)
    muestra()
    nula()
 elif Fila2.is_pressed:
    limpio()
    draw.text((0,0), "Fila 4, Columna 2", font=font1, fill=1)
    muestra()
    nula()
 elif Fila3.is_pressed:
    limpio()
    draw.text((0,0), "Fila 4, Columna 3", font=font1, fill=1)
    muestra()
    nula()
 elif Fila4.is_pressed:
    limpio()
    draw.text((0,0), "Fila 4, Columna 4", font=font1, fill=1)
    muestra()
    nula()
 time.sleep(0.4)
