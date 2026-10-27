from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("registration.html")

@app.route("/register", methods=["POST"])
def submit_registration():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not email:
        return "Name and email are required.", 400

    return render_template(
        "success.html",
        name=name,
        email=email
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)