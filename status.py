import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BOARD)
GPIO.setup(16,GPIO.IN)
var=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i=0
a=0
t=0
n=0
while (t<2):
	 while ( i < 20 ):
                        var[i]=GPIO.input(16)
			i=i+1
			time.sleep(0.05)
	 i = 1
	 a=var[0]
	 n1 = 0
	 
          
	 while (i<20):
	   	if(var[i]== a):
			n1=n1+1
		a=var[i]
		i=i+1
	 if(n1 <= 15):
		n=n+1
		
	 
		
	 i=0
	 a=0
	 t=t+1
	 
if n==2:
		print ("Ligado")
else:
		print ("Desligado")
	