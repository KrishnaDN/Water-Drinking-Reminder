
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 11:26:01 2020

@author: krishna
"""


from twilio.rest import Client
twilio_config='/home/krishna/Krishna/Jarvis/findmyphone/app/configs/twilio_cred.yaml'
from datetime import datetime

def make_call(twilio_config):
    from ruamel.yaml import YAML
    yml = YAML(typ="safe")
    with open(twilio_config) as f:
        keys = yml.load(f)
    client = Client(keys['acount_sid'], keys['auth_token'])
    call = client.calls.create(to='+919110******', from_=keys['ph_number'], url='https://demo.twilio.com/docs/voice.xml')
    print(call.sid)
    
    
def send_water_msg(twilio_config):
    from twilio.rest import Client
    from ruamel.yaml import YAML
    yml = YAML(typ="safe")
    with open(twilio_config) as f:
        keys = yml.load(f)
    
    from_whatsapp='' ##### put your twillio number here
    to_whatsapp='' #### put your phone number
    client = Client(keys['acount_sid'], keys['auth_token'])
    client.messages.create(body="It's Time to Drink Water Buddy!", from_=from_whatsapp, to=to_whatsapp,media_url=['https://admin.water-plus.co.uk/getattachment/fresh-thinking-hub/why-we-should-drink-water-at-work/Page-Content/dry-january_2.jpg.aspx?width=400&height=285'], )
    return None


if __name__=='__main__':
    watter_drinking_time = ['09:00:00','11:00:00','13:00:00','15:00:00','17:00:00','19:00:00','21:00:00']
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time in watter_drinking_time:
            send_water_msg(twilio_config)
        
            
