from flask import Flask, render_template , send_file
from get_image import get_image

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    get_image()
    
    return render_template('index.html')


@app.route('/img')
def img():
    return render_template('slider.html')

if __name__ == "__main__":
    app.run(debug=True)