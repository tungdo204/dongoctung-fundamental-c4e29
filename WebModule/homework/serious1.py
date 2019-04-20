from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'

@app.route('/bmi/<int:w>/<int:h>')
def bmi(w,h):
    list_1=[]
    h_m=h/100
    BMI=w/(h_m**2)

    #1. Without :
    # if BMI<16:
    #     return("Severely underweight")
    # elif BMI <18.5:
    #     return("Underweight")
    # elif BMI <25:
    #     return("Normal")
    # elif BMI < 30:
    #     return("Overweight")
    # else:
    #     return("Obese")
    

    if BMI<16:
        list_1.append("Severely underweight")
    elif BMI <18.5:
        list_1.append("Underweight")
    elif BMI <25:
        list_1.append("Normal")
    elif BMI < 30:
        list_1.append("Overweight")
    else:
        list_1.append("Obese")

    return render_template('bmi.html', list_1 = list_1)

if __name__ == '__main__':
  app.run(debug=True)
 