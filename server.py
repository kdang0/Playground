from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def renderPlay(x=3, color="rgb(73, 145, 226)"):
    return render_template('playground.html', times = x, color= color)


if __name__ == "__main__":
    print("hello")
    app.run(debug=True)