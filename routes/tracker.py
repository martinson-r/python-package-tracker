from flask import Blueprint, render_template, redirect, url_for
from app.models import db, Package

from app.shipping_form import ShippingForm

bp = Blueprint('Tracker', __name__, url_prefix="")

@bp.route('/')
def index():
  packages = Package.query.all()
  return render_template('package_status.html', packages=packages)


@bp.route('/new_package', methods=['GET', 'POST'])
def package():
  form = ShippingForm()
  if form.validate_on_submit():
    package = Package()
    form.populate_obj(package)
    package.location = package.origin
    package.save()
    Package.advance_all_locations()
    return redirect(url_for('.index'))
  return render_template('shipping_request.html', form=form)
