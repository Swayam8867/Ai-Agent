from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class DevAgent:
    def analyze_code(self, code):
        try:
            print("CALLING OPENAI...")

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": "Explain and fix this code:\n" + code}
                ]
            )

            print("RESPONSE RECEIVED")

            return response.choices[0].message.content

        except Exception as e:
            print("ERROR:", e)
            return "FAILED"