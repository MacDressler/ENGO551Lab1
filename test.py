import os
import requests
from flask import Flask, session, request, render_template, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


#res = requests.get("https://www.googleapis.com/books/v1/volumes", params={"q": "isbn:0812995341"})
#print(res.json())
#value = res.json().get('items')
#x = value('volumeInfo')
#x.index('ratingsCount')
#count = x.get('ratingsCount')
#rating = x.get('averageRating')
#print([count, rating])

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def google_books(book_id):
    res = requests.get("https://www.googleapis.com/books/v1/volumes", params={'key': 'GOOGLE_BOOKS_API_KEY', 'q': f'isbn:{book_id}'})
    info = res.json()
    if 'items' in info and info['items']:
        data = info['items'][0]['volumeInfo']
        count = data.get('ratingsCount', 'N/A')
        rating = data.get('averageRating', 'N/A')
    
    print([count, rating])
    return[count, rating]


@app.route('/', methods=['GET'])
def get_review_count():
    isbn = 1443455881
    api_key = 'YOUR_GOOGLE_BOOKS_API_KEY'
    
    if not isbn:
        return jsonify({'error': 'ISBN parameter is missing'}), 400
    
    # Make request to Google Books API
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    # Extract review count
    review_count = 0
    if 'items' in data and data['items']:
        review_count = data['items'][0]['volumeInfo'].get('ratingsCount', 0)

    return jsonify({'isbn': isbn, 'review_count': review_count})

if __name__ == '__main__':
    app.run(debug=True)
