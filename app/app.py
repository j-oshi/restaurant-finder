from flask import Flask, render_template, request, jsonify
from functions import filter_restaurant

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/find-restaurants", methods=["POST"])
def fetch_restaurant():
    if request.method=='POST':
        restaurant_postcode = request.get_json()
        response = filter_restaurant(restaurant_postcode['user_input'])

        return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False)