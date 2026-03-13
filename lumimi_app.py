import streamlit as st
import pandas as pd
from datetime import datetime

# 1. 구글 시트 연결 설정 (루미미님이 주신 ID 적용)
SHEET_ID = "1zaERVga9_efXnpNL1mmXNdOrJ3syRctLt6hmeJjVgN8"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

# 데이터 불러오기 함수
def load_keywords():
    try:
        # 실시간으로 시트 데이터를 읽어옵니다
        df = pd.read_csv(SHEET_URL)
        return df
    except Exception as e:
        # 에러 발생 시 보여줄 기본 데이터
        return pd.DataFrame({
            '구분': ['오늘', '어제', '장기'],
            '키워드': ['시트 설정을 확인해주세요', '데이터를 불러올 수 없습니다', '공유 설정을 확인해주세요']
        })

# 페이지 설정
st.set_page_config(page_title="루미미 전략 센터 v14.0", layout="wide")

# CSS 디자인
st.markdown("""
    <style>
    .keyword-badge {
        background-color: #E1E9FF;
        color: #2D63F7;
        padding: 6px 14px;
        border-radius: 15px;
        font-weight: bold;
        margin-right: 10px;
        display: inline-block;
        margin-bottom: 12px;
        border: 1px solid #D0DFFF;
        font-size: 14px;
    }
    .main-title { font-size: 40px; font-weight: 900; color: #1E1E1E; }
    .section-title { font-size: 20px; font-weight: bold; margin-top: 20px; margin-bottom: 15px; color: #444; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 루미미 AI 콘텐츠 전략 센터 v14.0</div>", unsafe_allow_html=True)

# 사이드바 메뉴
menu = st.sidebar.radio("메뉴 선택", ["📰 블로그 완제품 조립", "🔥 오늘의 황금 키워드", "📈 수익 분석 및 전략"])

# --- 📰 탭 1: 블로그 완제품 조립 ---
if menu == "📰 블로그 완제품 조립":
    st.subheader("🕵️ 네이버 블로그 포스팅 완제품 조립기")
    raw_data = st.text_area("분석할 기사 본문이나 제품 상세 정보", height=250)
    
    col_btn1, col_btn2 = st.columns(2)
    if col_btn1.button("🌟 클릭 유도형 제목 5종 뽑기", use_container_width=True):
        if raw_data:
            st.code("제목 5종이 생성되었습니다...", language="markdown")
            
    if col_btn2.button("✨ 클로드 전용 2,000자 설계도 뽑기", use_container_width=True):
        if raw_data:
            final_prompt = f"너는 인플루언서 '루미미'야. 아래 데이터를 바탕으로 2,000자 이상 작성해줘.\n\n[데이터]:\n{raw_data}"
            st.session_state['prompt_result'] = final_prompt

    if 'prompt_result' in st.session_state:
        st.text_area("클로드 전용 명령어", value=st.session_state['prompt_result'], height=300)

# --- 🔥 탭 2: 오늘의 황금 키워드 (자동 연동) ---
elif menu == "🔥 오늘의 황금 키워드":
    st.subheader("💎 구글 시트 실시간 연동 황금 키워드")
    
    with st.spinner('최신 키워드를 불러오는 중...'):
        df = load_keywords()
    
    # 1. 오늘의 최신 키워드
    st.markdown("<div class='section-title'>📅 오늘의 최신 키워드 (20개)</div>", unsafe_allow_html=True)
    today_list = df[df['구분'] == '오늘']['키워드'].tolist()
    if today_list:
        for kw in today_list:
            st.markdown(f"<span class='keyword-badge'>{kw}</span>", unsafe_allow_html=True)
    else:
        st.write("오늘의 키워드가 아직 업데이트되지 않았습니다.")

    # 2. 어제 핫 키워드
    st.markdown("<div class='section-title'>⏪ 어제 핫 키워드 (10개)</div>", unsafe_allow_html=True)
    yesterday_list = df[df['구분'] == '어제']['키워드'].tolist()
    for kw in yesterday_list:
        st.markdown(f"<span class='keyword-badge' style='background-color: #F0F2F6; color: #555;'>{kw}</span>", unsafe_allow_html=True)

    # 3. 장기 생존 키워드
    st.markdown("<div class='section-title'>🌲 장기 생존 키워드 (5개)</div>", unsafe_allow_html=True)
    evergreen_list = df[df['구분'] == '장기']['키워드'].tolist()
    for kw in evergreen_list:
        st.markdown(f"<span class='keyword-badge' style='background-color: #FFF0F0; color: #FF4B4B;'>{kw}</span>", unsafe_allow_html=True)

    if st.button("🔄 키워드 새로고침"):
        st.rerun()


# --- 📈 탭 3: 수익 분석 및 전략 (기존 유지) ---
elif menu == "📈 수익 분석 및 전략":
    st.subheader("📊 애드센스 실적 입력 및 수익 진단")
    # ... (기존 루미미님 코드 그대로 유지)
    st.info("💡 실적을 입력하면 루미미 비서가 분석해 드립니다.")
    daily_revenue = st.number_input("어제 수익 ($)", min_value=0.0, step=0.1)
    daily_pv = st.number_input("어제 페이지뷰 (PV)", min_value=0, step=10)
    daily_ctr = st.number_input("어제 클릭률 (CTR %)", min_value=0.0, step=0.1)
    if st.button("🧐 진단받기"):
        st.success("분석 완료! 다음 포스팅은 고단가 키워드로 써보세요.")