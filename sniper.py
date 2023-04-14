import time
from pynput.mouse import Controller, Button
import keyboard
#pip install pynput
#pip install keyboard

mouse = Controller()

print("Sniper. Snipe a minecraft username.")
print("Put your page in half.")
print('Instruction :\n\nGo to minecraf.net.\nGo to the section where you change your minecraft name.\nWrite the name that you want.\nClick "Inspect" on the change your name button.\nChange to this <button aria-disabled="false" type="submit" class="btn btn__success change-profile-name__update-btn" aria-label="Change Profile Name" data-aem-contentname="Change Profile Name" enabled="">Change Profile Name</button>.\nPush x to stop.')
print("Start in 3 seconds...")

time.sleep(3)

boucle = True

while boucle == True:
    mouse.position = (100, 775)
    time.sleep(0.09)
    mouse.click(Button.left)
    mouse.position = (500, 320)
    time.sleep(0.09)
    mouse.click(Button.left)
    if keyboard.is_pressed("x"):
        print("X is pressed")
        break