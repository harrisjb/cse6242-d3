from flask import Flask, request, session, redirect, url_for, render_template, flash
import csv

from datetime import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)  # load config from this file , flaskr.py
#app.debug = True

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

# Retieve data from 'static' directory. Used most typically for rendering images.
@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)


@app.route('/')
@app.route('/index')
def index():
    ui_data = {"slide2":slide2_data(),
               "slide5":slide5_data()}
    logging.debug("ui_data [{}]".format(ui_data))
    return render_template('index.html', ui_data=ui_data)

def slide2_data():
    # Build up data required to render slide two and return it in the form of a dictionary
    #dir_path = "./static/data/pill_totals_by_distributor_o.tsv"
    dir_path = "./static/data/reporter_family_ranks_top100_o.tsv"
    pill_totals = csv.DictReader(open(dir_path),delimiter='\t')
    #logging.debug("pill totals [{}]".format(pill_totals))
    return pill_totals

def slide5_data():
    # Build up data required to render slide five and return it in the form of a dictionary
    dir_path = "./static/data/manufacturers_ranks_o.tsv"
    pill_totals = csv.DictReader(open(dir_path),delimiter='\t')
    #logging.debug("pill totals [{}]".format(pill_totals))
    return pill_totals

@app.route('/references')
def references():
    return render_template('references.html')


# Load default config and override config from an environment variable
app.debug = True
app.config.update(dict(
    SECRET_KEY='development key',
    WTF_CSRF_ENABLED=True,
))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
    # app.run(host='0.0.0.0')
