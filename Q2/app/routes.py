from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import SubmissionForm
import re
import collections

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SubmissionForm()
    if form.validate_on_submit():
        new_text = form.text.data
        new_delimiter = form.delimiter.data
        new_operationname = form.operationname.data
        if new_operationname == 'wordcount':
            return redirect(url_for('results', operationname=new_operationname, text=new_text, delimiter=new_delimiter))
        if new_operationname == 'charactercount':
            return redirect(url_for('results', operationname=new_operationname, text=new_text))
        if new_operationname == 'mostfrequent5':
            return redirect(url_for('results', operationname=new_operationname, text=new_text))
    return render_template('index.html', title='Home', form=form)

@app.route('/results/<operationname>/<text>', methods=['GET', 'POST'])
@app.route('/results/<operationname>/<text>/<delimiter>', methods=['GET', 'POST'])
def results(operationname, text, delimiter=""):
    if operationname == 'wordcount':
        count = len(re.split('[\s+' + delimiter + ']', text))
        return render_template('results.html', title="wordcount", count=count)
    if operationname == 'charactercount':
        count = len(text)
        return render_template('results.html', title="charactercount", count=count)
    if operationname == 'mostfrequent5':
        words = text.split()
        counter = collections.Counter(words).most_common()
        printstr = ""
        for i in range(5):
            printstr += counter[i][0] + ' '
        return render_template('results.html', title="mostfrequent5", s=printstr)
    return render_template('results.html', title="wordcount", count='0')    

@app.errorhandler(403)
def not_allowed(error):
    return render_template('403.html'), 403

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
