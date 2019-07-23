from flask import Flask, request, render_template
from dao import dboperations

app = Flask(__name__)
home_page = "home.html"


@app.route('/<page>', methods=["GET"])
def load_page(page):
    if page == 'home':
        return render_template("home.html")
    elif page == 'create':
        return render_template("create.html")
    else:
        return "Not found ----"


@app.route('/publish', methods=["POST"])
def save_post():
    args = request.form
    subject = args.get("subject")
    article = args.get("content")
    dboperations.save_post(subject, article)
    return render_template(home_page)


@app.route('/get_all_posts', methods=["GET"])
def get_all_posts():
    print("Inside getAllPosts")
    return dboperations.get_all_posts()


if __name__ == "__main__":
    app.run(port="8080", host="0.0.0.0", threaded=True)
