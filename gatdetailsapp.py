from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('getdetails.html')

@app.route('/submit', methods=['POST'])
def details_print():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        password = request.form['password'] 
        address = request.form['address']    
        return render_template('details.html', name=name, age=age, password=password, address=address)

if __name__ == "__main__":
    app.run(host="0.0.0.0") 