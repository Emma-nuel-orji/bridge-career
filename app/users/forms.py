from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, length, equal_to
from app.models import User


class RegistrationForm(FlaskForm):
    branch = SelectField('Visa Type', validators=[DataRequired()], choices=[(" "), ("Tourist Visa"), ("Business Visa"), ("Work Visa"), ("Transit Visa"), ("Student Visa")])
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    resume = FileField('Upload Your Resume', validators=[FileAllowed(['jpg', 'png', 'pdf'])])
    phone = StringField('Primary Phone Number', validators=[DataRequired(), Length(min=2, max=11)])
    security = StringField(' Social Security Last 4', validators=[DataRequired(), Length(min=2, max=4)])
    position = SelectField('What kind of work are you applying for?', validators=[DataRequired()], choices=[(""), ("All"), ("Clerical"), ("Industrial"), ("Legal"), ("Medical"), ("Technical")])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('GET STARTED')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username already exist please choose a different one!')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email already exist please choose a different one!')


class IndextForm(FlaskForm):
    question = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    question1 = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    question2 = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    question3 = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    question4 = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    question5 = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    question6 = RadioField('', validators=[DataRequired()], choices=[('Yes'), ('No')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    number = StringField('Primary Phone', validators=[DataRequired()])
    addres = StringField('Address', validators=[DataRequired(), Length(min=2, max=500)])
    addres2 = StringField('Address(2)', validators=[DataRequired(), Length(min=2, max=500)])
    state = StringField('State', validators=[DataRequired(), Length(min=2, max=50)])
    city = StringField('City', validators=[DataRequired(), Length(min=2, max=20)])
    country = SelectField('Country', validators=[DataRequired()], choices=[("--Select One--"), ("Aaland Islands"), ("Afghanistan"), ("Albania"), ("Algeria"), ("American Samoa"), ("Andorra"), ("Angola "), ("Anguilla "), ("Antarctica "), ("Antigua and Barbuda "), ("Argentina "), ("Armenia "), ("Aruba "), ("Ascension Island (British) "), ("Australia "), ("Austria "), (" Azerbaijan"), ("Bahamas "), ("Bahrain "), ("Bangladesh "), ("Barbados "), (" Belarus"), (" Belgium"), ("Belize "), ("Benin "), ("Bermuda "), ("Bhutan "), ("Bolivia "), ("Bonaire, Sint Eustatius and Saba "), ("Bosnia and Herzegovina "), ("Botswana "), ("Bouvet Island "), ("Brasil "), ("British Indian Ocean Territory "), ("Brunei Darussalam "), ("Bulgaria "), ("Burkina Faso "), ("Burundi "), ("Cambodia "), ("Cameroon "), ("Canada "), ("Canary Islands "), ("Cape Verde "), ("Cayman Islands "), ("Central African Republic "), ("Chad "), ("Chile "), ("China "), ("Christmas Island "), ("Cocos (Keeling) Islands "), ("Colombia "), ("Comoros "), ("Congo "), ("Cook Islands "), ("Costa Rica "), ("Cote D'Ivoire "), ("Croatia "), ("Cuba"), ("Curacao "), ("Cyprus "), ("Czech Republic "), ("Democratic Republic of Congo "), ("Denmark "), ("Djibouti "), ("Dominica "), ("Dominican Republic "), ("East Timor "), ("Ecuador"), ("Egypt "), ("El Salvador "), ("Equatorial Guinea "), ("Eritrea "), ("Estonia "), ("Ethiopia "), ("Falkland Islands (Malvinas) "), ("Faroe Islands "), ("Fiji "), ("Finland "), ("France, Metropolitan "), ("French Guiana "), ("French Polynesia "), ("French Southern Territories "), ("FYROM "), ("Gabon "), ("Gambia "), ("Georgia "), ("Germany "), ("Ghana "), ("Gibraltar "), ("Greece "), ("Greenland "), ("Grenada "), ("Guadeloupe "), ("Guam "), ("Guatemala "), ("Guernsey "), ("Guinea "), ("Guinea-Bissau "), ("Guyana "), ("Haiti "), ("Heard and Mc Donald Islands "), ("Honduras "), ("Hong Kong "), ("Hungary "), ("Iceland "), ("India "), ("Indonesia "), ("Iran (Islamic Republic of) "), ("Iraq "), ("Ireland "), ("Isle of Man "), ("Israel "), ("Italy "), ("Jamaica "), ("Japan "), ("Jersey "), ("Jordan "), ("Kazakhstan "), ("Kenya "), ("Kiribati "), ("Korea, Republic of "), ("Kosovo, Republic of "), ("Kuwait "), ("Kyrgyzstan "), ("Lao People's Democratic Republic "), ("Latvia "), ("Lebanon "), ("Lesotho "), ("Liberia "), ("Libyan Arab Jamahiriya "), ("Liechtenstein "), ("Lithuania "), ("Luxembourg "), ("Macau "), ("Madagascar "), ("Malawi "), ("Malaysia "), ("Maldives "), ("Mali "), ("Malta "), ("Marshall Islands "), ("Martinique "), ("Mauritania "), ("Mauritius "), ("Mayotte "), ("Mexico "), ("Micronesia, Federated States of "), ("Moldova, Republic of "), ("Monaco "), ("Mongolia "), ("Montenegro "), ("Montserrat "), ("Morocco "), ("Mozambique "), ("Myanmar "), ("Namibia "), ("Nauru "), ("Nepal "), ("Netherlands "), ("Netherlands Antilles "), ("New Caledonia "), ("New Zealand "), ("Nicaragua "), ("Niger "), ("Nigeria "), ("Niue "), ("Norfolk Island"), ("North Korea "), ("Northern Mariana Islands "), ("Norway "), ("Oman "), ("Pakistan "), ("Palau "), ("Palestinian Territory, Occupied "), ("Panama "), ("Papua New Guinea "), ("Paraguay "), ("Peru "), ("Philippines "), ("Pitcairn "), ("Poland "), ("Portugal "), ("Puerto Rico "), ("Qatar "), ("Reunion "), ("Romania "), ("Russian Federation "), ("Rwanda"), ("Saint Kitts and Nevis "), ("Saint Lucia "), ("Saint Vincent and the Grenadines "), ("Samoa "), ("San Marino "), ("Sao Tome and Principe "), ("Saudi Arabia "), ("Senegal "), ("Serbia "), ("Seychelles "), ("Sierra Leone "), ("Singapore "), ("Slovak Republic "), ("Slovenia "), ("Solomon Islands "), ("Somalia "), ("South Africa "), ("South Georgia &amp; South Sandwich Islands "), ("South Sudan "), ("Spain "), ("Sri Lanka "), ("St. Barthelemy "), ("St. Helena "), ("St. Martin (French part) "), ("St. Pierre and Miquelon "), ("Sudan "), ("Suriname "), ("Svalbard and Jan Mayen Islands "), ("Swaziland "), ("Sweden "), ("Switzerland "), ("Syrian Arab Republic "), ("Taiwan "), ("Tajikistan "), ("Tanzania, United Republic of "), ("Thailand "), ("Togo "), ("Tokelau "), ("Tonga "), ("Trinidad and Tobago "), ("Tristan da Cunha "), ("Tunisia "), ("Turkey "), ("Turkmenistan "), ("Turks and Caicos Islands "), ("Tuvalu "), ("Uganda "), ("Ukraine "), ("United Arab Emirates "), ("United Kingdom "), ("United States "), ("United States Minor Outlying Islands "), ("Uruguay "), ("Uzbekistan "), ("Vanuatu "), ("Vatican City State (Holy See) "), ("Venezuela "), ("Viet Nam "), ("Virgin Islands (British) "), ("Virgin Islands (U.S.) "), ("Wallis and Futuna Islands "), ("Western Sahara "), ("Yemen "), ("Yemen "), ("Zambia "), ("Zimbabwe ")])
    interest = StringField('Country Of Interest', validators=[DataRequired(), Length(min=2, max=200)])
    city2 = StringField('State/City', validators=[DataRequired(), Length(min=2, max=200)])
    reason = TextAreaField('Reason For the Travel', validators=[DataRequired()])
    choice = SelectField('Choice of Accomodations', validators=[DataRequired()], choices=[("--Select One--"), ("One Bedroom"), ("Two Bedroom"), ("Three Bedroom"), ("More")])
    period = SelectField('Period of time', validators=[DataRequired()], choices=[("--Select One--"), ("Less Than 1 Month"), ("1 - 3 months"), ("3 - 6 months"), ("6 months and above ")])
    budget = SelectField('Your Budget', validators=[DataRequired()], choices=[("--Select One--"), ("Less Than $1000"), ("$1000 - $5000"), ("$5000 - $10,000"), ("$10,000 And Above ")])
    submit = SubmitField('Submit ')
    
                              
                                             
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username already exist please choose a different one!')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email already exist please choose a different one!')


class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(" There's no account with this email. Please register.")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), length(min=5, max=20)])
    confirm_password = PasswordField('confirm Password', validators=[DataRequired(), equal_to('password')])
    submit = SubmitField('Reset Password')
