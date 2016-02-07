# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
def sendText(number, msg):
	account_sid = "AC5c6407f246844d85810bb4ae7d116d4b"
	auth_token = "f36e1f3e95c3121b85c9d823789a641c"
	client = TwilioRestClient(account_sid, auth_token)


	 
	message = client.messages.create(to=number, from_="+12027509121",
	                                     body=msg)