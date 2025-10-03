from flask import Flask, render_template, send_from_directory
import os
from logic import sort_files, sort_files_by_sets_and_extension

from consts import PATH

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route('/physics')
def physics():
    files = []
    if os.path.exists(PATH.PHYSICS_REPORTS):
        files = [f for f in os.listdir(PATH.PHYSICS_REPORTS) if os.path.isfile(os.path.join(PATH.PHYSICS_REPORTS, f))]
    return render_template('physics.html', files=files)

@app.route('/')
def home():
    subjects = [
        {'name': 'physics', 'route': 'physics'},
        {'name': 'programming', 'route': 'programming'},
        {'name': 'networks', 'route': 'networks'},
        {'name': 'dct', 'route': 'dct'},
        {'name': 'databases', 'route': 'databases'},
        {'name': 'assembler', 'route': 'assembler'}
    ]
    projects = [
        {'name': 'python', 'route': 'python'},
        {'name': 'c++', 'route': 'cpp'},
        {'name': 'R', 'route': 'R'}
    ]
    notes = [
        {'name': 'physics', 'route': 'physics_notes'},
        {'name': 'dct', 'route': 'dct_notes'},
        {'name': 'assembler', 'route': 'assembler_notes'}
    ]
    return render_template('index.html', subjects=subjects, projects=projects, notes=notes)

@app.route('/subject/<subject_id>')
def subject(subject_id):
    files = []
    if subject_id == 'physics':
        if os.path.exists(PATH.PHYSICS_REPORTS):
            files = [f for f in os.listdir(PATH.PHYSICS_REPORTS) if os.path.isfile(os.path.join(PATH.PHYSICS_REPORTS, f))]
        return render_template('physics.html', files=files, subject_name='physics')
    elif subject_id == 'programming':
        if os.path.exists(PATH.PROGRAMMING_REPORTS):
            files = [f for f in os.listdir(PATH.PROGRAMMING_REPORTS) if os.path.isfile(os.path.join(PATH.PROGRAMMING_REPORTS, f))]
        return render_template('programming.html', files=files, subject_name='programming')
    elif subject_id == 'networks':
        if os.path.exists(PATH.NETWORKS_REPORTS):
            files = [f for f in os.listdir(PATH.NETWORKS_REPORTS) if os.path.isfile(os.path.join(PATH.NETWORKS_REPORTS, f))]
        return render_template('networks.html', files=files, subject_name='networks')
    elif subject_id == 'dct':
        if os.path.exists(PATH.DCT_REPORTS):
            files = sort_files([f for f in os.listdir(PATH.DCT_REPORTS) if os.path.isfile(os.path.join(PATH.DCT_REPORTS, f))])
        return render_template('dct.html', files=files, subject_name='dct')
    elif subject_id == 'databases':
        if os.path.exists(PATH.DATABASES_REPORTS):
            files = [f for f in os.listdir(PATH.DATABASES_REPORTS) if os.path.isfile(os.path.join(PATH.DATABASES_REPORTS, f))]
        return render_template('databases.html', files=files, subject_name='databases')
    elif subject_id == 'assembler':
        if os.path.exists(PATH.ASSEMBLER_REPORTS):
            files = [f for f in os.listdir(PATH.ASSEMBLER_REPORTS) if os.path.isfile(os.path.join(PATH.ASSEMBLER_REPORTS, f))]
        return render_template('assembler.html', files=files, subject_name='assembler')
    return f"Subject page for: {subject_id}"

@app.route('/projects/<project_id>')
def project(project_id):
    files = []
    if project_id == 'python':
        if os.path.exists(PATH.PYTHON_PROJECTS):
            files = [f for f in os.listdir(PATH.PYTHON_PROJECTS) if os.path.isfile(os.path.join(PATH.PYTHON_PROJECTS, f))]
        return render_template('python.html', files=files, subject_name='python')
    elif project_id == 'cpp':
        if os.path.exists(PATH.CPP_PROJECTS):
            files = [f for f in os.listdir(PATH.CPP_PROJECTS) if os.path.isfile(os.path.join(PATH.CPP_PROJECTS, f))]
        return render_template('cpp.html', files=files, subject_name='c++')
    elif project_id == 'R':
        if os.path.exists(PATH.R_PROJECTS):
            files = [f for f in os.listdir(PATH.R_PROJECTS) if os.path.isfile(os.path.join(PATH.R_PROJECTS, f))]
        return render_template('r.html', files=files, subject_name='R')
    return f"Project page for: {project_id}"

@app.route('/notes/<notes_id>')
def notes(notes_id):
    all_files = {}
    print(notes_id)
    if notes_id == 'physics_notes':
        if os.path.exists(PATH.PHYSICS_NOTES):
            for dir_name in os.listdir(PATH.PHYSICS_NOTES):
                dir_path = os.path.join(PATH.PHYSICS_NOTES, dir_name)
                files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                all_files[dir_name] = sort_files_by_sets_and_extension(files)
        return render_template('physics_notes.html', all_files=all_files, subject_name='physics')
    if notes_id == 'dct_notes':
        if os.path.exists(PATH.DCT_NOTES):
            for dir_name in os.listdir(PATH.DCT_NOTES):
                dir_path = os.path.join(PATH.DCT_NOTES, dir_name)
                files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                all_files[dir_name] = sort_files_by_sets_and_extension(files)
        return render_template('dct_notes.html', all_files=all_files, subject_name='dct')
    if notes_id == 'assembler_notes':
        if os.path.exists(PATH.ASSEMBLER_REPORTS_NOTES):
            for dir_name in os.listdir(PATH.ASSEMBLER_REPORTS):
                dir_path = os.path.join(PATH.ASSEMBLER_REPORTS, dir_name)
                files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
                all_files[dir_name] = sort_files_by_sets_and_extension(files)
        return render_template('assembler_notes.html', all_files=all_files, subject_name='assembler')
    return f"Project page for: {notes_id}"

if __name__ == "__main__":
    app.run(debug=True)
