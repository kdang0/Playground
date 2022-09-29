from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play/<x>')
@app.route('/play')
def renderPlay(x=3):
    return render_template('playground.html', times = int(x))


if __name__ == "__main__":
    print("hello")
    app.run(debug=True)