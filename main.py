from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def main():
    model = {"title": "Hello From ArgoCD and this is listening on port 80."}
    return render_template('index.html', model=model)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)