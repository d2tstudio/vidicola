from flask import Flask, render_template

def create_app(configfile=None):

    # CREATE APP
    inedicola = Flask(__name__)

    # MOVE THESE TO ENVIRONMENT
    inedicola.config['DEBUG'] = 'true'

    # ADD EXTENTIONS
    inedicola.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    # ROUTING
    @inedicola.route('/')
    def index():
        return render_template('components.jade')

    return inedicola

if __name__ == '__main__':
    create_app().run(debug=True)
