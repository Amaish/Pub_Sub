from flask import render_template, flash, redirect
from app import app
from app.forms import Subscribe_form, Publish_form


@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')

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
    
    form = Publish_form()
    if form.validate_on_submit():
        Input.append(form.Input.data)
        return redirect('/Publish')
    return render_template('Publish.html', title='Publish',load=Input,topic=my_topic, form=form)