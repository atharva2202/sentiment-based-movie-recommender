from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

def load_csv_data(filepath):
    movies = []
    with open(filepath, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Skip the header row
        for row in csvreader:
            movies.append(row)
    return movies

@app.route('/')
def index():
    movies = load_csv_data('data/dataset.csv')
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
