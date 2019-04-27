from flask import Blueprint,render_template



web_blueprint = Blueprint('web', __name__)


@web_blueprint.route('/index/',methods=['GET'])
def index():
    return render_template('web/index.html')

@web_blueprint.route('/about/',methods=['GET'])
def about():
    return render_template('web/about.html')

@web_blueprint.route('/share/',methods=['GET'])
def share():
    return render_template('web/share.html')

@web_blueprint.route('/list/',methods=['GET'])
def list():
    return render_template('web/time.html')
