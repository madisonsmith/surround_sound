from Pubnub import Pubnub
import control_audio

def call_audio(message):
        print(message)
        control_audio.play()
	
def send_sub():
	pubnub.subscribe({
		"channel": "play_song",
		"callback": call_audio})

if __name__ == "__main__":
	sub_key = "sub-c-dc6bc448-89af-11e3-baad-02ee2ddab7fe"
	pub_key = "pub-c-cc479bc5-bfa2-412c-826f-f8e05f702a03"
	print("Starting PubNub")
	pubnub = Pubnub(pub_key, sub_key)
	send_sub()
