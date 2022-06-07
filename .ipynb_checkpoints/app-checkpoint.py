{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f0df212",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#import tools\n",
    "from flask import Flask, render_template, redirect, url_for\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ebf6c381",
   "metadata": {},
   "outputs": [],
   "source": [
    "#set up Flask\n",
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0aaefa86",
   "metadata": {},
   "outputs": [],
   "source": [
    "##tell Python how to connect to Mongo using PyMongo\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f53ec90d",
   "metadata": {},
   "outputs": [],
   "source": [
    "##Set Up App Routes\n",
    "\n",
    "#define the route for the HTML page\n",
    "@app.route(\"/\")\n",
    "def index():\n",
    "   mars = mongo.db.mars.find_one()\n",
    "   return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c1dcd7b",
   "metadata": {},
   "outputs": [],
   "source": [
    "#next route and function to our code\n",
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update_one({}, {\"$set\":mars_data}, upsert=True)\n",
    "   return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a1b0c54",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Flask is to tell it to run\n",
    "if __name__ == \"__main__\":\n",
    "   app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d6963a2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
