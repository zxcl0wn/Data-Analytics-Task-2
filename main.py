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