from flask import Flask,render_template,request 
import csv
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def write_to_file(data):
    with open('database.csv','a') as database:
        print(data)
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])

@app.route('/submit_form', methods=['GET','POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return render_template('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

