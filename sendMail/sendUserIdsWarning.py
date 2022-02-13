import smtplib
  
s = smtplib.SMTP('smtp.gmail.com', 587)
  
s.starttls()
senderMail=input("Enter your e-mail id: ")
senderPass=input("Enter your password: ")
s.login(senderMail, senderPass)
  
message = "Dear customer, your account credentials have been leaked. Kindly change your login details."

usernames=open("dataFiles\\userNames.txt","r")
for mails in usernames:
    try:
        s.sendmail(senderMail, mails, message)
    except:
        pass

s.quit()