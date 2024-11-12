from flask import Flask, request, render_template, redirect, url_for
from app.CRUD import *
from datetime import datetime
app =  Flask(__name__)

@app.route("/")
def index():
    tasks = read()  # Obtiene todas las tareas
    return render_template("index.html", tasks=tasks)

@app.route("/save-data", methods=["POST"])
def process():
    name = request.form.get('task')
    description = request.form.get('description')
    startDate = request.form.get('fecha-inicio') or datetime.now().date()
    endDate = request.form.get('fecha-finalizacion') or datetime.now().date()
    if name !=  "":
        create(name, description, startDate, endDate)
    return redirect(url_for('index'))


@app.route('/edit-task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        name = request.form['task']
        description = request.form['description']
        
        # Convertir fecha a formato 'YYYY-MM-DD HH:MM:SS'
        start_date = datetime.strptime(request.form['fecha-inicio'], '%Y-%m-%dT%H:%M').strftime('%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(request.form['fecha-finalizacion'], '%Y-%m-%dT%H:%M').strftime('%Y-%m-%d %H:%M:%S')
        if name != "":
            update(name, description, start_date, end_date, task_id)
        return redirect(url_for('index'))

    task = get_task_by_id(task_id)
    return render_template('edit_task.html', task=task)




@app.route("/delete-task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    delete(task_id)  
    return redirect(url_for("index"))
