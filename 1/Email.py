import smtplib



class Email:
    """A class for email sending through gmails"""
    # To use this class, you must enable "less security connection" in gmail security setting

    def __init__(self, account, password):
        self.gmail_user = account
        self.gmail_password = password

    def send_email(self, sent_to, subject, body):
        try:
            email_text ="""From: %s  
To: %s  
Subject: %s

%s

""" % (self.gmail_user, ", ".join(sent_to), subject, body)

            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.ehlo()
            self.server.login(self.gmail_user, self.gmail_password)
            print (email_text)
            self.server.sendmail(self.gmail_user, sent_to, email_text)
            self.server.close()
            print 'Email sent!'
        except:
            print 'Something went wrong...'

