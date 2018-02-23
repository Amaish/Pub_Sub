from flask import render_template, flash, redirect
from app import app
from app.forms import Subscribe_form, Publish_form, Index_form
import time
import paho.mqtt.client as paho
from random import randint
import socket
from celery import Celery


ran = ""
def create_socket():
    global s
    global socket_message
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socket_message = "Socket created"
    print socket_message


Client =""
user = ""
port = ""
password = ""
broker = ""
socket_message = ""
message = ""
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    global broker
    global port
    global user
    global password
    global Client
    ran = str(randint(10,1000))
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
    print message
    return render_template('index.html', title='Home', message=message, socket_message=socket_message, form=form )







# client = Client

# broker="sungura1-angani-ke-host.africastalking.com"
# port = 10883                         #Broker port
# user = "amaina"                    #Connection username
# password = "TamaRind"            #Connection password
# client= paho.Client("Anthony-001"+ran) #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
# client.username_pw_set(user, password=password)    #set username and password
# client.connect(broker, port)#connect
#client.loop_start() #start loop to process received messages
client= paho.Client(Client)
def on_connect(client, userdata, flags, rc):
        global message
        
        if rc == 0:
    
            message="Connected to broker"
            
            global Connected                #Use global variable
            Connected = True                #Signal connection 
    
        else:
    
            message = "Connection failed"
        
Payload=["test"]
def on_message(client, userdata, message):
    global Payload
    Payload.append(message.payload)
    

#client= paho.Client("Anthony-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
# client.username_pw_set(user, password=password)    #set username and password
# client.connect(broker, port)#connect
create_socket()


#client.loop_start() #start loop to process received messages
# client.on_connect= on_connect
# client.on_message= on_message
client.on_connect= on_connect
client.on_message= on_message

my_topic=""
topic = ["Temperature","Weather","News","Sports"]
@app.route('/Subscribe', methods=['GET', 'POST'])
def Subscribe():
    global my_topic
    form = Subscribe_form()
    if form.validate_on_submit():
        if form.Topic.data == "Temperature":
            value = 0
            my_topic = topic[value]
            return redirect('/Publish')
        if form.Topic.data == "Weather":
            value = 1
            my_topic = topic[value]
            return redirect('/Publish')
        if form.Topic.data == "News":
            value = 2
            my_topic = topic[value]
            return redirect('/Publish')
        if form.Topic.data == "Sports":
            value = 3
            my_topic = topic[value]
            return redirect('/Publish')
        flash('Invalid topic try again,'.format(form.Topic.data))
        return redirect('/Subscribe')
    return render_template('Subscribe.html', title='Subscribe',topic=topic,form=form)

Input=["Welcome"]
@app.route('/Publish', methods=['GET','POST'])
def Publish():
    global Pub 
    global sub_topic
    sub_topic = "amaina/"+my_topic
    form = Publish_form()
    if form.validate_on_submit():
        Input.append(form.Input.data)
        Pub = form.Input.data
        client.publish(sub_topic,Pub)
        print Pub
        client.subscribe(sub_topic)
        return redirect('/Publish')
    return render_template('Publish.html', title='Publish',load=Input,Payload=Payload,topic=my_topic, form=form)

