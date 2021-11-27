from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/contactus')
def contact_us_page():
    return render_template("contact_us.html")

if __name__ == '__main__':
    app.run(debug=True)
