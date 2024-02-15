# ENGO551Lab1
Here is my submission for lab 1.

I used python, css, sql and html for this lab. The css is not done. I promise I will make the website look prettier for the next submission. The templates file contains all of my html files. This was required for flask. Book.html corresponds to each page. It takes the isbn in the python to create the correct book. Books is the search result page. login is the login page. This one won't let you through if you have the wrong info. login error is a file to make a page with an error. I thought it was funny, and I didn't like the way that the error looked on the same page. I think I will try and make this a pop up for the next lab. Login error 2 was more funny, but the link was annoying so I scrapped it. Search is the home page, and lets you search for books. Signup page lets you create a new account. It communicates with the database.

Application.py is the main file that runs the web app. Make sure to use the info at the bottom of the page to run the project. My favourite part was the search mechanism. It was fun reading about SQL. Books.csv was provided before. Models.py was something I saw on some websites for creating your database. They used it to create each table, and then linked it into your main application page. I was trying to do that but found it too many steps. import.py is the last file and it imports all of the books. It loops through the csv and does a new sql call on each row, which seems inefficient but it worked so here we go.

Thank you for looking at my project! 

I hope you enjoy.


For Lab 2, here is the second readme. 

In order to run the code, please use the following two lines to set up your machine. 

run this first at the beginning of the session  $env:FLASK_APP = "application.py"
In order to run the code type python -m flask run in the command line

This lab allows the user to review books, and it also draws on the google books api in order to provide the user with more review statistics. The files are the same as lab 1. There are a few more files here but these were generated to test out the api. 
I started trying to figure out chatgpt for this lab. Here are some of the questions that I asked chatgpt.

how do I use jsonify to write an error message in my api
what is the difference between isbn 10 and isbn 13
can you help me make an API to extract the review count for particular books from the Google books website based on the ISBN number?
can you please build me an amazing css file to make my book review website look magical?
please make it more magical
please make it more magical
