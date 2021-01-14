from flask import Blueprint, render_template, redirect, url_for

from app.shipping_form import ShippingForm

bp = Blueprint('Tracker', __name__, url_prefix="")

@bp.route('/')
def index():
  return "Package tracker!"


@bp.route('/new_package', methods=['GET', 'POST'])
def package():
  form = ShippingForm()
  if form.validate_on_submit():
    return redirect(url_for('.index'))
  return render_template('shipping_request.html', form=form)
