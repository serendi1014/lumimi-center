import streamlit as st
import pandas as pd
import random
import re
from datetime import datetime, timedelta

# 1. 구글 시트 연동 설정
SHEET_ID = "1zaERVga9_efXnpNL1mmXNdOrJ3syRctLt6hmeJjVgN8"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

def load_keywords():
    try:
        df = pd.read_csv(SHEET_URL)
        df['구분'] = df['구분'].astype(str).str.strip()
        df['키워드'] = df['키워드'].astype(str).str.strip()
        return df
    except:
        return pd.DataFrame({'구분': [], '키워드': []})

# 페이지 설정
st.set_page_config(page_title="루미미 전략 센터 v25.5", layout="wide")

# --- ✨ 루미미 프리미엄 CSS 테마 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
    * { font-family: 'Pretendard', sans-serif; }
    .main-title { font-size: 42px; font-weight: 900; background: linear-gradient(120deg, #2D63F7, #D63384); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; }
    .keyword-badge { background: #F0F4FF; color: #2D63F7; padding: 8px 16px; border-radius: 20px; font-weight: 700; margin: 5px; display: inline-block; border: 1px solid #E1E9FF; }
    .badge-wp { background: #FFF0F0; color: #FF4B4B; border: 1px solid #FFDCDC; font-weight: 900; }
    .wp-box { background: #FFF5F5; border: 1px solid #FFDCDC; padding: 20px; border-radius: 15px; margin-top: 10px; }
    .section-title { font-size: 22px; font-weight: 800; color: #333; margin-top: 35px; margin-bottom: 18px; border-left: 5px solid #2D63F7; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 LUMIMI Strategy Center</div>", unsafe_allow_html=True)

menu = st.sidebar.radio("📋 전략 보드 선택", ["📰 네이버 블로그 조립", "🔥 WP 황금 키워드 (고단가)", "📈 수익 추세 분석"])

# --- 공통 로직 함수 ---
def analyze_content(text):
    if not text: return "준비 중...", "info-style"
    is_info = any(word in text for word in ["지원", "복지", "수당", "신청", "정부", "정책", "자격", "공고"])
    return ("📘 정보형", "info-style") if is_info else ("🌸 감성형", "vibe-style")

def get_refined_kw(user_kw, text):
    if user_kw: return user_kw.strip()
    if not text: return "꿀팁"
    match = re.search(r'([가-힣]{2,8})\s*(지원|사업|공원|센터|비|정책)', text)
    if match: return match.group(1) + match.group(2)
    words = re.findall(r'[가-힣]{3,6}', text)
    return max(set(words), key=words.count) if words else "꿀팁"

# --- [메뉴 1] 네이버 블로그 조립기 (일상/유입 중심) ---
if menu == "📰 네이버 블로그 조립":
    st.markdown("<div class='section-title'>🕵️ 네이버 블로그 전용 조립기</div>", unsafe_allow_html=True)
    target_kw = st.text_input("💎 네이버 유입 키워드", placeholder="예: 화랑대 철도공원, 성수동 팝업")
    raw_data = st.text_area("📄 네이버용 본문 데이터", height=150)
    
    mode_name, mode_class = analyze_content(raw_data)
    if raw_data: st.markdown(f"<div class='mode-info {mode_class}'>네이버 모드: {mode_name}</div>", unsafe_allow_html=True)

    if st.button("✨ 네이버 최적화 설계도 생성"):
        main_kw = get_refined_kw(target_kw, raw_data)
        selected_ments = random.sample(["이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸", "N잡러 루미미가 분석해보니 🧐"], 2)
        prompt = f"너는 인플루언서 '루미미'야. [{main_kw}] 키워드를 제목 맨 앞에 박고 네이버 블로그 톤으로 써줘. 필수 멘트: {selected_ments}. 가독성 좋게 줄바꿈 많이 해줘."
        st.session_state['nb_prompt'] = prompt
        st.success(f"✅ 네이버용 설계도 완료!")

    if 'nb_prompt' in st.session_state:
        st.text_area("📋 클로드 전용 프롬프트", value=st.session_state['nb_prompt'], height=200)

# --- [메뉴 2] WP 황금 키워드 (고단가/워드프레스 전략) ---
elif menu == "🔥 WP 황금 키워드 (고단가)":
    st.markdown("<div class='section-title'>💰 워드프레스 수익형 황금 키워드</div>", unsafe_allow_html=True)
    df = load_keywords()
    
    col1, col2 = st.columns([1, 1.5])
    with col1:
        st.markdown("**📌 애드센스 고단가 리스트**")
        wp_kws = ["보험 비교", "대출 자격", "정부 지원금", "신용카드 추천", "법인 설립", "재테크 꿀팁"]
        for kw in wp_kws: st.markdown(f"<span class='keyword-badge badge-wp'>💎 {kw}</span>", unsafe_allow_html=True)
        if st.button("🔄 리스트 새로고침"): st.rerun()

    with col2:
        wp_target = st.selectbox("워드프레스 타겟 키워드", wp_kws + ["직접 입력"])
        if wp_target == "직접 입력": wp_target = st.text_input("WP 키워드 직접 입력")
        
        if st.button("🔥 WP 전문 설계도 뽑기"):
            st.markdown(f"<div class='wp-box'><b>🎯 [{wp_target}] WP 전략</b><br>구글 SEO 최적화, 표(Table) 포함, 전문 용어 사용.</div>", unsafe_allow_html=True)
            wp_prompt = f"너는 WP 수익형 블로거 '루미미'야. [{wp_target}] 주제로 구글 애드센스 고단가를 타겟팅한 전문 글을 써줘. 서론-본론-결론이 명확해야 하고 전문 지식을 표로 정리해줘."
            st.text_area("📋 WP 전용 프롬프트", value=wp_prompt, height=250)

# --- [메뉴 3] 수익 추세 분석 (7일 데이터 연동) ---
elif menu == "📈 수익 추세 분석":
    st.markdown("<div class='section-title'>📊 7일 수익 추세 및 다음 달 예측</div>", unsafe_allow_html=True)
    
    with st.expander("📅 최근 7일 수익 데이터 입력 ($)", expanded=True):
        rev_list = []
        cols = st.columns(7)
        for i in range(7):
            date_str = (datetime.now() - timedelta(days=7-i)).strftime('%m/%d')
            with cols[i]:
                rev = st.number_input(f"{date_str}", min_value=0.0, value=1.0, key=f"rev_{i}")
                rev_list.append(rev)
    
    if st.button("📈 추세 정밀 분석 시작"):
        avg_rev = sum(rev_list) / 7
        est_month = avg_rev * 30
        
        st.divider()
        m1, m2 = st.columns(2)
        m1.metric("7일 평균 수익", f"${avg_rev:.2f}")
        m2.metric("다음 달 예상 수익", f"${est_month:.2f}")

        # 면적 그래프 시각화
        chart_df = pd.DataFrame({
            '날짜': [(datetime.now() - timedelta(days=7-i)).strftime('%m/%d') for i in range(7)],
            '수익($)': rev_list
        }).set_index('날짜')
        st.area_chart(chart_df)
        
        if avg_rev >= 10.0:
            st.balloons()
            st.success("🎉 수익 추세가 아주 건강합니다! 루미미님, 이대로만 갑시다!")
