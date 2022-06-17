import flask
from flask import request
import urllib.request
import urllib.parse

app = flask.Flask(__name__)
def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)

@app.route('/', methods = ['GET'])
def home():
    apikey = str(request.args['token'])
    numbers = str(request.args['mobile'])
    otpCode = str(request.args['otp'])
    clientName = str(request.args['Name'])
    try: 
        resp, code = sendSMS(apikey, numbers,'USMRTA', 'Dear '+clientName+', OTP is '+otpCode+' for Gate Pass, kindly enter it to confirm your gate pass. thank you! Managed By U SMART AI LAB.')
        return resp['status']
    except:
        return  "Hello World"