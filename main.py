from flask import *
app=Flask(__name__)
@app.route('/',)

def getIndex():
  return "<a href='/about'><h1>About</h1></a> <a href='/contact'><h1>Contacts</h1></a> <a href='/home'><h1>Home</h1></a> <p>teksts teksts teksts teksts teksts teksts teksts teksts teksts </p>"

@app.route('/about')
def getAbout():
  return render_template('about.html')

@app.route('/home')
def getHome():
  return render_template('home.html', phone= 12341234)

@app.route('/contact')
def getContact():
  return render_template('contact.html', phone= 12341234)

if __name__ == '__main__':
  app.run(host="0.0.0.0", threaded=True, port=5000, debug=True)
