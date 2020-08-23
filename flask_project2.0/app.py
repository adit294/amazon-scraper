from flask import Flask, render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
import requests


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db= SQLAlchemy(app)
def helper(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    amzn_product = soup.find('h1', class_='a-size-large a-spacing-none').span.text
    flip_link =  f'https://www.flipkart.com/search?q={amzn_product}'
    snap_link= f'https://www.snapdeal.com/search?keyword={amzn_product}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    flip_source = requests.get(flip_link, headers=headers).text
    flip_soup = BeautifulSoup(flip_source, 'html.parser')
    print(flip_link)
    flip_product_name = flip_soup.find('a', class_='_2cLu-l').text

    flip_price= flip_soup.find('div', class_='_1vC4OE').text
    flip_logo= f'https://aditagarwal.com/connect4/flipkart_logo_test-removebg-preview.png'
    snap_logo= f'https://aditagarwal.com/connect4/snap_logo_test-removebg-preview.png' 

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
    snap_source = requests.get(snap_link, headers=headers).text
    snap_soup = BeautifulSoup(snap_source, 'html.parser')

    snap_product_name = snap_soup.find('p', class_='product-title').text

    snap_price= snap_soup.find('span', class_='lfloat product-price').text

    all_products = [
        {
            'title' : flip_logo,
            'link' : flip_link,
            'price' :flip_price,
            'name' : flip_product_name
        },
            {
            'title' : snap_logo,
            'link' : snap_link,
            'price' :snap_price ,
            'name' : snap_product_name
        }
    ]
    return all_products
    

@app.route("/")
def hello():
    url=request.args.get("url")
    print("hello")
    print(url)
    print("hi")
    all_products = helper(url)
    return render_template("products.html", products= all_products)

@app.route('/products')
def posts():
    return render_template("layout.html" )


if __name__== "__main__":
    app.run(debug=True)



