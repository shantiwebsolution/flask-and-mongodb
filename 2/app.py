from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'tutedude'  # Needed for flashing messages

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://princeswami:LcmoGsFq8LR4GK84@cluster0.ipx4yqq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["test_db"]
collection = db["test_collection"]

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            flash("All fields are required!", "error")
            return render_template('form.html')

        try:
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except Exception as e:
            flash(f"Error occurred: {str(e)}", "error")
            return render_template('form.html')

    return render_template('form.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
