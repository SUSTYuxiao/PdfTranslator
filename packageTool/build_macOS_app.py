import streamlit as st
import sys

sys.path.append('../packageTool')  # 添加其他目录到系统路径
import server  # 导入其他脚本

if __name__ == "__main__":
    server.main()