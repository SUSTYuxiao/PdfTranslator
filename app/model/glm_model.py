import openai
import requests
import simplejson
import time
from model import Model
from utils import LOG

class GLMModel(Model):
    def __init__(self, model_url: str):
        self.model = "chatglm2-6b"
        openai.api_base = model_url
        openai.api_key = "none"

    def make_request(self, prompt):
        attempts = 0
        while attempts < 3:
            try:
                if self.model == "chatglm2-6b":
                    response = openai.ChatCompletion.create(
                        model=self.model,
                        messages=[
                            {"role":"system","content": Model.MODEL_ROLE_TRANSLATE_PROMPT},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    translation = response.choices[0].message['content'].strip()
                else:
                    response = openai.Completion.create(
                        model=self.model,
                        prompt=prompt,
                        max_tokens=150,
                        temperature=0
                    )
                    translation = response.choices[0].text.strip()

                return translation, True
            except openai.error.RateLimitError:
                attempts += 1
                if attempts < 3:
                    LOG.warning("Rate limit reached. Waiting for 60 seconds before retrying.")
                    time.sleep(60)
                else:
                    raise Exception("Rate limit reached. Maximum attempts exceeded.")
            except requests.exceptions.RequestException as e:
                raise Exception(f"请求异常：{e}")
            except requests.exceptions.Timeout as e:
                raise Exception(f"请求超时：{e}")
            except simplejson.errors.JSONDecodeError as e:
                raise Exception("Error: response is not valid JSON format.")
            except Exception as e:
                raise Exception(f"发生了未知错误：{e}")
        return "", False
