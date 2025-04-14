from flask import Flask, render_template, request, jsonify
import pandas as pd

# Load anime data
data = pd.read_csv('C:/Users/benny/Desktop/PRG/Anime/anime.csv')

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    # Render the HTML front-end
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the genre from the request
    genre = request.json.get('genre')
    
    # Filter the dataset for matching genres
    recommendations = data[data['genre'].str.contains(genre, case=False, na=False)].head(5)
    
    # Return the recommendations as JSON
    return jsonify(recommendations=recommendations['title'].tolist())

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)

