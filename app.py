from flask import Flask, render_template

def create_app(configfile=None):

    # CREATE APP
    inedicola = Flask(__name__)

    # MOVE THESE TO ENVIRONMENT
    inedicola.config['DEBUG'] = 'true'
    inedicola.config['STATIC_URL'] = '/static'

    # ADD EXTENSIONS
    inedicola.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

    # DEFAULTS
    defaults = {
        'STATIC_URL': inedicola.config.get('STATIC_URL', '/static/'),
    } 

    # ROUTING
    @inedicola.route('/')
    def index():
        opts = defaults.copy()
        return render_template('home.jade', **opts)

    @inedicola.route('/options')
    def options():
        opts = defaults.copy()
        return render_template('options.jade', **opts)

    return inedicola

if __name__ == '__main__':
    create_app().run(debug=True)
