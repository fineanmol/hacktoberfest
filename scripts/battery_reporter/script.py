import os
import time
import smtplib
from email.message import EmailMessage

def send_mail(s):
    timepass , password = os.environ.get('email_address'),os.environ.get('email_password')
    msg = EmailMessage()
    msg['Subject']='Battery Alert'
    msg['From'] = timepass
    msg['To'] = timepass
    msg.set_content(s)
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(timepass,password)
        smtp.send_message(msg)
def send_message(s):
    command = f'notify-send "Battery Alert" \"{s}\"'
    os.system(command)
while(True):
    os.system('acpi > ./sdtout.txt')
    f = open('sdtout.txt','r')
    output = f.read()
    ls = output.split()
    status,percentage = ls[2][:-1],int(ls[3][:-2])
    if(status=='Discharging' and percentage<=15):
        s = 'Plug It In I Am Going to be Dead.'
        send_message(s)
        time.sleep(300)
    elif(status=='Charging' and percentage>=90):
        s = "Plug It Off i don't want do be overcharged!"
        send_message(s)
        time.sleep(300)
