from flask import Flask, render_template, redirect
app = Flask(__name__)

info = {
    'Name':'Do Ngoc Tung',
    'Work':'Bank',
    'School':'UC',
    'Hobby':'Music',
}

@app.route('/')
def index():
    return render_template('link.html')

@app.route('/about-me')
def aboutme():
    return render_template('info.html', info = info )

@app.route('/school')
def school():
    return redirect("http://techkids.vn ")

if __name__ == '__main__':
  app.run(debug=True)
 