from flask import Flask, render_template, redirect, request
from transformers import pipeline
import torch


app = Flask(__name__)

#variables from ai
generator = pipeline('text-generation', model='gpt2', device=0)

def ai(user_input):
    #the magic is on do_sample that enables randomness and creativity and tempature that set how much is the creativite
    output = generator(user_input, max_length=300, num_return_sequences=1, do_sample=True, temperature=0.99)
    return output[0]['generated_text']

def home():
    return redirect('/')

@app.route("/")
@app.route('/ai', methods=['GET', 'POST'])
def hello_world():
    output = " "
    if request.method == 'POST':
        user_input = request.form.get('Input')
        output = ai(user_input)
    return render_template('index.html', output=output)
@app.route('/home', methods=['GET', 'POST'])
def homereturn():
    if request.method == 'POST':
        return('/')
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)