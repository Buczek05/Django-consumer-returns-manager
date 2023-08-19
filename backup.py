from fileinput import filename
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import os
import glob
import shutil
import time

time.sleep(10)


def get_newest():
    folder_path = r"C:\backup"
    file_type = r"\*dump"
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)
    return max_file


pendrive_path = r"D:\backup"

file_path = get_newest()
file_end = file_path.split(".")[-1]
file_name = os.path.basename(file_path)
port = 465
smtp_serwer = "*******"
sender_email = "*****"
password = "*******"
receiver_email = "*******"

print(file_path)
print(file_end)
print(file_name)


# create message object
message = MIMEMultipart()

# add in header
message["From"] = Header(sender_email)
message["To"] = Header(receiver_email)
message["Subject"] = Header("Zwroty BACKUP")

# attach message body as MIMEText
message.attach(MIMEText("", "plain", "utf-8"))

_f = open(file_path, "rb")
att = MIMEApplication(_f.read(), _subtype=file_end)
_f.close()
att.add_header("Content-Disposition", "attachment", filename=file_name)
message.attach(att)

ssl_pol = ssl.create_default_context()
print("with")
with smtplib.SMTP_SSL(smtp_serwer, port, context=ssl_pol) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, sender_email, message.as_string())
    server.quit()

shutil.copy(file_path, os.path.join(pendrive_path, file_name))
