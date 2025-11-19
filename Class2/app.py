# pip install flask
# python -m venv venv
# pip list

from flask import Flask, render_template, request, url_for, redirect   # <- added redirect

app = Flask(__name__)

Students = [
    {
        'name': 'Ali',
        'id': '1',
        'grade': '50'
    }
]

@app.route('/')
def index():
    return render_template('show.html', data=Students)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        id = request.form.get('id')
        grade = request.form.get('grade')   # <- grade must match form name="grade"

        Students.append({
            'name': name,
            'id': id,
            'grade': grade
        })
        # return render_template('index.html', data=Students)
        return redirect(url_for('index'))   # <- fixed redirect syntax
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
