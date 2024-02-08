from flask import Flask, render_template, jsonify  
app = Flask(__name__)

lst_jobs = [
{
'id' : 1,
'title' : 'Data Analyst',
'location' :  'Doha',
'salary' : '5000'  
},
{
  'id' : 2,
  'title' : 'Data Sceintist',
  'location' :  'Iran',
  'salary' : '10000'  
  },
{
  'id' : 3,
  'title' : 'Frontend Engineer',
  'location' :  'Remote',
  'salary' : '7500'  
  }
]

@app.route('/') #Decorate Charater  (Empty Route)

def hello_world(): 
   #return "Hello, Python World!, Application using Flask"
   return render_template ('home.html', 
                           jobs=lst_jobs, 
                           company_name='Qatar Computer Services')


@app.route('api/jobs')
def list_jobs():
  return jsonify (lst_jobs)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)