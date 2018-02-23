from flask import render_template, flash, redirect
from app import app
from app.forms import Subscribe_form, Publish_form, Index_form
import time
import paho.mqtt.client as paho
from random import randint

from celery import Celery


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
def on_message(client, userdata, message):
    global Payload
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
    return render_template('index.html', title='Home', connect_message=message, form=form )

client= paho.Client(Client)
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
            client.subscribe("amaina/"+my_topic)
            return redirect('/Publish')
        if form.Topic.data == "Weather":
            value = 1
            my_topic = topic[value]
            client.subscribe("amaina/"+my_topic)
            return redirect('/Publish')
        if form.Topic.data == "News":
            value = 2
            my_topic = topic[value]
            client.subscribe("amaina/"+my_topic)
            return redirect('/Publish')
        if form.Topic.data == "Sports":
            value = 3
            my_topic = topic[value]
            client.subscribe("amaina/"+my_topic)
            return redirect('/Publish')
        flash('Invalid topic try again,'.format(form.Topic.data))
        return redirect('/Subscribe')
    return render_template('Subscribe.html', title='Subscribe',connect_message=message,topic=topic,form=form)


#client.connect(broker, port)
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
        return redirect('/Publish')
    return render_template('Publish.html', title='Publish',load=Input,Payload=Payload,connect_message=message,topic=my_topic, form=form)

