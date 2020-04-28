import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ryan Raymonds Computer'
email['to'] = 'ryan@genuine-deals.com'
email['subject'] = 'You won 10,000,000 Dollars! Just Click here to claim!!'

email.set_content('I am a python master and I can send all kinds of emails!!!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email@gmail.com', '<password>')
    smtp.send_message(email)
    print('all good boss!')
