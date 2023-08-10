# 基于LLM的PDF阅读助手

PDF阅读助手是一个基于大语言模型（LLM）的阅读助手，专门设计用于将格式复杂的外文文献转换为易于阅读的版本。与传统的翻译软件相比，PDF阅读助手具有明显的优势。

## 产品特点

- **基于LLM的深度理解**：PDF阅读助手使用最新的大语言模型（LLM）技术进行文档的翻译和内容生成，它能更深入地理解语义并准确翻译。

- **优化阅读体验**：LLM能生成易读的内容，使复杂的外文文献变得容易理解，从而优化用户的阅读体验。
    - **生成长度可调**：用户可以通过调整参数，定制生成的内容长度，满足不同阅读需求。
    - **处理高密度信息**：PDF阅读助手能高效处理文献中的高密度信息，适当引申，使读者更好地理解和吸收。
## 特性

- [X] 使用大型语言模型 (LLMs) 将高密度信息的论文、文章做翻译与引申，支持多语言
- [X] 对保留源 PDF 的原始布局和格式的支持。
- [X] 支持 OpenAI 模型，及实现了OpenAI接口的本地模型如:ChatGLM2。
- [X] 模块化和面向对象的设计，易于定制和扩展。
- [x] 基于streamlit的浏览器下图形交互界面 (GUI) , 支持批量操作，可网络部署
- [ ] 面向windwos、macOS分别打包不依赖命令行启动的单机程序
- [ ] 通过使用自定义训练的翻译模型来提高翻译质量。
- [ ] 支持不同的阅读水平或偏好的定制，以满足不同程度的内容生成需求

## 效果
**产品迭代中，不定期更新效果部分**

### 交互界面
![p-1](https://github.com/SUSTYuxiao/PdfTranslator/assets/25291804/08a2e6c5-ad27-44b8-a2d3-cc023ae26626)

### 生成结果对比
<img width="929" alt="p-2" src="https://github.com/SUSTYuxiao/PdfTranslator/assets/25291804/a31ba05a-48a2-4e1b-968d-975de8713839">

## 环境
任意Python3运行环境

## 开始使用
1. 克隆仓库并切换到仓库根目录
2. 使用 `pip install -r requirements.txt` 安装依赖项。
3. 运行 streamlit run server.py

Enjoy it！😊

## 许可证

该项目采用 GPL-3.0 许可证。有关详细信息，请查看 [LICENSE](LICENSE) 文件。
