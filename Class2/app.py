# pip install flask
# python -m venv venv
# pip list

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

Students = [
    {
        'name': 'Ali',
        'id': '1',
        'grade': '50'
    },
    {
        'name': 'Sara',
        'id': '2',
        'grade': '85'
    },
    {
        'name': 'Ahmed',
        'id': '3',
        'grade': '92'
    }
]

@app.route('/')
def index():
    total_students = len(Students)  # Total count
    return render_template('show.html', data=Students, total=total_students)

@app.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form.get('name')
        id = request.form.get('id')
        grade = request.form.get('grade')

        Students.append({
            'name': name,
            'id': id,
            'grade': grade
        })
        return redirect(url_for('index'))
    else:
        return render_template('form.html')

# NEW ROUTE: Profile page
@app.route('/profile/<student_id>')
def profile(student_id):
    # Find student by ID
    student = None
    for s in Students:
        if s['id'] == student_id:
            student = s
            break
    
    if student:
        return render_template('profile.html', student=student)
    else:
        return "Student not found!", 404

if __name__ == '__main__':
    app.run(debug=True)