# coding: utf-8
from twilio import rest
# from twilio.rest import TwilioRestClient

account_sid = "AC197b60bfafd68ad731691101bead8ecb"
auth_token = "40325afc3c9a7ec235f9c57122e9a138"
client = rest.TwilioRestClient(account_sid, auth_token)
#client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(body="HI.中午好",
                                     to="+8618017313933",
                                     from_="+17088132510")

print message.sid
