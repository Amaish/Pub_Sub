from flask import render_template, flash, redirect
from app import app
from app.forms import Subscribe_form, Publish_form
import time
import paho.mqtt.client as paho
from random import randint


broker="sungura1-angani-ke-host.africastalking.com"
port = 10883                         #Broker port
user = "amaina"                    #Connection username
password = "TamaRind"            #Connection password

def on_connect(client, userdata, flags, rc):
        global message
        
        if rc == 0:
    
            message="Connected to broker"
            
            global Connected                #Use global variable
            Connected = True                #Signal connection 
    
        else:
    
            message = "Connection failed"
        
Payload=[]
def on_message(client, userdata, message):
    global Payload
    Payload.append(message.payload)
    


message = ""
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    
    
    return render_template('index.html', title='Home', message=message )

client= paho.Client("Anthony-001"+str(randint(10,1000))) #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
client.username_pw_set(user, password=password)    #set username and password
client.connect(broker, port)#connect
client.loop_start() #start loop to process received messages
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
    sub_topic = "amaina/"+my_topic
    form = Publish_form()
    if form.validate_on_submit():
        Input.append(form.Input.data)
        client.publish(sub_topic,form.Input.data)
        client.subscribe(sub_topic)
        return redirect('/Publish')
    return render_template('Publish.html', title='Publish',load=Input,sub_value=Payload,topic=my_topic, form=form)
