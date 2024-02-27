from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        example = request.form['example']
        print(example)
    return render_template('main.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
