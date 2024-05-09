## Load Libraries
import os
import timeit
from openai import OpenAI

## Load Environment Variables
BASE_URL = os.getenv("BASE_URL", "http://localhost:8000/v1")
API_KEY = os.getenv("API_KEY", "DEFAULT")
MODEL = os.getenv("MODEL", "models/7B/llama-2-7b-chat.Q5_K_M.gguf")

## Create Client
client = OpenAI(base_url=BASE_URL, api_key=API_KEY)

## Make Request of LLAMA
start_time = timeit.default_timer()
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Tell me about the starter pokémon from the first generation of games.",
        },
    ],
    temperature=0.0,
    max_tokens=500,
)

## Print Response & Elapsed Time
print(response.choices[0].message.content)
elapsed = timeit.default_timer() - start_time

print(f"{elapsed=}")
