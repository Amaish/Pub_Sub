from wtforms import SelectField, StringField, PasswordField, BooleanField, SubmitField, TextAreaField, TextField, DecimalField
from wtforms.validators import DataRequired, Required
from flask_wtf import FlaskForm
import paho.mqtt.client as paho
import random
import time



connect_message=""  
class on_connection:
    def __init__(self):
        self.connect_message=""

      
    def on_connect_func(self,client, userdata, flags, rc):
        if rc == 0:
            global Connected, connect_message
            connect_message="Connected to broker"
            Connected = True
            return connect_message                
        elif (1<=rc and rc<=5):
            connect_message="Connection failed"
            return connect_message
        else:
            connect_message="Waiting for connection"
            return connect_message
Payload=[]
topic=""        
class on_messaging:
    def __init__(self):
        self.Payload=[]
        self.topic=""             

    def on_message_func(self,client, userdata, message):
        global topic, Payload
        topic= str(message.topic)
        Payload.append(str (message.payload))
        print "my topic is " +topic
        

Connected = False

connection=on_connection()
class Pub_Sub_Config:
    def  __init__(self, broker="sungura1-angani-ke-host.africastalking.com",port=10883, user=None, password=None, Client_=None):
        self.broker=broker
        self.port=port
        self.user=user
        self.password=password
        self.Client_=Client_
        self.display_message=connect_message
        self.display_payload=Payload
        self.display_topic=topic
        client = paho.Client(Client_) 
        client.username_pw_set(user, password=password)    #set username and password
        client.on_connect= connection.on_connect_func#.on_connect_func  #attach function to callback
        client.on_message= on_messaging.on_message_func
        client.connect(broker,port)
        #client.loop_start()

class Index_form(FlaskForm):
    user = TextField('user', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    Client_ = TextField('client(e.g Anto)', validators=[DataRequired()])    
    submit = SubmitField('submit')       


class Subscribe_form(FlaskForm):
    topic = TextField('Topic', validators=[DataRequired()])
    submit = SubmitField('Subscribe')
    

class Publish_form(FlaskForm):
    Pub_data = TextField('Input', validators=[DataRequired()])
    submit = SubmitField('Publish')
    Unsubscribe = SubmitField('Unsubscribe')
    

"""The value of rc determines success or not:
        0: Connection successful
        1: Connection refused - incorrect protocol version
        2: Connection refused - invalid client identifier
        3: Connection refused - server unavailable
        4: Connection refused - bad username or password
        5: Connection refused - not authorised
        6-255: Currently unused.
"""
    