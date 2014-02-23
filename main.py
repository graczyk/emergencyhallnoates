from flask import Flask, request, redirect, url_for
import twilio.twiml
 
app = Flask(__name__)

@app.route('/play', methods=['POST'])
def play():
    resp = twilio.twiml.Response()
	
    # Based on the Digits we get in the Twilio POST, play the appropriate
    # song.
    if request.form['Digits'] == '1':
        song = "http://cs.uky.edu/~ntgr223/1.mp3"
    elif request.form['Digits'] == '2':
        song = "http://cs.uky.edu/~ntgr223/2.mp3"
    elif request.form['Digits'] == '3':
        song = "http://cs.uky.edu/~ntgr223/3.mp3"
    elif request.form['Digits'] == '4':
        song = "http://cs.uky.edu/~ntgr223/4.mp3"
    elif request.form['Digits'] == '5':
        song = "http://cs.uky.edu/~ntgr223/5.mp3"
    else:
        # If it is not a 1, 2, 3, or 4, indicate we don't understand
        # and play main menu
        resp.say("I'm sorry - I did not understand your request.")
        return str(resp)

    # Play the song we identified.
    resp.say("1 2 3 4.")
    resp.play(song)
    return str(resp)

  
@app.route('/', methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them.""" 
    resp = twilio.twiml.Response()
    # Greet the caller by name
    with resp.gather(action="/play") as g:
        g.say("Hello welcome to the Emergency Hall and Oates Phone Line")
        g.say("For You Make My Dreams, press 1.")
        g.say("For Rich Girl, press 2.")
        g.say("For Maneater, press 3.")
        g.say("For One on One, press 4.")
        g.say("For Private Eyes, press 5.")

    resp.pause(length="3")

    return str(resp)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
