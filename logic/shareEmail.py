import smtplib

def main(playerEmail, position):
   to = playerEmail
   sender = 'ludoprogjar@yahoo.com'
   password = 'ixfmtzqzsbbhcpeu'

   message = "Congratulations, you have finished in " + position + " place. Hope you enjoy the game :)"

   try:
      server = smtplib.SMTP_SSL("smtp.mail.yahoo.com", 465)
      # server.connect("smtp.mail.yahoo.com", 465)
      # server.ehlo()
      # server.starttls()
      server.ehlo()
      server.login(sender, password)
      server.sendmail(sender, to, str(message))
      server.quit()

   except Exception as err:
         print(err)