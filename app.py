from flask import Flask
app = Flask(__name__)

@app.route('/') #Decorate Charater  (Empty Route)
def hello_world(): 
   return "Hello, Python World!"

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)