from flask import Flask, render_template, request

app = Flask(__name__)

deserts = [
    {"name" : "chocolate", "price": 150},
    {"name" : "strawberry", "price": 550},
    {"name" : "blueberry", "price": 750},
    {"name" : "icecream", "price": 1150}
]

@app.route("/")
def home():
    return render_template(
        'index.html',
        deserts = deserts,
        cafe_name = "Sweet Bakery",
        message = "MADE IN HOME"
    )

if __name__ == "__main__":
    app.run(debug=True)