from flask import Flask, request, render_template

from Pubnub import Pubnub

sub_key = "sub-c-dc6bc448-89af-11e3-baad-02ee2ddab7fe"
pub_key = "pub-c-cc479bc5-bfa2-412c-826f-f8e05f702a03"
pubnub = Pubnub(pub_key, sub_key)

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("hi.html")

@app.route("/play")	
def request_audio():
	if request.method == "GET":
		#Publish the request
		pubnub.publish({
			"channel": "play_song",
			"message": "kpdarkhorse.mp3"})
	return "response"


if __name__ == "__main__":
	#Start server with ip the same as the local host
	app.run(debug=True, host="0.0.0.0")
