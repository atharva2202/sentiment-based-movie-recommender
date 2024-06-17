from flask import Flask, render_template, redirect, url_for
import csv
import os
app = Flask(__name__)

# Function to load data from CSV
def load_csv_data(filepath):
    movies = []
    with open(filepath, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Skip the header row
        for row in csvreader:
            movies.append(row)
    return movies

# Route for welcome page
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Route for viewing movies
@app.route('/view_movies')
def view_movies():
    movies = load_csv_data('data/dataset.csv')
    return render_template('index.html', movies=movies)

# Route for sentiment based recommendation form
@app.route('/get_sentiment_based_recommendation')
def get_sentiment_based_recommendation():
    return render_template('recommendation_form.html')

if __name__ == '__main__':
    app.run(debug=True)
