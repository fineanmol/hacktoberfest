import os
import pyautogui
import subprocess
import time


person = input("The Person Who You Wanna Send The Message : ")

msg = input("Message : ")
t = int(input("How Many Times You Wanna Send The Message more [Limit : 20] : "))

if t > 20:
    print("Limit Exceeded")
    exit()


try:
     # Generally Windows Store Whatsapp.exe file here if you downloaded it from Microsoft Store | If it isnt there try finding the original path and paste it here below 
    subprocess.Popen("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2228.14.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe")
    time.sleep(15)

    
    # Make Sure Whatsapp is opening in fullscreen 
    
    # Will Click on search button
    pyautogui.click(169,100)
    
    # Will Write Person's Name 
    pyautogui.write(person, interval=0.25)
    time.sleep(.5)
    
    # Will Click on person 
    pyautogui.click(162,210)
    
    # Send Message 
    while t != 0:
        pyautogui.write(msg, interval=0.01)
        pyautogui.click(1328,681)
        t = t - 1
except:
    print("Error 404 ")

