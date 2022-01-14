from flask import Blueprint, render_template, request, flash


auth = Blueprint('auth', __name__)

@auth.route("/login", methods =['GET', 'POST'])
def login():
    data= request.form 
    return render_template('login.html')
@auth.route('/logout')
def logout():
    return "<p>Logout</p>" 

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1= request.form.get('password1')
        password2= request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4', category='error')
        elif len(firstName <2):
            flash('name is too short', category ="error")
        elif password1 != password2:
            flash("passwords must be the same", category = "error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long", category = "error")
        else:
            flash("Account created", category= 'success')

    return render_template("home.html")


    return render_template('signup.html')