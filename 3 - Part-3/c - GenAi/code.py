from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explique o que é GenAI em uma frase simples"
)

print(response.output_text)