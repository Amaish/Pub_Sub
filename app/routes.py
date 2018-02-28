from flask import render_template, flash, redirect
from app import app
from app.forms import Subscribe_form, Publish_form, Index_form
import time
import paho.mqtt.client as paho
import sys

import socket



def create_socket():
    global s
    global socket_message

    try:
            s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit();

    socket_message = "Socket created"
    print socket_message


message = ""
def on_connect(client, userdata, flags, rc):
        global message
        
        if rc == 0:
    
            message="Connected to broker"
            
            global Connected                #Use global variable
            Connected = True                #Signal connection 
    
        else:
    
            message = "Connection failed"
        
Payload=["test"]
my_topic = ""
def on_message(client, userdata, message):
    global Payload
    global my_topic
    topic = message.topic
    my_topic = topic
    print my_topic
    Payload.append(message.payload)


Client =""
user = ""
port = ""
password = ""
broker = ""
message = ""
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    create_socket()
    global broker
    global port
    global user
    global password
    global Client
    
    form = Index_form ()
    if form.validate_on_submit():
        broker = form.Broker.data
        port = int(form.port.data)
        user = form.user.data
        password = form.password.data
        Client = form.client.data
        client.username_pw_set(user, password=password)
        client.connect(broker, port)
        client.loop_start()      
        return redirect('/Subscribe')
    return render_template('index.html', title='Home', connect_message=message, socket_message=socket_message,form=form )

client = paho.Client(Client)
client.on_connect = on_connect
client.on_message = on_message


topic = ["Temperature","Weather","News","Sports"]
@app.route('/Subscribe', methods=['GET', 'POST'])
def Subscribe():
    form = Subscribe_form()
    global sub_topic
    
    if form.validate_on_submit():
        if form.Topic.data == "Temperature":
            client.subscribe("amaina/"+str(form.Topic.data))
            sub_topic = "amaina/"+str(form.Topic.data)
            
            return redirect('/Publish')
        if form.Topic.data == "Weather":
            client.subscribe("amaina/"+str(form.Topic.data))
            sub_topic = "amaina/"+str(form.Topic.data)
            
            return redirect('/Publish')
        if form.Topic.data == "News":
            client.subscribe("amaina/"+str(form.Topic.data))
            sub_topic = "amaina/"+str(form.Topic.data)
            
            return redirect('/Publish')
        if form.Topic.data == "Sports":
            client.subscribe("amaina/"+str(form.Topic.data))
            sub_topic = "amaina/"+str(form.Topic.data)
            
            return redirect('/Publish')
        flash('Invalid topic try again,'.format(form.Topic.data))
        return redirect('/Subscribe')
    return render_template('Subscribe.html', title='Subscribe',connect_message=message,topic=topic,form=form)




@app.route('/Publish', methods=['GET','POST'])
def Publish():        
    form = Publish_form()
    Input=["Welcome"]
    if form.validate_on_submit():
        Input.append(form.Input.data)
        Pub = form.Input.data
        client.publish(sub_topic,Pub)
        return redirect('/Publish')
    return render_template('Publish.html', title='Publish',load=Input,Payload=Payload,connect_message=message,my_topic=sub_topic, form=form)






"""import paho.mqtt.client as paho
import os
import time
import random


Connected=bool
Payload=""
topic=""
class Subscribe_:
    def  __init__(self, Client_="Anthony-"):
        self.Client_=Client_
           
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            global Connected                #Use global variable
            Connected = True                #Signal connection 
        else:
            print("Connection failed")


    def on_message(self, client, userdata, message):
        global topic, Payload
        topic= str(message.topic)
        Payload = str (message.payload)
        print Payload
        print topic


    def sub_func(self, broker="sungura1-angani-ke-host.africastalking.com", topic_=None,port=10883, user=None, password=None, Client_=None):        
        if user is  None:
            print "Please provide a user"
            user = raw_input("Enter User:\n")
        if password is None:
            print "Please enter a password"
            password = raw_input("Enter Password:\n")
        if topic_ is None:
            topic_=raw_input("Enter a topic:\n")
        if Client_ is None:
            Client_=raw_input("Enter a client name:\n")
            if len(Client_)==0:
                Client_=user+"-"+str(random.randrange(16,38))
        print Client_
        client = paho.Client(Client_) 
        client.username_pw_set(user, password=password)    #set username and password
        client.on_connect= self.on_connect                     #attach function to callback
        client.on_message= self.on_message                      #attach function to callback
        client.connect(broker, port=port)          #connect to broker
        client.loop_start()        #start the loop
        while Connected != True:    #Wait for connection
            time.sleep(0.1)
        client.subscribe(user+"/"+topic_)
        print Payload
        print topic
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print ("exiting")
            client.disconnect()
            client.loop_stop()



    
    

class Publish_(Subscribe_):
    def pub_func(self,broker="sungura1-angani-ke-host.africastalking.com", topic_="Temperature",port=10883, user="amaina", password="TamaRind", Client_="Anthony-"):
        client = paho.Client(Client_)
        client.username_pw_set(user, password=password)    #set username and password
        client.on_connect= self.on_connect                     #attach function to callback
        client.on_message= self.on_message                      #attach function to callback
        client.connect(broker, port=port)          #connect to broker
        client.loop_start()        #start the loop
        while Connected != True:    #Wait for connection
            time.sleep(0.1)
        try:
            count = []
            while True:
                temp = random.randrange(16,38)
                if temp<=25:
                    count.append(temp)
                    print "press CTRL + C to exit\n"
                    time.sleep(1)    
                else:
                    client.publish(user+"/"+topic_,temp)#publish 
                    time.sleep(0.5)
                    print "Press CTRL + C to exit\n"
                while len(count) > 5:
                    os.system('clear')
                    count = []
                    break
        except KeyboardInterrupt:
            print "\nexiting"
            client.disconnect() #disconnect
            client.loop_stop() #stop loop

        
sub_app=Subscribe_()
sub_app.sub_func()

    """