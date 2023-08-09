import openai
import requests
import simplejson
import time

from model import Model
from utils import LOG

class OpenAIModel(Model):
    def __init__(self, model: str, api_key: str, api_base: str = 'https://openai.api2d.net'):
        self.model = model
        openai.api_key = api_key
        openai.api_base = api_base

    def make_request(self, prompt):
        attempts = 0
        while attempts < 3:
            try:
                if self.model == "gpt-3.5-turbo":
                    response = openai.ChatCompletion.create(
                        model=self.model,
                        messages=[
                            {"role":"system","content":"你是一个翻译专家，不要对单词或文本有太多展开的解释，而是直接返回翻译的结果,比如如果问题是‘apple’，那返回内容应该是‘苹果’。另外如果原文是无意义的或包含代码，请直接返回原文"},
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
