from flask import Flask, render_template, request, abort

from utils import load_candidates, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates = load_candidates()
    if not candidates:
        abort(404)
    return render_template('candidates.html',
                           title='Candidates',
                           candidates=candidates
                           )


@app.route('/candidate/<int:pk>')
def candidate(pk):
    candidates = load_candidates()
    person = get_candidate(pk)
    if not person:
        abort(404)
    skills = person['skills'].split(', ')
    return render_template('candidates.html',
                           title=person["name"],
                           candidates=candidates,
                           person=person,
                           skills=skills)


@app.route('/search', methods=['POST'])
def search_by_name():
    candidate_name = request.form['name']
    candidates = load_candidates()
    found_candidates = get_candidates_by_name(candidate_name)
    return render_template('candidates.html',
                           title='Candidates',
                           candidates=candidates,
                           name=candidate_name,
                           found_by_name=found_candidates
                           )


@app.route('/skill', methods=['POST'])
def search_by_skill():
    skill = request.form['skill']
    candidates = load_candidates()
    found_candidates = get_candidates_by_skill(skill)
    return render_template('candidates.html',
                           title='Candidates',
                           candidates=candidates,
                           skill=skill,
                           found_by_skill=found_candidates
                           )


@app.route('/part1')
def part1():
    """ Part 1 of the homework"""
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='404 Not found')


if "__name__" == "__main__":
    app.run(debug=True)
