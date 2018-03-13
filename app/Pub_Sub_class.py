import paho.mqtt.client as paho
import os
import time
import random
import routes

def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to broker")
            global Connected                #Use global variable
            Connected = True                #Signal connection 
        else:
            print("Connection failed")

Payload=""
topic=""
def on_message(client, userdata, message):
    global topic, Payload
    topic= str(message.topic)
    Payload = str (message.payload)
    print Payload
    print topic

Connected = False

class Pub_Sub_Config:
    def  __init__(self, broker="sungura1-angani-ke-host.africastalking.com", topic_=None,port=10883, user=None, password=None, Client_=None):
        #global glob_user
        #global glob_password
        #global glob_topic_
        #global glob_Client_
        global client
        self.user=user
        self.password=password
        self.topic_=topic_
        self.Client_=Client_

        form = Index_form ()
        if form.validate_on_submit():
            if user is  None:
                user = form.user.data
                #glob_user=user
            if password is None:
                password = form.password.data
                #glob_password=password
            if topic_ is None:
                topic_=form.Topic.data
                #glob_topic_=topic_
            if Client_ is None:
                Client_=form.client.data
                if len(Client_)==0:
                    Client_=user+"-"+str(random.randrange(16,38))
                #glob_Client_=Client_
            print Client_
            client = paho.Client(Client_) 
            client.username_pw_set(user, password=password)    #set username and password
            client.on_connect= on_connect  #attach function to callback
            client.on_message= on_message
            client.connect(broker, port)
            client.loop_start()

class Publish_(Pub_Sub_Config):
    def pub_func(self,client,user,topic_):
        while Connected != True:    #Wait for connection
            time.sleep(0.1)
        try:
            while True:
                pub_data = form.Input.data
                client.publish(user+"/"+topic_,pub_data)#publish
                client.subscribe(user+"/"+topic_)
                print "this is the payload: "+Payload
                time.sleep(0.5)
                print "Press CTRL + C to exit at any time\n"
        except KeyboardInterrupt:
            print "\nexiting"
            client.disconnect() #disconnect
            client.loop_stop() #stop loop

class Subscribe_(Pub_Sub_Config):        
    def sub_func(self,client,user,topic_):  
        form = Publish_form()      
        while Connected != True:    #Wait for connection
            time.sleep(0.1)
        print "Subscribing to a topic:"
        client.subscribe(user+"/"+topic_)
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print "\nexiting"
            client.disconnect() #disconnect
            client.loop_stop() #stop loop        
# sub_app=Subscribe_()
# sub_app.sub_func(client,glob_user,glob_topic_)

    