from flask import Flask, render_template, request
import configurations
import model.pyrebase as q

app = Flask(__name__)
email = "null"

firebsevar = q.initialize_app(config=configurations.config)
db = firebsevar.database()


@app.route('/')
def Base_qstn_paper_set():
    
    return render_template('first.html')


@app.route('/foo', methods=['POST', 'GET'])
def foo():
    if request.method == 'POST':
        first = request.form['first']
        second = request.form['second']
        third = request.form['third']

        email = request.form['emailID']

        ans = {"a1": first, "a2": second, "a3": third, "email": email}

        result = db.child("/answers").push(ans)
        print(result)
    return render_template('first.html')

if __name__ == '__main__':
    app.run()
