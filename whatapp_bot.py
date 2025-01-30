import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI
import httpx
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Store the key in GitHub Actions, navigate to Settings > Secrets and Variables > Actions > New repository secret, name it OPENAI_API_KEY, and paste the key.
# Retrieve the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("API key not found. Make sure to set it in the environment.")

# Create a custom HTTP transport to disable SSL verification
class CustomTransport(httpx.HTTPTransport):
    def handle_request(self, request):
        return super().handle_request(request)

transport = CustomTransport(verify=False)

# Initialize OpenAI client with the API key and custom transport
client = OpenAI(api_key=openai_api_key, http_client=httpx.Client(transport=transport))
# client = OpenAI(api_key='<paste_your_openai_key_here>', http_client=httpx.Client(transport=transport))

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()
    logging.debug(f"Received message: {incoming_msg}")

    if incoming_msg:
        try:
            # Call OpenAI API with timeout parameter
            response = client.completions.create(
                model='gpt-3.5-turbo',
                prompt=incoming_msg,
                max_tokens=50,  # Adjust max_tokens as per your requirement
                timeout=30  # Set a reasonable timeout for the API call
            )
            reply = response.choices[0].text.strip()
            logging.debug(f"OpenAI response: {reply}")
            msg.body(reply)
        except Exception as e:
            error_message = f"Error: {str(e)}"
            msg.body("Error processing message.")
            logging.error(error_message)
    else:
        msg.body("Sorry, I didn't understand that.")

    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
