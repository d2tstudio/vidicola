from flask import Flask, render_template
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
app.debug = True

@app.route('/')
def hello_world():
    return render_template('base.jade')

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('base.jade', name=name)

if __name__ == "__main__":
    app.run()
