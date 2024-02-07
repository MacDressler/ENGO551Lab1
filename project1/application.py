import os

from flask import Flask, session, request, render_template, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) # I need to make sure that I have a session going so that I can have active usernames. 

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine)) # This loads the connection to my database

def reviews(book_id): # I need this function in order to get the stats from my review database
    review = db.execute("SELECT count(review), round(avg(rating), 2) FROM review where book_id = :id;", {'id':book_id}).fetchone() # This gives these two stats from the table.
    return [review.count, float(str(review.round))]



@app.route("/signup", methods = ['GET','POST']) # I need the get and post because users will need to add info
def signup():
    if request.method =='POST':
        username = request.form.get('username') # I need one username
        password1 = request.form.get('password1') # I need to get two passwords that need to match
        password2 = request.form.get('password2')
        if password1 != password2:
            return render_template('signup.html', message = "Password did not match.") # The message goes to the message in the html
        try:

            user = db.execute(text("INSERT into users (username, password) values (:username, :password)"), {'username':username, 'password':password1})
            db.commit() # I need to add the new info to the database so that they can log in again.
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for("search"))
        
        except:
            return render_template('signup.html', message = "Username already exists, please try another") # If you try and insert a username again then it won't work.
        
    return render_template('signup.html')


@app.route("/book/<isbn>", methods = ['GET','POST']) # This isbn makes the different webpage depending on the book.
def book(isbn):# isbn is unique to each book.
    message = None 
    status = False
    error_message = False
    if request.method == "POST" and session['logged_in']: # This is for when you want to add a review
        my_rating = int(request.form.get('rating')) # This is added using the dropdown menu
        my_review = request.form.get('review') # This is from the text review
        id = request.form.get('book_id')
        if my_review.strip() =="" or my_rating == "": # If the review has no words it doesn't work.
            message == "Invalid Review"
        else:
            db.execute(text("INSERT into review (username, review, rating, book_id) select :username, :review, :rating, :book_id where not exists (SELECT * from review where username = :username and book_id = :book_id);"),
            {
                'username': session['username'], # These are all of the important components of the review.
                'review': my_review,
                'rating': my_rating,
                'book_id': id
            })
            db.commit()
            status = True

    res = db.execute(text("select * from books where isbn=:isbn;"), {'isbn':isbn}).fetchone() # if it can't find a book with the isbn, then it returns the same original page.
    if res == None:
        return render_template('book.html')
    
    reviews = db.execute(text("select * from review where book_id = :id;"), {'id':res.id}).fetchall() # This lists the different reviews for each book.
    if request.method == "GET":
        try:
            if session['logged_in']:
                check_review = db.execute(text("select username from review where book_id=:id and username = :username;"), #this checks if there is a review from the session username. If there is then you can't add another.
            {
                'id':res.id,
                'username': session['username']
            }).fetchone()
                if check_review != None: # if there is no review, then the user can add another.
                    status = True
        except:
            pass

    try:
        count, rating= reviews(isbn) # this calls the previous function.
    except:
        error_message = True
        count, rating = 0, 0
    return render_template('book.html', obj_book = res, reviews= reviews,count = count, rating =rating, status = status,error = error_message)
        

@app.route("/login", methods = ['GET', 'POST']) # This page will have input and output
def login():
    if request.method == 'POST': # This is the section about when the user wants to add information to the database
        username = request.form.get('username') # I need to get the username and password from the user. Then I add this information to the database.
        password = request.form.get('password')
        user = db.execute(text("select * from users where username = :username and password = :password;"), {'username':username, 'password':password})
        if user.rowcount == 0: # This happens if there is no database entry where the usernames and database match the same id number.
            return render_template('loginerror.html')
        session['logged_in']=True # The website changes when a user is logged in
        session['username'] = request.form['username'] # I need this so that I can make sure that a user can't add a new review for the same book 
        return redirect(url_for("search")) # This is the main page
    
    return render_template('login.html') 

            


@app.route("/books")
def books():
    info = request.args.get('search') # I need the search result
    if info!= None:
        info = info.strip().replace("'", "") # Ijust need to make sure that the search doesn't include quotation marks
        obj_book = db.execute(text("SELECT * from books where isbn LIKE ('%"+info+"%') or lower (title) LIKE lower ('%" + info + "%') or lower(author) LIKE lower('%" + info + "%') order by year desc;")).fetchall()
        count = len(obj_book) # obj_book is the dictionary for the books that somewhat match the search results
        if count == 0:
            return render_template('books.html', info = info, count = count, message = "Book Not Found") # I need this if the search doesn't yield results
        
        return render_template('books.html', info = info, count = count, obj_book = obj_book) # This makes the page with the list, along with the html
    return render_template('books.html')


@app.route("/")
def search():
    return render_template('search.html') # This makes the search page the main page.

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login")) # I need logout functionality so that the user can end the session.

    #In order to run the code type python -m flask run in the command line

