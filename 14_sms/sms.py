from twilio.rest import Client

account_sid = '[account sid'
auth_token = '[auth token]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+twillionumber',
    body='I am inside the house',
    to='+outgoing number'
)

print(message.sid)
