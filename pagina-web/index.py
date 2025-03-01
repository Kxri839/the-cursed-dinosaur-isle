from flask import Flask, render_template
app = Flask(__name__, template_folder="../templates")

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/contacto")
def contacto():

    return render_template("contacto.html")

@app.route("/jugetes")
def jugetes():
    misjugetes  = ("")

    return render_template("jugetes_dinosaurios.html", jugetes=misjugetes)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)



