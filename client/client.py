import socket
from threading import Thread
import tkinter
from tkinter import *
import time
import error

def receive(): # receive messages
    while True:
        try:
            msg = s.recv(1024).decode() # receive message and decode into str
            msg_list.insert(tkinter.END, msg) # insert new message at the end
        except Exception as ex:
            error.server_not_online(error)
            exit()

def send():
    global name_entered
    if name_entered == False:
        name_entered = True
        information.config(text = "ENTER YOUR MESSAGE")
    try:
        msg = my_msg.get()
        my_msg.set("")
        s.send(bytes(msg, "utf8")) # send message to server in encoded form
    except Exception as ex:
        error.cannot_send_message(ex)
        exit()

name_entered = False
window = Tk()
window_width = 1280
window_height = 720
window.title("Chat Room")
window.geometry(f"{window_width}x{window_height}")
window.configure(bg="Green")
if name_entered == False:
    information_text = "ENTER YOUR NAME"

message_frame = Frame(window, height=100, width=100, bg="white")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar_msg_frame = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=int(window_height/18), width=window_width, bg="white", yscrollcommand=scroll_bar_msg_frame.set)
scroll_bar_msg_frame.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

entry_field = Entry(window, textvariable=my_msg, fg="black", font=("Arial", 16, "bold"), width=100)
entry_field.pack()

information = Label(window, text=information_text, font=("Arial", 10, "bold"))
information.pack()

send_button = Button(window, text="Send", font="Arial", fg="Black", bg="blue", command=send)
send_button.pack()

#############################################################################################################################

host = "192.168.178.27"
port = 27

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except Exception as ex:
    error.server_not_online(ex)
    exit()

receive_thread = Thread(target=receive)
receive_thread.start()

mainloop()