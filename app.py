from flask import Flask, render_template, jsonify

app = Flask(__name__)


# ... rest of your code
@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/api/protien/')
#def protien():
#return render_template('protien.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
