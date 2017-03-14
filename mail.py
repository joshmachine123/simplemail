
import smtplib
subject=raw_input("Subject: ")
msg=raw_input("enter message: ")
message='Subject: %s\n\n%s'%(subject,msg)
targetmail=raw_input("enter target email: ").split(' ')
email='your_emailID'
password='your_pasword'
server=smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(email,password)
server.sendmail(email,targetmail,message)
