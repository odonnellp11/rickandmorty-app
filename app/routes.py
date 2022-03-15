from app import app

from flask import render_template

@app.route('/')
def home():
    headline = 'welcome to the many worlds or Rick & Morty'
    description = 'Rick and Morty is the Emmy award-winning half-hour animated hit comedy series on Adult Swim that follows a sociopathic genius scientist who drags his inherently timid grandson on insanely dangerous adventures across the universe.'
    return render_template('index.html', headline = headline, description = description)

@app.route('/characters')
def characters():
    return render_template('char.html')

@app.route('/rick')
def Ricks():
    return render_template('/rick.html')

@app.route('/morty')
def mortys():
    return render_template('/morty.html')
