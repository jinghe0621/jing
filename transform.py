import streamlit as st  
from litellm import completion  # 确保已经安装了litellm库  
  
# Streamlit 应用程序界面  
st.title('中英文翻译应用')  
  
# 用户输入中文文本  
input_text = st.text_input('请输入中文文本', '')  
  
# 当用户点击按钮后,进行翻译并显示结果  
if st.button('翻译为英文'):  # 注意这里添加了空格  
    if input_text:  
        # 使用 LiteLLM 调用 Deepseek 模型进行翻译  
        # 注意：这里的 model 和参数可能需要根据实际情况调整  
        response = completion(model='deepseek/deepseek-chat',  
                              messages=[  
                                  {"content": "你是一个优秀的英文翻译,\n请根据用户输入和英文读者的阅读习惯,\n把内容原原本本翻译成对应的英文",  
                                   "role": "system"},  
                                  {"content": input_text,  
                                   "role": "user"}  
                              ])  
  
        # 注意：这里假设 response 的结构是符合预期的，但实际情况可能不同  
        try:  
            translated_text = response['choices'][0]['message']['content']  
            st.write('英文翻译结果:', translated_text)  
        except (KeyError, IndexError):  
            st.error('翻译过程中出现错误，请检查输入或模型是否可用。')  
    else:  
        st.write('请输入中文文本后再进行翻译')
