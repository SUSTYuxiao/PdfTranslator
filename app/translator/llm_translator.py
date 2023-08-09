
from model import Model
from utils import LOG

class LlmTranslator:
    def __init__(self, model: Model):
        self.model = model
        self.contentN = []

    def translate_content(self, content: str, file_format: str = 'PDF', target_language: str = '中文'):

        prompt = self.model.translate_prompt(content, target_language)
        LOG.debug( f"当前翻译prompt={prompt}")
        translation, status = self.model.make_request(prompt)
        LOG.debug( f"当前翻译result={translation}")
        print(type(translation))
        return translation
        
