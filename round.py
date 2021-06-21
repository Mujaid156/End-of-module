from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from playsound import playsound


mail = Tk()
mail.title("Sending Emails")
mail.geometry("500x500")

# Creating Labels
name = Label(mail, text="Please enter email: ")
passwod = Label(mail, text="Please enter password: ")

# Placing Labels
name.pack()
passwod.pack()

# Creating Entries
user = Entry(mail)
word = Entry(mail)

# Placing Entries
user.pack()
word.pack()

# Creating Buttons



def sending():
    playsound('hide_a_body.mp3')
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email_id = 'mujaid.kariem22@gmail.com'
    receiver_email_id = user.get()
    password = word.get()
    subject = "Greetings"
    msg = MIMEMultipart()
    msg['From'] = sender_email_id
    msg['To'] = receiver_email_id
    msg['Subject'] = subject
    body = "Hi, how are you doing today\n"
    body = body + "What are you doing this weekend"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()

    s.starttls()
    s.login(sender_email_id, password)

    s.sendmail(sender_email_id, receiver_email_id, text)
    s.quit()

send = Button(mail, text="Send", command=sending)
send.pack()

mail.mainloop()
