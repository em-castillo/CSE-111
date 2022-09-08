'''Alarm App Project'''

# Import libraries and modules
from tkinter import *  # GUI
from tkinter import messagebox  # message
import time  # time
from pygame import mixer  # sound


def main():
    create_window()


def create_window():
    '''Creates GUI window'''
    # Create the Tk root object.
    root = Tk()
    # Title
    root.title('Alarm App')
    # Size
    root.geometry('450x300')
    # color
    root.configure(background='#4a7abc')

    # header
    header = Frame(root)
    header.place(x=5, y=5)

    # panel
    panel = Frame(root)
    panel.place(x=30, y=30)

    # image
    image = PhotoImage(file='alarm_app/alarm_img.png')

    # Labels
    img = Label(panel, image=image)
    lbl_time = Label(panel, text='Enter time in 24 hrs\n format (HH:MM):')
    message = Label(panel, text='Enter message:')

    # Entries
    global ent_time, ent_msg  # global variables
    ent_time = Entry(panel, width=10)
    ent_msg = Entry(panel, width=10)

    # Button
    btn_enter = Button(panel, text='Set Alarm', width=10, height=2,  fg='#4a7abc', font=('Times New Roman', 18),
                       command=alarm)

    # Grid
    img.grid(row=1, column=0)
    lbl_time.grid(row=1, column=1)
    ent_time.grid(row=1, column=2, padx=20)
    message.grid(row=2, column=1)
    ent_msg.grid(row=2, column=2)
    btn_enter.grid(row=3, column=1, padx=20, pady=30)

    # Start the tkinter loop that processes user events
    root.mainloop()


def set_alarm():
    '''Sets alarm by user'''
    alarm_set = ent_time.get()
    # displays message
    messagebox.showinfo('Alarm Clock', f'The alarm time is: {alarm_set}')


def alarm():
    '''Does alarm logic'''
    # global ent_time, ent_msg
    alarm_time = ent_time.get()
    if alarm_time == '':
        messagebox.showerror('Alert', 'Please enter time.')

    else:
        set_alarm()
        # gets current time from computer
        currentTime = time.strftime("%H:%M")
        global alarm_msg
        alarm_msg = ent_msg.get()

        while alarm_time != currentTime:
            currentTime = time.strftime("%H:%M")

            if alarm_time == currentTime:
                sound()


def sound():
    '''Plays alarm sound'''
    mixer.init()
    mixer.music.load('alarm_app/alarm_sound.wav')
    mixer.music.play()
    messagebox.showinfo('It is time!', f'{alarm_msg}')


if __name__ == "__main__":
    main()
