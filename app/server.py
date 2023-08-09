import streamlit as st
import yaml,os
import subprocess
from translator.doc_parser import DocParser
from translator import HtmlParser
from utils import ArgumentParser, ConfigLoader, LOG
from model import GLMModel, OpenAIModel

# 在streamlit应用的侧边栏中创建输入字段
config_file_name = st.sidebar.text_input('Config', 'GUI-config.yaml')
model_type = st.sidebar.selectbox('Model Type', ['GLMModel', 'OpenAIModel'])

current_dir = os.path.dirname(os.path.abspath(__file__))
config_dir = os.path.join(current_dir, 'config')
temp_dir = os.path.join(current_dir, 'temp')

data = {}
data['model_type_name'] = model_type

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

config_file_path = os.path.join(config_dir, config_file_name)

# 当用户点击"Save"按钮时，保存输入字段为yaml文件
if st.sidebar.button('Save'):
    with open(config_file_path, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


config_loader = ConfigLoader(config_file_path)

config = config_loader.load_config()

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

# 用户上传PDF文件
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
uploaded_file_path =  os.path.join(temp_dir, "upload_file_1.pdf")
uploaded_file_path_html =  os.path.join(temp_dir, "upload_file_1_html.html")
translated_file_path_html =  os.path.join(temp_dir, "translated_file_1_html.html")




if uploaded_file is not None:
    LOG.debug("上传文件路径")
    LOG.debug(uploaded_file_path)
    LOG.debug("html路径")
    LOG.debug(uploaded_file_path_html)
    LOG.debug("html处理结果路径")
    LOG.debug(translated_file_path_html)

    # 保存PDF文件
    with open(uploaded_file_path, 'wb') as out:
        out.write(uploaded_file.getvalue())

    docParser = DocParser(model)

    # 现在，你应该有一个名为'output.html'的HTML文件，它是由你的PDF文件转换而来的
    st.write("HTML file has been created.")
    
    docParser.doTrans(uploaded_file_path,translated_file_path_html )
    

