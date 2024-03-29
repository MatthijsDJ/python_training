from flask import ( Flask,
                    render_template,
                    request)

app = Flask(__name__)

db = {'jobs': {'job1': {'name': 'render job',
                        'running': False,
                        'errors': None},
               'job2': {'name': 'cron job',
                        'running': True,
                        'errors': None }
               }
}


@app.route("/")
def hello_world():
    data = {'msg': "Dag mensen!"}
    return render_template('index.html', data=data)


@app.route("/etl/jobs")
def show_etl_jobs():
    data = db
    return render_template('job_list.html', data=data)


@app.route("/etl/jobs/<string:name>", methods=['GET', "POST"])
def show_etl_job_details(name):
    if request.method == 'POST':
        print(request.form)
        return f"<h1>Creating new job with name {name} </h1>"
    else:
        return f"<h1>Job {name} details</h1>"



