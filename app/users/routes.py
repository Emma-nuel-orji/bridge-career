from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, session
from app import db, bcrypt, mail, app
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required
from app.users.utils import save_picture, send_password_reset_email
from app.users.forms import LoginForm, RegistrationForm, UpdateAccountForm, ResetPasswordForm, RequestResetForm
from flask_mail import Message, Attachment
from flask_mail import Message
from flask import flash, redirect, render_template, url_for
import os
from werkzeug.utils import secure_filename
from flask import request
from flask import current_app


users = Blueprint('users', __name__)




@users.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        resume = form.resume.data
        resume_filename = secure_filename(resume.filename)
        resume_path = os.path.join(current_app.root_path, 'static/images', resume_filename)
        resume.save(resume_path)

        directory = os.path.join(current_app.root_path, 'static', 'images')
        os.makedirs(directory, exist_ok=True)
        
        resume_filename = ''
        resume_path = ''  # Initialize resume_path variable
        
        if 'resume' in request.files:
            resume = request.files['resume']
            if resume.filename != '':
                resume_filename = secure_filename(resume.filename)
                resume_path = os.path.join(directory, resume_filename)
                resume.save(resume_path)
    
        # Create the email message
        msg = Message(f'New Message from {form.username.data}', sender=form.email.data, recipients=['info@bridge-careers.com'])
        msg.body = f"""
           {form.username.data} Just Created A New Account. Below Are His/Her Credentials:
           
           Branch:  {form.branch.data}
           First Name:  {form.firstname.data}
           Last Name:  {form.lastname.data}
           Email:  {form.email.data}
           Phone:  {form.phone.data}
           Primary Phone Number:  {form.security.data}
           Position: {form.position.data}
           Username:  {form.username.data}
           Password:  {form.password.data}
           """
        
        # Attach the uploaded PDF file to the email
        if resume_path:
               with open(resume_path, 'rb') as pdf_file:
                  msg.attach(resume_filename, 'application/pdf', pdf_file.read())

                # attachment = Attachment(resume_filename, 'application/pdf', pdf_file.read())
                # msg.attach(attachment)


        # Send the email
        mail.send(msg)

        flash(f'Welcome {form.username.data}! Your account has been created successfully. Please kindly fill the forms below.', 'success')
        return redirect(url_for('main.home'))
    
    return render_template("register.html", title='Register', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash('You have logged in successfully.', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('login unsuccessful.please check your Email and password', 'danger')
    return render_template('login.html', form=form)


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='img/' + current_user.image_file)
    return render_template("account.html", image_file=image_file, form=form)


@users.route("/delete_user/<int:user_id>/delete", methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if current_user.id != 2:
        abort(403)
    db.session.delete(user)
    db.session.commit()
    flash("the user has been deleted successfully", 'success')
    return redirect(url_for('admin.home'))
    return render_template("admin/users.html", user=user)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@users.route('/reset_password', methods=['POST', 'GET'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route('/reset_password-<token>', methods=['POST', 'GET'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if not user:
        flash('Invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('your password has been updated!.', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)
