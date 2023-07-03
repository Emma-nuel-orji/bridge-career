import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, session
from app import app, db, bcrypt, Message, mail, mail_username
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, BlogForm, GalleryForm, ProductForm, \
    RecommendationForm
from app.models import User, Blog, Gallery, Product, Recommendation
from flask_login import login_user, current_user, logout_user, login_required


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     product = Product.query.all()
#     recom = Recommendation.query.all()
#     posts = Blog.query.all()
#     return render_template("index.html", product=product, recom=recom, posts=posts)
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, phone=form.phone.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Welcome {form.username.data} Your account has been created! You are now able to log in', 'success')
#         return redirect(url_for('login'))
#     return render_template("register.html", title='Register', form=form)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             next_page = request.args.get('next')
#             flash('You have logged in successfully.', 'success')
#             return redirect(next_page) if next_page else redirect(url_for('index'))
#         else:
#             flash('login unsuccessful.please check your Email and password', 'danger')
#     return render_template('login.html', form=form)
#
#
# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/img', picture_fn)
#
#     output_size = (1000, 1000)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)
#
#     return picture_fn
#
#
# @app.route('/account', methods=['GET', 'POST'])
# @login_required
# def account():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         if form.picture.data:
#             picture_file = save_picture(form.picture.data)
#             current_user.image_file = picture_file
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.commit()
#         flash('Your account has been updated!', 'success')
#         return redirect(url_for('account'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     image_file = url_for('static', filename='img/' + current_user.image_file)
#     return render_template("account.html", image_file=image_file, form=form)
#
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


# @app.route('/catalog', methods=['GET', 'POST'])
# @login_required
# def catalog():
#     recommendation = Recommendation.query.all()
#     return render_template("catalog.html", recommendation=recommendation)


# @app.route('/product', methods=['GET', 'POST'])
# @login_required
# def product():
#     product = Product.query.all()
#     return render_template("product.html", product=product)


# @app.route('/blog', methods=['GET', 'POST'])
# @login_required
# def blog():
#     posts = Blog.query.all()
#     return render_template("blog.html", posts=posts)
#
#
# @app.route('/gallery', methods=['GET', 'POST'])
# @login_required
# def gallery():
#     gallery = Gallery.query.all()
#     return render_template("gallery.html", gallery=gallery)


# @app.route('/cart', methods=['GET', 'POST'])
# @login_required
# def cart():
#     if 'shoppingcart' not in session:
#         return redirect(request.referrer)
#     return render_template("cart.html")


# @app.route('/checkout', methods=['GET', 'POST'])
# @login_required
# def checkout():
#     return render_template("checkout.html")
#
#
# @app.route('/faq', methods=['GET', 'POST'])
# @login_required
# def faq():
#     return render_template("faq.html")
#
#
# @app.route('/contact', methods=['GET', 'POST'])
# @login_required
# def contact():
#     return render_template("contact.html")


# @app.route('/single_product', methods=['GET', 'POST'])
# def single_product():
#     product = Product.query.all()
#     recom = Recommendation.query.all()
#     return render_template('single_product.html', product=product, recom=recom)


# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     users = User.query.all()
#     gallery = Gallery.query.all()
#     product = Product.query.all()
#     recom = Recommendation.query.all()
#     if current_user.id != 2:
#         flash('Please you cant access to this page', 'danger')
#         return redirect(url_for('index', users=users, gallery=gallery, product=product, recom=recom))
#     else:
#         render_template('admin/home.html', users=users, gallery=gallery, product=product, recom=recom)
#     return render_template("admin/home.html", users=users, gallery=gallery, product=product,
#                            recom=recom)

#
# @app.route('/blogpost', methods=['GET', 'POST'])
# def blogpost():
#     global image_file
#     form = BlogForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             picture_file = save_picture(form.image.data)
#             image = picture_file
#         title = form.title.data
#         content = form.content.data
#         author = current_user
#         post = Blog(title=title, content=content, author=author, image=image)
#         db.session.add(post)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('home'))
#     elif request.method == 'GET':
#         image_file = url_for('static', filename='img/' + Blog.image)
#         image_file = url_for('static', filename='img/' + current_user.image_file)
#     return render_template('admin/blogpost.html', form=form, image_file=image_file)

#
# @app.route('/image', methods=['GET', 'POST'])
# @login_required
# def image():
#     global image_file
#     form = GalleryForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             picture_file = save_picture(form.image.data)
#             image = picture_file
#         title = form.title.data
#         content = form.content.data
#         author = current_user
#         gallery = Gallery(title=title, content=content, author=author, image=image)
#         db.session.add(gallery)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('home'))
#     elif request.method == 'GET':
#         image_file = url_for('static', filename='img/' + Blog.image)
#         image_file = url_for('static', filename='img/' + current_user.image_file)
#     return render_template('admin/image.html', form=form, image_file=image_file)


# @app.route('/productpost', methods=['GET', 'POST'])
# @login_required
# def productpost():
#     global image_file
#     form = ProductForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             picture_file = save_picture(form.image.data)
#             image = picture_file
#         name = form.name.data
#         price = form.price.data
#         discount = form.discount.data
#         category = form.category.data
#         desc = form.desc.data
#         author = current_user
#         product = Product(name=name, price=price, discount=discount, category=category, desc=desc, author=author,
#                           image=image)
#         db.session.add(product)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('home'))
#     elif request.method == 'GET':
#         image_file = url_for('static', filename='img/' + Blog.image)
#         image_file = url_for('static', filename='img/' + current_user.image_file)
#     return render_template('admin/productpost.html', form=form, image_file=image_file)
#
#
# @app.route("/productpost/<int:product_id>", methods=['GET', 'POST'])
# def products(product_id):
#     products = Product.query.get_or_404(product_id)
#     return render_template("single_product.html", products=products)
#
#
# @app.route('/recom', methods=['GET', 'POST'])
# def recom():
#     global image_file
#     form = RecommendationForm()
#     if form.validate_on_submit():
#         if form.image.data:
#             picture_file = save_picture(form.image.data)
#             image = picture_file
#         name = form.name.data
#         price = form.price.data
#         discount = form.discount.data
#         category = form.category.data
#         desc = form.desc.data
#         author = current_user
#         recom = Recommendation(name=name, price=price, discount=discount, category=category, desc=desc,
#                                         author=author,
#                                         image=image)
#         db.session.add(recom)
#         db.session.commit()
#         flash('Your post has been created!', 'success')
#         return redirect(url_for('home'))
#     elif request.method == 'GET':
#         image_file = url_for('static', filename='img/' + Blog.image)
#         image_file = url_for('static', filename='img/' + current_user.image_file)
#     return render_template('admin/recom.html', form=form, image_file=image_file)
#
#
# @app.route("/recom/<int:recommendation_id>", methods=['GET', 'POST'])
# def recommendations(recommendation_id):
#     recom = Recommendation.query.get_or_404(recommendation_id)
#     return render_template("single_rec.html", recom=recom)
#
#
# @app.route("/delete_user/<int:user_id>/delete", methods=['GET', 'POST'])
# def delete_user(user_id):
#     user = User.query.get_or_404(user_id)
#     if current_user.id != 2:
#         abort(403)
#     db.session.delete(user)
#     db.session.commit()
#     flash("the user has been deleted successfully", 'success')
#     return redirect(url_for('home'))
#     return render_template("Admin/home.html", user=user)
#
#
# @app.route("/delete_prod/<int:prod_id>/delete", methods=['GET', 'POST'])
# def delete_prod(prod_id):
#     products = Product.query.get_or_404(prod_id)
#     if current_user.id != 2:
#         abort(403)
#     db.session.delete(products)
#     db.session.commit()
#     flash("the product has been deleted successfully", 'success')
#     return redirect(url_for('home'))
#     return render_template("Admin/home.html", products=products)
#
#
# @app.route("/delete_rec/<int:rec_id>/delete", methods=['GET', 'POST'])
# def delete_rec(rec_id):
#     recom = Recommendation.query.get_or_404(rec_id)
#     if current_user.id != 2:
#         abort(403)
#     db.session.delete(recom)
#     db.session.commit()
#     flash("the recommended product has been deleted successfully", 'success')
#     return redirect(url_for('home'))
#     return render_template("Admin/home.html", recom=recom)

#
# def MagerDicts(dict1, dict2):
#     if isinstance(dict1, list) and isinstance(dict2, list):
#         return dict1 + dict2
#     elif isinstance(dict1, dict) and isinstance(dict2, dict):
#         return dict(list(dict1.items()) + list(dict2.items()))
#     return False
#
#
# @app.route('/addcart', methods=['POST'])
# def AddCart():
#     try:
#         prod_id = request.form.get('prod_id')
#         quantity = request.form.get('quantity')
#         products = Product.query.filter_by(id=prod_id).first
#         if prod_id and quantity and request.method == "POST":
#             DictItems = {prod_id: {}}
#             if 'shoppingcart' in session:
#                 print(session['shoppingcart'])
#                 if prod_id in session['shoppingcart']:
#                     flash("This product is already in your cart", 'warning')
#                 else:
#                     session['shoppingcart'] = MagerDicts(session['shoppingcart'], DictItems)
#                     return redirect(request.referrer)
#             else:
#                 session['shoppingcart'] = DictItems
#                 return redirect(request.referrer)
#     except Exception as e:
#         print(e)
#     finally:
#         return redirect(request.referrer)
#
#
# @app.route('/addcart', methods=['POST'])
# def Addcart():
#     try:
#         rec_id = request.form.get('rec_id')
#         quantity = request.form.get('quantity')
#         recom = Recommendation.query.filter_by(id=rec_id).first
#         if rec_id and quantity and request.method == "POST":
#             DictItems = {rec_id: {'name': Recommendation.name, 'price': Recommendation.price, 'discount': Recommendation.discount, 'category': Recommendation.category, 'image': Recommendation.image}}
#             if 'shoppingcart' in session:
#                 print(session['shoppingcart'])
#                 if rec_id in session['shoppingcart']:
#                     print("This product is already in your cart")
#                 else:
#                     session['shoppingcart'] = MagerDicts(session['shoppingcart'], DictItems)
#                     return redirect(request.referrer)
#             else:
#                 session['shoppingcart'] = DictItems
#                 return redirect(request.referrer)
#     except Exception as e:
#         print(e)
#     finally:
#         return redirect(request.referrer)
#
#
# @app.route('/error', methods=['GET', 'POST'])
# def error():
#     return render_template("error.html")
