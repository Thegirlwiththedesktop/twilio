import os
from twilio.rest import Client
import random
import schedule

#Automating messages with python + twilio

#First, create an array of messages to send

messages = ["hey man", "hello, hi", "goodmorning dude", "oh btw, not a robot","heyyyy hahaha","what's poppin'","what's good man?","hey remember to be zen today"]


#using Twilio API to send the texts

from twilio.rest import Client

def send_text(text):
    acc_sid = #add accout sid
    token = #add token
    client = Client(acc_sid,token)

    client.messages.create(to = "add phone number to text", from_ = "add twilio phone num", body = text)


#Use schedule library to schedule time

text = messages[random.randint(0, len(messages))]
schedule.every().day.at("05:30").do(send_text,messages[0])



