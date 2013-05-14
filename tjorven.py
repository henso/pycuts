""" tjorven """

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify(request.args)

if __name__  == "__main__":
    app.debug = True
    app.run()