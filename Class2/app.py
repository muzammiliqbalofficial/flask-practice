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
    total_students = len(Students)  # Total count calculate kiya
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

# YE NEW ROUTE ADD KARO
@app.route('/profile/<student_id>')
def profile(student_id):
    # Student dhundo ID se
    student = None
    for s in Students:
        if s['id'] == student_id:
            student = s
            break
    
    # Agar mila toh show.html me hi profile mode me render karo
    if student:
        return render_template('show.html', data=Students, profile_student=student, total=len(Students))
    else:
        return "Student not found!", 404

if __name__ == '__main__':
    app.run(debug=True)
