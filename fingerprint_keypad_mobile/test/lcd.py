import key
from time import sleep
from Adafruit_CharLCD import Adafruit_CharLCD

# instantiate lcd and specify pins
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2)
lcd.clear()
keys=[1]
keyStr=''
# display text on LCD display \n = new line
try:
   keyStr=str(keys)
   keyStr=keyStr[1 :-1]
   
   lcd.message('Input key:\n')
   lcd.message(keyStr)   

except KeyboardInterrupt:
   lcd.clear()


#lcd.massage()
# scroll text off display
#for x in range(0, 16):
 #  lcd.move_right()
  # sleep(.1)
#sleep(3)
# scroll text on display
#for x in range(0, 16):
 #   lcd.move_left()
  #  sleep(.1)
