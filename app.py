from flask import Flask, render_template, request

app = Flask(__name__)

def process_string(input_str):
    # Your processing function here
    output_str = input_str.upper()
    return output_str

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_str = request.form['input_str']
        output_str = process_string(input_str)
        return render_template('index.html', output_str=output_str)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
