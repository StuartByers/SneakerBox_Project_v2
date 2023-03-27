from flask import Flask, render_template

from controllers.sneakers_controller import sneakers_blueprint

app = Flask(__name__)

app.register_blueprint(sneakers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)