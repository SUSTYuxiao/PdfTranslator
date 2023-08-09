import streamlit as st
import yaml,os
from translator.progress import Progress
from translator.doc_parser import DocParser
from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel

# 在streamlit应用的侧边栏中创建输入字段

# config_file_name = st.sidebar.text_input('Config', 'GUI-config.yaml')
data = {}

def store_config( data: dict):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_name = 'GUI-config.yaml'
    config_dir = os.path.join(current_dir, 'config')
    config_file_path = os.path.join(config_dir, config_file_name)
    os.makedirs(os.path.dirname(config_file_path), exist_ok=True)
    with open(config_file_path, 'w+') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
    return config_file_path

def make_sidebar():
    model_type = st.sidebar.selectbox('Model Type', ['GLMModel', 'OpenAIModel'])
    # 根据model_type的值显示或隐藏特定的输入字段
    if model_type == 'GLMModel':
        glm_model_url = st.sidebar.text_input('GLM Model URL', 'http://localhost:8000/v1')
        timeout = st.sidebar.number_input('Timeout', min_value=1, max_value=1000, value=500)
        data[model_type] = {
            'model_url': glm_model_url,
            'timeout': timeout,
        }
    else:
        openai_model = st.sidebar.text_input('OpenAI Model', '')
        openai_api_key = st.sidebar.text_input('OpenAI API Key', '')
        api_base = st.sidebar.text_input('OpenAI API base url', '')
        
        data[model_type] = {
            'model': openai_model,
            'api_key': openai_api_key,
            'api_base': api_base,
        }
    data['model_type_name'] = model_type
    
    processPageNum = st.sidebar.number_input('页面数限制（预览用）, 0表示无限', 0)
    data['processPageNum'] = processPageNum
    target_language = st.sidebar.text_input('目标语言', "中文")
    data['target_language'] = target_language
    return data

def getModel(config):
    model_type_name = config['model_type_name'] if 'model_type_name' in config else ''

    if model_type_name == 'OpenAIModel':
        model_name = config['OpenAIModel']['model']
        api_key = config['OpenAIModel']['api_key']
        api_base = config['OpenAIModel']['api_base']
        model = OpenAIModel(model=model_name, api_key=api_key, api_base = api_base)  
    else:
        model_url =  config['GLMModel']['model_url']
        # timeout = args.timeout if args.timeout else config['GLMModel']['timeout']
        model = GLMModel(model_url=model_url)
    return model

config_data = make_sidebar()
config_file_path = store_config(config_data)
file_exists = os.path.isfile(config_file_path)

if not file_exists:
    st.sidebar.warning("请到侧边栏先初始化配置")
else:
    # 选择要上传的文件列表
    uploaded_files = st.file_uploader("选择一个或多个PDF文件", type="pdf", accept_multiple_files=True, help='1234')
    cur_task_text = st.empty() 
    progress_text = st.empty() 
    progress_bar = st.progress(0)
    progress = Progress(progress_bar, progress_text)
    temp_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp')
    
    config_loader = ConfigLoader(config_file_path)
    config = config_loader.load_config()
    LOG.info(config)
    model = getModel(config)
    processPageNum =  config['processPageNum']
    target_language =  config['target_language']


    # 处理上传的文件
    if uploaded_files is not None:
        for index, uploaded_file in enumerate(uploaded_files):
            file_name = uploaded_file.name
            uploaded_file_path = os.path.join(temp_dir, file_name)
            os.makedirs(os.path.dirname(uploaded_file_path), exist_ok=True)
            # 保存PDF文件
            with open(uploaded_file_path, 'wb') as out:
                out.write(uploaded_file.getvalue())

            # 处理PDF文件
            cur_task_text.text(f'正在处理第{index+1}个文件：{file_name}')
            result_docx_file_path= os.path.join(temp_dir, file_name+"_result"+".docx")
            # 如果服务器缓存，则跳过
            if not os.path.isfile(result_docx_file_path):
                docParser = DocParser(model, progress, target_language)
                docParser.doTrans(
                    file_name = file_name
                    ,pdf_input_path=uploaded_file_path
                    ,result_docx_file_path = result_docx_file_path
                    , temp_source_path=temp_dir
                    , endPos=processPageNum
                    )
                # 生成下载链接
                if  os.path.isfile(result_docx_file_path):
                    with open(result_docx_file_path, 'rb') as f:
                        st.download_button(
                            label=f"点击下载{file_name}翻译后的文件",
                            data=f,
                            file_name=os.path.basename(result_docx_file_path),
                            mime='application/octet-stream'
                        )
                    # 删除临时文件
                    # os.remove(result_docx_file_path)

            









    

