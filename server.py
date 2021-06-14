from flask import Flask, render_template,session,redirect
app = Flask(__name__)

app.secret_key = "Secret keeping it Not worth it"
@app.route('/')
def index():
    if "counter" in session.keys():
        session["counter"] += 1
    else:
        session["counter"] = 1
    return render_template('index.html', counter=session["counter"])

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__ == '__main__':
  app.run(debug=True)
 