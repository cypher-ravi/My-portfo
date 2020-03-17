from flask import Flask, render_template,url_for, request, redirect
import csv




app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# function to store data into the database
def write_to_file(data):
    with open('database.txt', 'a') as db:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = db.write(f'\n{name},{email},{subject},{message }')


def write_to_csv(data):
    with open('database.csv', 'a') as db2:
        name = data["name"]
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db2, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

# for sending data to the server

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again'


