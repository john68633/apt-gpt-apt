import streamlit as st
from utils.gpt_engine import ask_gpt
from pathlib import Path

st.title("🏠 아파트 가치 평가 프로그램")
st.markdown("Streamlit + GPT 기반 부동산 분석 SaaS")

version = st.selectbox("분석 버전 선택", ["v1"])
apt_name = st.text_input("단지명", "힐스테이트 태전")
area = st.text_input("전용면적(㎡)", "84")
price = st.text_input("매매가 (예: 6억 5천)", "6억 5천")

if st.button("분석 시작"):
    prompt_path = Path(f"prompts/{version}_prompt.txt")
    template = prompt_path.read_text(encoding="utf-8")
    prompt = template.replace("{apt_name}", apt_name).replace("{area}", area).replace("{price}", price)
    response = ask_gpt(prompt)
    st.markdown(response)
