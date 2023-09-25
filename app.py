from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests
import imdb


app = Flask(__name__)
imdbi=imdb.IMDb()

# # Sample movie data
# movies = requests.get("https://vidsrc.to/embed/movie/tt5311514")

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/tv')
def tv():
    return render_template('tv.html')

@app.route('/movie')
def movie():
    return render_template('movie.html')

@app.route("/tvnameid",methods=['POST','GET'])
def search_tv():
    name = request.args.get("name")
    search = imdbi.search_movie(name)
    data = {
        "id": search[0].movieID,
        "title": search[0]['title']
    }
    return data

@app.route("/movienameid",methods=['POST','GET'])
def search_mov():
    name=request.args.get("name")
    search = imdbi.search_movie(name)
    data = {
        "id": search[0].movieID,
        "title": search[0]['title']
    }
    return data

if __name__ == "__main__":
    app.run(debug=True)
