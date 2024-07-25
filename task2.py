import openai
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.title('Shayeri Maker')

st.write('Enter some text:')

user_input = st.text_area('Your text here')

# Define the Anyscale endpoint token
ANYSCALE_ENDPOINT_TOKEN = os.environ["api_key"]

# Create an OpenAI client with the Anyscale base URL and API key
oai_client = openai.OpenAI(
    base_url="https://api.endpoints.anyscale.com/v1",
    api_key=os.environ["api_key"],
)

# Define the OpenAI model to be used for chat completions
model = "mistralai/Mistral-7B-Instruct-v0.1"

# Use the AnyScale model for chat completions
# Send a user message using the defined prompt
response = oai_client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "Generate shayari according to user input."},
        {"role": "user", "content": user_input}
    ],
)

# printing the response
if st.button('Generate Shayeri'):
    st.write('Here is your Shayeri:')
    st.write(response.choices[0].message.content)
