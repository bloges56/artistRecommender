from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin
from musiccollaborativefiltering import load_user_artists, ArtistRetriever
from musiccollaborativefiltering import ImplicitRecommender
import implicit
from pathlib import Path

app = Flask(__name__, static_folder='client/build', static_url_path='')
CORS(app)

@app.route("/members")
@cross_origin()
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/recommender")
@cross_origin()
def recommender():
    # load user artists matrix
    user_artists = load_user_artists(Path("./lastfmdata/user_artists.dat"))

    # instantiate artist retriever
    artist_retriever = ArtistRetriever()
    artist_retriever.load_artists(Path("./lastfmdata/artists.dat"))

    # instantiate ALS using implicit
    implict_model = implicit.als.AlternatingLeastSquares(
        factors=50, iterations=10, regularization=0.01
    )

    # instantiate recommender, fit, and recommend
    recommender = ImplicitRecommender(artist_retriever, implict_model)
    recommender.fit(user_artists)
    artists, scores = recommender.recommend(2, user_artists, n=5)
    return {"artists": artists}

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)

