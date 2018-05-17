import os
import mraa
import time
import math
from twilio.rest import Client

#D1
but = mraa.Gpio(23)
#D2
buz = mraa.Gpio(25)

buz.dir(mraa.DIR_OUT)
but.dir(mraa.DIR_IN)

time.sleep(3)

while True:         
    print "Aguardando pressionar botao"
    
    while but.read()==1:
        buz.write(0)
        time.sleep(0.75)
                                
    while but.read()==0:
        buz.write(1)  
        #sms begin
        account_sid = "<twilio_sid>"
        auth_token = "<twilio_token>"
        client = Client(account_sid, auth_token)
        client.messages.create(to="<destination_phone>",
                       from_="<your_phone>",
                       body="<sms_body>")
        print "SMS enviado"
        #sms end   
        time.sleep(0.0001)


