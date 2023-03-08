from SoundSys.TextToSpeech import *

print('Please enter the phrase you want the file to say..')
x = input()

print('Please enter a relevant file name..')
y = input()
save_msg_to_cache(x, y)

print('Do you want to retry and over right file name (Y/N)')
z = input()
if z == "Yes" or z == "True" or z == "Y" or z =="y":
    save_msg_to_cache(x, y,True)

print('Success :)')
