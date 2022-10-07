#===========================================================
# Important Liberies 
#===========================================================
import sys
import os
import csv
import smtplib
from cgitb import html
from email import message
from random import randint, choices
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#===========================================================
# Checking All Files and Collecting Resources form files..
#===========================================================
# FILE [A] Checking & Reading (SMTP.CSV) File.
with open("smtp.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for username, passwrd in reader:
            smtp_username = username
            smtp_password = passwrd
#===========================================================
# FILE [B] Checking & Reading (CONTACT.CSV) File.
with open("contact.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for name, email in reader:
            client_name = name
            client_email = email
#===========================================================
# FILE [C] Checking & Reading (Subject.csv) File.
with open("subject.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for subjects in reader:
            subject_lines = subjects
#===========================================================
# Calculation how many email has been sent (Logic (A))
#===========================================================
totalSend = 1
if(len(sys.argv) > 1):
    totalSend = int(sys.argv[1])
#===========================================================
# All Files Reading & Checking End Here...
#==================================================================================================
# Here is the logic of program start.
# Basically here we definig the work of python script.
#==================================================================================================
def send_mail(recipient, name_to_display, from_email, password, body, subj):
    msg = MIMEMultipart()
    msg.attach(MIMEText(body, 'plain'))
    msg['Subject'] = subj
    msg['From'] = f'{name_to_display} <{from_email}>'
    msg['To'] = recipient
    #==================================================================================================
    # Main Def Logic Brack
    #==================================================================================================
    # Mail Program of Email Sending 
    #==========================================================================================
    with open("smtp-settings.csv") as file:
        reader = csv.reader(file)
        next(reader)
        for domain, port in reader:
            mailserver = smtplib.SMTP(domain, port)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login(from_email, password)
            mailserver.sendmail(from_email, email, msg.as_string())
            mailserver.quit()
    #==========================================================================================
    # How many email sent and from which by using and total of email sent
        print(f"send to {email} by {from_email} successfully : {totalSend}")
    #==================================================================================================
