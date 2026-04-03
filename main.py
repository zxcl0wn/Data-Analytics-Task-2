from openai import OpenAI


client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1",
)

with open("news.csv", "r", encoding="utf-8") as f:
    text = f.read()

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input=f"Сделай краткое резюме каждой новости в формате 'Новость n':{text}\n\n"
)

result = response.output_text

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result)

print(response.output_text)