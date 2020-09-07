from flask import render_template, request, redirect, url_for, flash,session
from app.api.dao.user import UserDAO
from app.database.models.user import UserModel
from app.database.sqlalchemy_extension import db

obj = UserDAO()

# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             flash("You need to login first")
#             return redirect(url_for('login_page'))
#     return wrap

def dboard(app):
    @app.route('/admin')  
    def admin():
        obj = UserModel.query.order_by(UserModel.id).all()
        return render_template('admin/dashboard.html',title='Home',obj=obj)

    @app.route('/admin/login', methods=['GET', 'POST'])
    def login_page():
        session['username'] = 'Admin'
        error = None
        if request.method == 'POST':
            print(db)
            authenticate = obj.authenticate(
                request.form['username'], request.form['password'])
            try:
                username = UserModel.query.filter_by(
                    username=request.form['username']).first()
                if username.is_admin and username.password_hash:
                    if session['username'] == username.name:
                        flash('You were successfully logged in....')
                        return redirect(url_for('admin'))
                elif authenticate:
                    flash('Only admin can login....')
                    return render_template('admin/login.html', title='Login')
                else:
                    error = 'Please check your login details and try again.'
                    return render_template('admin/login.html', title='Login', error=error)
            except Exception as e:
                print(e)
        return render_template('admin/login.html', title='Login',error = error)
    @app.route("/logout/")
    # @login_required
    def logout():
        session.clear()
        flash("You have been logged out!")
        return redirect(url_for('login_page'))
        
    @app.route('/userdata/<id>')
    def user(id):
        try:
            '''
                Detail View
            '''
            obj = UserModel.query.filter_by(id=id).first()
            return render_template('admin/userview.html', title=obj.name, obj=obj)
        except Exception as e:
            return render_template('admin/userview.html', title='No Name', obj=obj)
        

    @app.route('/create', methods=['GET', 'POST'])
    def create():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']

            my_data = UserModel(name, email)
            # db.session.add(my_data)
            # db.session.commit()
            flash("User Inserted Successfully")
            return redirect(url_for('admin'))
        return render_template('admin/create.html', title='Create User')
    @app.route('/update/<id>', methods=['GET', 'POST'])
    def update(id):
        obj = UserModel.query.filter_by(id=id).first()
        if request.method == 'POST':
            my_data = UserModel.query.get(request.form.get('id'))
            # my_data.name = request.form['name']
            # db.session.commit()
            print(request.form['name'])
            flash("User Updated Successfully")
            return redirect(url_for('admin'))
        return render_template('admin/update.html',title='Update User', obj=obj)
    
    @app.route('/delete/<id>/', methods=['GET', 'POST'])
    def delete(id):
        my_data = UserModel.query.get(id)
        db.session.delete(my_data)
        db.session.commit()
        flash("User Deleted Successfully")

        return redirect(url_for('admin'))
