import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak something...")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    if str("Google") in text:
        print("Openning Google")
        url = "https://www.google.com.org"
        webbrowser.open(url)
    if str("YouTube") in text:
        print("Opening YouTube")
        url = "https://www.youtube.com"
        webbrowser.open(url)
    if str("WhatsApp") in text:
        print("Openning Whatsapp web")
        url = "https://web.whatsapp.com/"
        webbrowser.open(url)
    if str("Facebook") in text:
        print("Openning Facebook")
        url = "https://www.facebook.com/"
        webbrowser.open(url)
    if str("Instagram") in text:
        print("Openning Instagram")
        url = "https://www.instagram.com/"
        webbrowser.open(url)
    if str("Amazon") in text:
        print("Openning Amazon")
        url = "https://www.amazon.in/"
        webbrowser.open(url)
    if str("Flipkart") in text:
        print("Openning Flipkart")
        url = "https://www.flipkart.com/"
        webbrowser.open(url)
except sr.UnknownValueError:
    print("Speak something Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print("Please connect to network")

