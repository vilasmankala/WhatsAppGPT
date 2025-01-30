# WhatsAppGPT
A WhatsApp chatbot leveraging the OpenAI API for automated responses.
This guide explains how to integrate a WhatsApp chatbot using Twilio, Flask, and OpenAI GPT-3.5-Turbo. Follow the steps below to set up your chatbot.

# Prerequisites:
1. Twilio Account: Sign up at [Twilio](https://console.twilio.com/) to send and receive WhatsApp messages.
2. Ngrok Account: Sign up at [Ngrok](https://dashboard.ngrok.com/login) to expose your local app to the internet securely.
3. Python Installed: Ensure Python 3.x is installed to run the application.
4. Required Libraries: Install Flask (web framework), Twilio (communication API), OpenAI (GPT integration), and Ngrok (local tunneling).

# Steps to Implement
**Step 1:** Setup Accounts
**Twilio:**
1. Log in to your [Twilio Console](https://console.twilio.com/).
Navigate to Try it Out > Send a WhatsApp Message.
2. Link your WhatsApp number:
Scan the QR code shown in the Twilio Sandbox.
Your WhatsApp number is now linked to the Twilio Sandbox.

**Ngrok:**
1. Log in to your [Ngrok Dashboard](https://dashboard.ngrok.com).
2. Go to Your Authtoken and copy the token.
3. In your terminal, authenticate Ngrok:
$ ngrok authtoken <paste_copied_token>

**Step 2:** Set Up and Run the Application
1. Install required libraries:
$ pip3 install Flask twilio openai ngrok
2. Save the Python script provided above as app.py.
3. Run the application locally:
$ python3 app.py
4. The app will start on port 5000 with the URL:
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
5. In another terminal, start Ngrok:
ngrok http 5000
Ngrok will forward http://127.0.0.1:5000/ to a public URL like:
[https://<unique_id>.ngrok-free.app/whatsapp](https://<unique_id>.ngrok-free.app/whatsapp)

**Step 3:** Configure Twilio Webhook
1. In your Twilio Console, navigate to: Try it Out > Send a WhatsApp Message > Sandbox Settings.
2. Set When a message comes in to the Ngrok URL:
[https://<unique_id>.ngrok-free.app/whatsapp](https://<unique_id>.ngrok-free.app/whatsapp)
Select Method: **POST**, and save the changes.
