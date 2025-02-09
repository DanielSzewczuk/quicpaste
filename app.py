from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET'])
def home():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)