# LLM-based PDF Reading Assistant

[中文版文档](README-CN.md)

The PDF Reading Assistant is a reading assistant based on large language models (LLM), specifically designed to convert complex foreign literature into easy-to-read versions. Compared with traditional translation software, the PDF Reading Assistant has clear advantages.

## Product Features

- **Deep Understanding Based on LLM**: The PDF Reading Assistant uses the latest Large Language Models (LLM) technology for document translation and content generation, allowing for deeper semantic understanding and accurate translation.

- **Optimized Reading Experience**: The LLM can generate easy-to-read content, making complex foreign literature easier to understand, thereby optimizing the user's reading experience.
    - **Adjustable Generation Length**: Users can adjust parameters to customize the length of the generated content to satisfy different reading needs.
    - **Handling High-Density Information**: The PDF Reading Assistant can efficiently process the high-density information in the literature, appropriately extrapolate, and help readers better understand and absorb.

## Features

- [X] Use Large Language Models (LLMs) to translate and extrapolate high-density information papers and articles, support multiple languages.
- [X] Support for preserving the original layout and format of the source PDF.
- [X] Support for OpenAI models, and local models that have implemented the OpenAI interface, such as: ChatGLM2.
- [X] Modular and object-oriented design, easy to customize and extend.
- [X] A graphical user interface (GUI) based on streamlit in the browser, supports batch operations, can be deployed on the network.
- [ ] Package standalone programs that do not depend on the command line to start for windwos and macOS respectively.
- [ ] Improve translation quality by using custom trained translation models.
- [ ] Support customization for different reading levels or preferences to meet content generation needs at different levels.

## Effects
**Product iteration in progress, the effects section will be updated irregularly**

### Interactive Interface
![p-1](https://github.com/SUSTYuxiao/PdfTranslator/assets/25291804/08a2e6c5-ad27-44b8-a2d3-cc023ae26626)

### Comparison of Generated Results
<img width="929" alt="p-2" src="https://github.com/SUSTYuxiao/PdfTranslator/assets/25291804/a31ba05a-48a2-4e1b-968d-975de8713839">

## Environment
Any Python3 running environment

## Getting Started
1. Clone the repository and switch to the repository root directory.
2. Use `pip install -r requirements.txt` to install dependencies.
3. Run `streamlit run server.py`.

Enjoy it! 😊

## License

This project is licensed under GPL-3.0. For more details, please see the [LICENSE](LICENSE) file.