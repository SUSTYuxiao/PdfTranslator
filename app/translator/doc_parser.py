
from translator.llm_translator import LlmTranslator
from model import Model
from utils import LOG
from pdf2docx import Converter

from docx import Document
from docx2pdf import convert



class DocParser:
    def __init__(self, model: Model):
        self.translator = LlmTranslator(model)

    def is_float(self,text):
        try:
            float(text)
            return True
        except ValueError:
            return False

    def process_text(self, text, target_language: str = '中文'):
        if text in ['\n', '']:
            return text
        if text.isnumeric() or self.is_float(text):
            return text
        translated_text = self.translator.translate_content([text], target_language)
        return translated_text



    def process_paragraph(self,paragraph):
        # 检查段落中的每一个运行元素
        for run in paragraph.runs:
            # 如果运行元素包含图片或数学公式，跳过这个段落
            if 'graphicData' in run._r.xml or 'oMathPara' in run._r.xml:
                return

        print("处理前", paragraph.text)
        # 处理段落的文本
        processed_text = self.process_text(paragraph.text)
        print("翻译结果", processed_text)
        # 清空原有的段落
        paragraph.clear()

        # 添加处理后的文本到原有段落
        paragraph.add_run(processed_text)
        print("处理后", paragraph.text)

    def doTrans(self,  pdf_input_path: str, work_path:str, target_language: str = '中文'):
        # 创建转换器对象
        cv = Converter(pdf_input_path)

        docx_file = "output3.docx"
        # 执行转换操作
        cv.convert(docx_file, start=0, end=None)

        # 关闭转换器，释放资源
        cv.close()


       # 打开文档
        doc = Document('output3.docx')

        # 遍历所有的段落
        for paragraph in doc.paragraphs:
            # 检查段落中的每一个运行元素
            for run in paragraph.runs:
                # 如果运行元素包含图片或数学公式，跳过这个段落
                if 'graphicData' in run._r.xml or 'oMathPara' in run._r.xml:
                    break
            else:  # 没有找到图片或数学公式
                # 处理段落的文本
                processed_text = self.process_text(paragraph.text)

                # 清空原有的段落
                paragraph.clear()

                # 添加处理后的文本到原有段落
                paragraph.add_run(processed_text)

        # 遍历所有的表格
        for table in doc.tables:
            # 遍历表格中的所有行
            for row in table.rows:
                # 遍历行中的所有单元格
                for cell in row.cells:
                    # 遍历单元格中的所有段落
                    for paragraph in cell.paragraphs:
                        self.process_paragraph(paragraph)

                    # 遍历单元格中的所有表格
                    for nested_table in cell.tables:
                        # 遍历嵌套表格中的所有行
                        for nested_row in nested_table.rows:
                            # 遍历行中的所有单元格
                            for nested_cell in nested_row.cells:
                                # 遍历单元格中的所有段落
                                for nested_paragraph in nested_cell.paragraphs:
                                    self.process_paragraph(nested_paragraph)

        # 保存修改后的文档
        doc.save('modified_example2.docx')

        # convert("modified_example2.docx", "output.pdf")
        print('处理完成！')



   

    