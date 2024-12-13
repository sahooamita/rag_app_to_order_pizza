from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

# Your Twilio account SID and auth token
# account_sid = ' '
account_sid = ' '
# auth_token = ' '
auth_token = ' '

# Create a Twilio client
client = Client(account_sid, auth_token)
from_number = '+12345622492'
# Retrieve all verified numbers
verified_numbers = client.incoming_phone_numbers.list()

# Print the verified numbers
for number in verified_numbers:
    print(number.phone_number)


# from twilio.rest import Client

# # Your Twilio account SID and auth token
# account_sid = 'ACf202c0346208a20a1bd0f8b9af011ba0'
# auth_token = '7460dd7507121ec60524a9eaff72021b'

# Create a Twilio client
client = Client(account_sid, auth_token)

# The phone number to call
# to_phone_number = '+16789019661' 
to_phone_number = '+ ' # mine
# to_phone_number = '+14086073003' # david

# The text to say during the call
text_to_say = 'Hello, this is a test call from Twilio.'

# Create a TwiML response
response = VoiceResponse()

# Create a TwiML response
# response = VoiceResponse()

# Add a say element to the response
# response.say('Hello, this is a test call from Twilio.')
response.play('./output/1_Hello this is a test.wav')
response.play('https://filebin.net/4bov8fw0tn7vsuek/1_Hi_what_is_the_weather.wav')
response.record(transcribe=True)
# Make the call
call = client.calls.create(
    twiml=str(response),
    to=to_phone_number,
    from_=from_number  # Your Twilio phone number
)

print(f"Call SID: {call.sid}")

# get the call from the other side as text
# import speech_recognition as sr
call_recordings = client.recordings.list(call_sid=call.sid)

for recording in call_recordings:
    print(f"Recording SID: {recording.sid}")

    # Fetch the transcriptions for the recording
    transcriptions = client.transcriptions.list(recording_sid=recording.sid)

    for transcription in transcriptions:
        print(f"Transcription text: {transcription.transcription_text}")



