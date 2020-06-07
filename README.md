# OLED-Keypad
How to configure a Raspberrypi 3+ or Zero W to use a keypad and an OLED Display (I2C)



Hi!

This installation is pretty straightforward

1) Install  Pyhton and Adafruit OLED library from here: https://www.raspberrypi-spy.co.uk/2018/04/i2c-oled-display-module-with-raspberry-pi/

2) (Optional )Create a symbolic link from root's $HOME to /root/Adafruit_Python_SSD1306/examples

3) Change to directory to Adafruit_Python_SSD1306

4) git init

5) git clone https://github.com/guicastello/OLED-Keypad/

6) Shutdown the Raspberry

7) Connect display and keypad, verify wiring. TWICE!!!

8) Power up the Raspberry, login as root and execute python
