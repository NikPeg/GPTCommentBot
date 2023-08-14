from config import OPENAI_API_KEY
import openai
from tenacity import retry, wait_random_exponential, wait_fixed, stop_after_attempt
import re


class GPTProxy:
    def __init__(self, model="gpt-3.5-turbo"):
        openai.api_key = OPENAI_API_KEY
        self.model = model

    @staticmethod
    def delete_quotes(text):
        return re.sub(r'^"(.*)"$', '\\1', text)

    @retry(wait=wait_fixed(21), stop=stop_after_attempt(10))
    def ask(self, message):
        print(f"Asking GPT: {message}")
        try:
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": message}
                ]
            )

            answer = self.delete_quotes(completion.choices[0].message.content)
            print(f"GPT's answer: {answer}")
            return answer
        except Exception as e:
            print(e)
            raise e
