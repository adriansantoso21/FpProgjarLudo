import smtplib

def main(playerEmail, position):
   to = playerEmail
   sender = 'ludoboardgamefp@gmail.com'
   subject = 'Congratulations Message'
   password = 'xxx'

   text = "Congratulations, you have finished in " + \
          position + \
          " place. Don't forget to play with your frieds again. Hope you enjoy the game.\nBest Regard,\nLudo Board Game Team"

   message = """From: %s\nTo: %s\nSubject: %s\n\n%s
       """ % (sender, ", ".join(playerEmail), subject, text)
   try:
      server = smtplib.SMTP("smtp.gmail.com", 587)
      server.ehlo()
      server.starttls()
      server.login(sender, password)
      server.sendmail(sender, to, str(message))
      server.close()
      print("Successfull send email")

   except Exception as err:
         print(err)