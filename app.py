from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "Version 5 Application"
=======
    return "Version 3 Application"
>>>>>>> parent of c2d5b90 (version 4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)