from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('supplier', __name__, url_prefix='/supplier')

@bp.route('', methods=['GET'])
def supplier():
    return render_template('supplier/overview.html')

@bp.route('/add', methods=['GET', 'POST'])
def add():
    return render_template('supplier/add.html')