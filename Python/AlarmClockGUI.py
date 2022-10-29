from tkinter import *
from tkinter import font
import pygame.mixer as mixer
import datetime
"""
install the following dependencies in your environment by this command:
pip install pygame
"""


class Clock(Frame):
    def __init__(self, root):
        """Constructor method to intialise sound, GUI Window, and real-time time track"""
        super().__init__(root)
        self.status=False
        self.alarm_info=StringVar()
        self["bg"]="#bfc9ca"
        self.place(x=0,y=0,width=400,height=300)
        self.info_label=Label(self,bg="#bfc9ca",font=("Arial",15),fg="#ec7063",textvariable=self.alarm_info)
        self.info_label.place(x=50,y=100,width=300,height=25)
        mixer.init()
        self.sound=mixer.Sound(file='/path/to/alarm/file') #Add path file of alarm sound in '.wav' format
        self.time_label()
        self.time_update()
        self.set_stop_button()
        self.alarm_entries()

    def alarm_entries(self):
        """
        Alarm entries label.
        A spinbox to select time
        """
        self.num_font=font.Font(family="Arial",size=20)
        self.hours_spinbox=Spinbox(self,fg="#283747",cursor="arrow",buttoncursor="hand2",from_=1,to=12,font=self.num_font,wrap=True,bd=0,state="readonly",justify=CENTER)
        self.hours_spinbox.place(x=50,y=150,width=75,height=50)
        self.minute_spinbox=Spinbox(self,fg="#283747",cursor="arrow",buttoncursor="hand2",from_=0,to=59,font=self.num_font,wrap=True,bd=0,state="readonly",justify=CENTER)
        self.minute_spinbox.place(x=150,y=150,width=75,height=50)
        self.am_pm_spinbox=Spinbox(self,fg="#283747",cursor="arrow",buttoncursor="hand2",values=("AM","PM"),wrap=True,font=("Arial",20),state="readonly",bd=0,justify=CENTER)
        self.am_pm_spinbox.place(x=275,y=150,height=50,width=75)

    def set_stop_button(self):
        """
        Buttons for Alarm functions like: STOP, SNOOZE, SET
        """
        self.button_font=font.Font(family="Arial",size=18)
        self.set_button=Button(self,bg="#ec7063",activebackground="#ec7063",activeforeground="white",text="Set",bd=0,fg="white",font=self.button_font,command=self.set_alarm)
        self.set_button.place(x=275,y=225,width=100,height=50)
        self.snooze_button=Button(self,bg="#ec7063",activebackground="#ec7063",activeforeground="white",text="Snooze",bd=0,fg="white",font=self.button_font,command=self.snooze_alarm)
        self.snooze_button.place(x=150,y=225,width=100,height=50)
        self.stop_button=Button(self,bg="#ec7063",text="Stop",activebackground="#ec7063",activeforeground="white",bd=0,fg="white",font=self.button_font,command=self.stop_alarm)
        self.stop_button.place(x=25,y=225,width=100,height=50)

    def set_alarm(self):
        """Method to set the alarm for the time on pressing SET button"""
        if not self.status:
            self.alarm_music = False
            hours = int(self.hours_spinbox.get())
            self.minutes = int(self.minute_spinbox.get())
            am_pm=self.am_pm_spinbox.get()
            if am_pm=="PM":
                if hours != 12:
                    hours += 12
                self.time_obj = datetime.time(hour=hours,minute=self.minutes)
            else:
                if hours == 12:
                    hours -= 12
                self.time_obj = datetime.time(hour=hours,minute=self.minutes)
            stri = "Alarm set for {}".format(self.time_obj.strftime("%I:%M:%S %p"))
            self.alarm_info.set(stri)
            self.status=True
            self.snoozeobj = self.time_obj

    def time_difference(self):
        """
        To calculate the minutes for snooze function:
        If the time set in the alarm is more than 55 in minutes, Snooze time is in the next hour.
        """
        alarm_hour=self.snoozeobj.hour
        min = self.snoozeobj.minute
        if min >=55:
            min %= 5
            alarm_hour = alarm_hour+1 if alarm_hour+1 <= 12 else (alarm_hour+1) % 12
        else:
            min += 5
        self.snoozeobj = datetime.time(hour=alarm_hour, minute=min)
        print(f'Snooze Time:{self.snoozeobj.strftime("%I:%M:%S %p")}')

    def stop_alarm(self):
        """Stop the alarm sound and clear the alarm time set"""
        if self.status:
            self.alarm_info.set("")
            self.sound.fadeout(500)
            self.status=False

    def time_label(self):
        # To display the real-time information of the clock in Hours: Minutes: Seconds
        self.time_font=font.Font(family="hooge 05_53",size=40)
        self.label=Label(self,bg="#bfc9ca",fg="#5d6d7e",text="",font=self.time_font)
        self.label.place(x=0,y=0,width=400,height=100)

    def time_update(self):
        """
        Keep updating the clock time for every 200 milliseconds
        Trigger the alarm music on alarm set time or after snooze time(5 minutes)
        """
        if self.label["text"]!=datetime.datetime.today().strftime("%I:%M:%S %p"):
            self.label["text"]=datetime.datetime.today().strftime("%I:%M:%S %p")
        self.label.after(200,self.time_update)
        if self.status and not self.alarm_music:
                try:
                    if datetime.datetime.today().strftime("%I:%M:%S %p") == self.snoozeobj.strftime("%I:%M:%S %p"):
                        self.sound.play(-1, fade_ms=2000)
                        self.alarm_music = True
                except AttributeError:
                    if datetime.datetime.today().strftime("%I:%M:%S %p") == self.time_obj.strftime("%I:%M:%S %p"):
                        self.sound.play(-1, fade_ms=2000)
                        self.alarm_music = True

    def snooze_alarm(self):
        """
        Method to play the alarm sound every 5 minutes after the set alarm time.
        Runs until the stop button is pressed.
        """
        self.alarm_info.set(f"Alarm snoozed for 5 mins! ")
        self.sound.fadeout(500)
        self.alarm_music = False
        # An if condition to prevent user from spamming Snooze button!
        if datetime.datetime.now().strftime("%I:%M:%S %p") >= self.snoozeobj.strftime("%I:%M:%S %p"):
            self.time_difference()


# Main driver code
if __name__ == "__main__":
    root = Tk()
    root.geometry("400x300")
    root.title("Clock")
    root.resizable(False,False)
    obj = Clock(root)
    root.mainloop()