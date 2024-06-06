from flask import Flask, render_template

app = Flask(__name__, template_folder=
'templates'
)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/clothing')
def clothing():
    return render_template('categories.html')

@app.route('/shoes')
def jacket():
    return render_template('product.html')

if __name__ == '__main__':
    app.run(debug=True)