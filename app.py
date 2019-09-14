from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
   return render_template("index.html")

@app.route('/convert', methods=['GET', 'POST'])

def form():
   if request.method == 'POST':
      amount = request.form['amount']
      print(type(amount))
      abc = str(amount)
      print(abc + "stringhereeeee")
      print(type(abc))
      print(currency)
      return ''' 
      <h1> the value is: {amount}</h1>
      
      '''



if __name__ == '__main__':
   app.run(debug = True)
   app.run()