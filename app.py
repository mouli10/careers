from flask import Flask, render_template,  jsonify

app = Flask(__name__)

JOBS = [
   {
      'id': 1,
      'title': 'Data Analyst',
      'location': 'Hyderabad, India',
      'salary': 'Rs. 10,00,000'
   },

   {
      'id': 2,
      'title': 'Data Scientist',
      'location': 'Bengaluru, India',
      'salary': 'Rs. 15,00,000'
   },
    {
      'id': 3,
      'title': 'Software Developer',
      'location': 'Delhi, India',
      'salary': 'Rs. 19,00,000'
   },
   {
      'id': 4,
      'title': 'Full Stack developer',
      'location': 'San Fransisco, USA',
      'salary': 'USD. 1,00,000'
   }

]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
   return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)


