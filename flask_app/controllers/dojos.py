from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app import app


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos_index():
    return render_template('index_dojo.html', all_dojos=Dojo.get_all())

@app.route('/dojos/process', methods=['POST'])
def new_dojo():
    data = {
        'name': request.form['name']
    }
    new_dojo = Dojo.add_dojo(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def details_dojo(id):
    data = {
        'dojo_id': id
    }
    dojo_ninjas = Dojo.get_dojo_ninjas(data)
    return render_template('index_details_dojo.html', dojo=dojo_ninjas)