from flask import render_template, flash, redirect
from app import app
from app.forms import Subscribe_form, Publish_form, Index_form, Pub_Sub_Config, on_connection, on_messaging
import time
import paho.mqtt.client as paho
import sys  



password = ""
user = ""
Client_=""
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index(): 
    global Client_, user, password
    form = Index_form ()
    if form.validate_on_submit():
        user = form.user.data
        password = form.password.data
        Client_ = form.Client_.data
        client.username_pw_set(user, password=password)
        config_app=Pub_Sub_Config(user=user,password=password,Client_=Client_)
        client.connect(config_app.broker, config_app.port)
        client.loop_start()
        return redirect('/Subscribe')
    return render_template('index.html', title='Home',form=form )

my_connection=on_connection()
my_message=on_messaging()
client = paho.Client(Client_)
client.on_connect=my_connection.on_connect_func
client.on_message=my_message.on_message_func


topic_=""
sub_topic=""
topic = ["Temperature","Weather","News","Sports"] 
@app.route('/Subscribe', methods=['GET', 'POST'])
def Subscribe():
    form = Subscribe_form()
    global sub_topic
    global topic_
    config_app=Pub_Sub_Config(user=user,password=password,Client_=Client_)
    connect_message=config_app.display_message
    if form.validate_on_submit():
        print"from subscribe "+ connect_message
        topic_=form.topic.data
        if topic.count(topic_)==1:
            sub_topic=user+"/"+topic_
            client.subscribe(sub_topic)
            print "we are ready"
            return redirect('/Publish')
        else:
            warning_ = "Invalid topic try again,"
            flash(warning_.format(form.topic.data))
            return redirect('/Subscribe')
    return render_template('Subscribe.html', title='Subscribe',topic=topic,connect_message=connect_message,form=form)

payload_vals = []
Input=["Welcome"]
pub_data = ""
@app.route('/Publish', methods=['GET','POST'])

def Publish():  
    global pub_data
    config_app=Pub_Sub_Config(user=user,password=password,Client_=Client_)
    connect_message=config_app.display_message
    Payload=payload_vals
    form = Publish_form()
    if form.validate_on_submit():
        print "From Publish " + connect_message
        Input.append(str(form.Pub_data.data))
        pub_data=form.Pub_data.data
        client.publish(sub_topic,pub_data)
        print Input
        print pub_data
        print sub_topic
        payload_app=Pub_Sub_Config(user=user,password=password,Client_=Client_)
        payload_vals.append(payload_app.display_payload)
        print payload_vals
        print "my topic = "+ payload_app.display_topic
        return redirect('/Publish')
    return render_template('Publish.html', title='Publish',Input=Input,my_topic=sub_topic,connect_message=connect_message,Payload=Payload,form=form)

