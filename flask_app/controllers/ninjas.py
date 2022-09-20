from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask_app import app


@app.route('/ninjas')
def ninjas_index():
    return render_template('index_ninja.html', all_dojos=Dojo.get_all())


@app.route('/ninjas/process', methods=['POST'])
def new_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo_id']
    }
    new_ninja = Ninja.add_ninja(data)
    if new_ninja != False:
        return redirect(f"/dojos/{request.form['dojo_id']}")
    return redirect('/ninjas')