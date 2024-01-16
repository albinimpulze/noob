from flask import Flask, render_template, request
from bot import generate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_form', methods=['POST'])
def process_form():
    prompt = request.form['input_field']
    bot_result = generate(prompt)
    print(f"Answer: {bot_result}")
    return render_template('index.html', result=bot_result)

if __name__ == '__main__':
    app.run(debug=True)