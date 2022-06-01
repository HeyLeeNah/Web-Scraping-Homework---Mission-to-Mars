from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

Mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():
    mars_data = Mongo.db.mars_data.find_one()
    return render_template("index.html", mars=mars_data)


@app.route("/scrape")
def scraper():
    mars_data = Mongo.db.mars_data
    mars = scrape_mars.scrape()
    mars_data.update_one({}, {"$set": mars}, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)