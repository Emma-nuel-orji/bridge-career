import secrets
# from app.models import Product, Checkout, Payment
from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session
from app import db, mail
from app.users.forms import IndextForm
from app.models import User
from flask_login import current_user, login_required
from flask_mail import Message
from app.users.utils import save_picture

main = Blueprint('main', __name__)




@main.route('/home', methods=['GET', 'POST'])
def home():
    user = User
    form_data = request.form
    form = IndextForm()
    if form.validate_on_submit():
        msg = Message(f'New Message from {form.email.data}', sender=f'{user.email}',
                      recipients=['info@bridge-careers.com'])
        msg.body = f"""
           Are you able to provide information that establishes your identity and eligibility to work in the US? :  {form.question.data}
           Are you willing to submit to a drug test according to our policy? :  {form.question1.data} 
           Are you willingto release your background information including your criminal record? :  {form.question2.data}
           Have you been convicted of a Felony in any state within the past 7 years? :  {form.question3.data}
           Are you able to perform the essential funtions of the job for which you have applied with or without reasonable accommodation? :  {form.question4.data}
           Are you at least 18 years of age or older? :  {form.question5.data}
           Have you ever worked for us before? :  {form.question6.data}
           Email :  {form.email.data}
           Primary Phone :  {form.number.data}
           Address :  {form.addres.data}
           Address(2) :  {form.addres2.data}
           State :  {form.state.data}
           City :  {form.city.data}
           Country :  {form.country.data}
           Country Of Interest :  {form.interest.data}
           Reason For the Travel :  {form.reason.data}
           Choice of Accomodations:  {form.choice.data}
           Period of time :  {form.period.data}
           Budget :  {form.budget.data}
           """
        mail.send(msg)
        flash('your message have been sent', 'success')
        return redirect(url_for('main.thanks'))
    return render_template("home.html", title='contact Form', form=form, form_data=form_data)


@main.route('/thanks')
# @login_required
def thanks():
    return render_template('thanks.html')

