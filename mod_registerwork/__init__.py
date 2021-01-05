from flask import Blueprint , render_template

register_work = Blueprint('register_work',__name__,url_prefix='/register_work/')

@register_work.route('/')
def index():
    return render_template('register_work.html')