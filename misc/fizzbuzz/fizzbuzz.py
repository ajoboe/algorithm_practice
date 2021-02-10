import sl4a
import time

droid = sl4a.Android()

for i in range(21):
 if(i%3 == 0):
  droid.ttsSpeak("fizz") #print('fizz')*/
 if(i%5 == 0):
  droid.ttsSpeak("buzz") #/*print('buzz')*/
 if(i%3 != 0 and i%5 != 0):
  droid.ttsSpeak(i) #/* print(i) */