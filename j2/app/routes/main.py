from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint('main', __name__)

@main_bp.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@main_bp.route('/', methods=['GET'])
def home():
    return redirect(url_for('main.index'))
