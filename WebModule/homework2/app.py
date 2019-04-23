from flask import Flask, render_template, redirect, request
app = Flask(__name__)
bike_info = [
    
]

@app.route('/')
def index():
     return 'Hello'

@app.route('/bike')
def bike():
     return render_template('bike.html', bike_info = bike_info)

@app.route('/bike/new_bike', methods = ['GET','POST'])
def new_bike():
    if request.method == 'GET':
        return render_template("new_bike.html", bike_info = bike_info)
    elif request.method == 'POST':
        form = request.form
        new_bike = {
            'model': form['model'],
            'dailyfee': form['dailyfee'],
            'image':form['image'],
            'year':form['year'],
        }
    bike_info.append(new_bike)
    return redirect('/bike')
if __name__ == '__main__':
  app.run(debug=True)
 

