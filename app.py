from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# 환경 변수 로드
load_dotenv()

# Google Generative AI 설정
genai.configure(api_key=os.getenv("AIzaSyAy8q7xSZ8Z6o3q10leBjnobz1NGgm5i_g"))

# Streamlit 설정
st.set_page_config(page_title="DiSC Chatbot", page_icon="🤖")

st.header("DiSC Personality Chatbot")

# DiSC 데이터 정의
disc_data = {
    "D": {
        "description": "Dominance - Results-oriented, direct, and decisive.",
        "matches": ["I", "C"],
        "conflicts": ["D"]
    },
    "I": {
        "description": "Influence - Enthusiastic, outgoing, and sociable.",
        "matches": ["D", "S"],
        "conflicts": ["I"]
    },
    "S": {
        "description": "Steadiness - Calm, patient, and supportive.",
        "matches": ["I", "C"],
        "conflicts": ["D"]
    },
    "C": {
        "description": "Conscientiousness - Analytical, detail-oriented, and reserved.",
        "matches": ["S", "D"],
        "conflicts": ["I"]
    }
}

# 사용자 질문 입력
st.subheader("Ask a Question about DiSC!")
user_question = st.text_input("Ask anything about DiSC types, compatibility, or personal traits:")

# AI 기반 응답 생성
if user_question:
    # AI 프롬프트 생성
    base_prompt = """
    You are an expert in DiSC personality typing. Analyze the following question and provide an accurate and insightful response.
    Be specific, reference personality traits, and suggest compatibility or strategies where necessary.
    
    DiSC data to use:
    - D: Dominance. Matches: I, C. Conflicts: D.
    - I: Influence. Matches: D, S. Conflicts: I.
    - S: Steadiness. Matches: I, C. Conflicts: D.
    - C: Conscientiousness. Matches: S, D. Conflicts: I.
    
    Question:
    """
    prompt = base_prompt + f"\n{user_question}\n"

    # 모델 호출
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content([prompt])
        st.subheader("AI Response:")
        st.write(response.text)
    except Exception as e:
        st.error("Error generating response. Please try again later.")
        st.error(f"Details: {e}")
