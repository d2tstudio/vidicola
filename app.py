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

    @inedicola.route('/login')
    def login():
        opts = defaults.copy()
        return render_template('login.jade', **opts)

    @inedicola.route('/cart')
    def cart():
        opts = defaults.copy()
        return render_template('cart.jade', **opts)

    @inedicola.route('/guida')
    def guida():
        opts = defaults.copy()
        return render_template('guida.jade', **opts)

    @inedicola.route('/assistenza')
    def assistenza():
        opts = defaults.copy()
        return render_template('assistenza.jade', **opts)

    @inedicola.route('/azienda')
    def azienda():
        opts = defaults.copy()
        return render_template('azienda.jade', **opts)

    @inedicola.route('/account')
    def account():
        opts = defaults.copy()
        return render_template('account.jade', **opts)

    @inedicola.route('/promo')
    def promo():
        opts = defaults.copy()
        return render_template('promo.jade', **opts)

    @inedicola.route('/cartaceo')
    def cartaceo():
        opts = defaults.copy()
        return render_template('cartaceo.jade', **opts)


    return inedicola

if __name__ == '__main__':
    create_app().run(debug=True)
