from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<string:obj>')
def inputText(obj=None):
    return render_template('main.html', obj=obj)

@app.route('/translate', methods=['POST'])
def translate(obj=None):
    if request.method == 'POST':
        temp = request.form['obj']
    else:
        temp = None
    return redirect(url_for('inputText',obj=temp))

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
