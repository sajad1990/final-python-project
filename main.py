from flask import Flask, render_template
from second import second 

app = Flask(__name__)
app.register_blueprint(second, url_prefix="")

@app.route("/")
def test():
    return render_template("base.html")

'if__name__'== "__main__"
app.run(debug=True) 
