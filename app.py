from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')

def index():
   return render_template("index.html")

@app.route('/convert', methods=['GET', 'POST'])

def form():
   if request.method == 'POST':
      currency = request.form.get('amount')
      print(type(currency))
      abc = str(currency)
      print(abc + "stringhereeeee")
      print(type(abc))
      # print(currency)
      # return currency



if __name__ == '__main__':
   app.run(debug = True)
   app.run()