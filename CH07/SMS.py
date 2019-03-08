# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC78eca2e07075cf3176a2689b1d41db72'
auth_token = '267504d9b0f36b852616bd67715f09a2'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="大家好",
                     from_='+12544497934',
                     to='+886934050080'
                 )

print(message.sid)