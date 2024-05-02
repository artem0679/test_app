import datetime

from flask import Flask, render_template,flash, abort, send_from_directory, redirect, url_for, request
from flask_login import current_user, LoginManager, UserMixin, login_required
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from prometheus_client import generate_latest
from prometheus_client import Counter
from prometheus_client import Summary

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from models import User, Products1
from auth import bp as auth_bp, init_login_manager, check_rights

app.register_blueprint(auth_bp)

init_login_manager(app)

INDEX_TIME = Summary('index_request_processing_seconds', 'DESC: INDEX time spent processing request')
c = Counter('requests_for_host', 'Number of runs of the process_request method', ['method', 'endpoint'])




@app.route('/')
@INDEX_TIME.time()
def index():
    return render_template('index.html')


@app.route('/metrics')
def metrics():
    return generate_latest()




def get_json(fields_list):
    dict_ = {}
    for field in fields_list:
        dict_[field] = request.form.get(field)
    return dict_





@app.route('/cost_prod')
def cost_prod():
    products = Products1.query.all()
    return render_template('products/cost_prod.html', products=products)


@app.route('/count_prod')
@login_required
def count_prod():
    users = User.query.all()
    return render_template('products/count_prod.html', users=users)
