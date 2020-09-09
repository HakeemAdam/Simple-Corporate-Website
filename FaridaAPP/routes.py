from flask import Flask, render_template, request, flash, redirect, url_for
from FaridaAPP import app, forms
from FaridaAPP.forms import ContactForm
from flask_mail import Message, Mail
import os

mail = Mail(app)

app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.googlemail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USE_TLS=False,
    MAIL_USERNAME='nkrumahbot@gmail.com',
    MAIL_PASSWORD='gvuunrxexqhgnwmi',
)

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            flash('You must enter something into all of the fields')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender='nkrumahbot@gmail.com', recipients=['Afriq360global@gmail.com'])
            msg.body = """
    			From: %s %s <%s>
    			%s
    			""" % (form.firstName.data, form.lastName.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html',
                               title='Contact Us',
                               form=form)
