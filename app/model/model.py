# from book import ContentType

class Model:
    MODEL_ROLE_TRANSLATE_PROMPT = '你是一个翻译引擎，你只可以翻译文本，不要解释。另外，对于姓名、地址、超链接、公式、论文的引用等内容可以不用翻译直接返回原文'
    MODEL_ROLE_TRANSLATE_PROMPT_plus =  MODEL_ROLE_TRANSLATE_PROMPT + '但是，对于较长的段落和句子，除了翻译外可以适当引申。'
   
    def make_text_prompt(self, text: str, target_language: str) -> str:
        return f"将目标文本翻译为{target_language}，不要做过多解释，目标文本内容是：{text}。如果部分内容已经是{target_language}，不需要翻译对应内容"

    def make_table_prompt(self, table: str, target_language: str) -> str:
        return f"翻译为{target_language}，保持间距（空格，分隔符），以表格形式返回：\n{table}"

    def translate_prompt(self, content, target_language: str) -> str:
        return self.make_text_prompt(content, target_language)
        # if content.content_type == ContentType.TEXT:
        #     return self.make_text_prompt(content.original, target_language)
        # elif content.content_type == ContentType.TABLE:
        #     return self.make_table_prompt(content.get_original_as_str(), target_language)

    def make_request(self, prompt):
        raise NotImplementedError("子类必须实现 make_request 方法")
