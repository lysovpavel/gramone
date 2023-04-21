import openai

from src.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


async def get_answer(question):
    completion = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{question}"}]
    )
    answer = completion['choices'][0]['message']['content']
    print(answer)
    return answer
