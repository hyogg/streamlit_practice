# from dotenv import load_dotenv
# load_dotenv() # 파이썬이 환경변수 (.env) 불러와서 쓰게 됨
from langchain.chat_models import ChatOpenAI

import streamlit as st
chat_model = ChatOpenAI()
st.title('인공지능 시인과 대화하기')
content = st.text_input('짧은 시를 생성할 주제를 제시해주세요.')
if st.button('요청하기') :
    with st.spinner('생성 중입니다...'):
        result = chat_model.predict(content+'에 관한 20자짜리 시를 써줘.')
        st.write(result)