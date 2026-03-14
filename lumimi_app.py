
import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="루미미 네이버 마스터 v64.2", layout="wide")

# --- ✨ 루미미 프리미엄 CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
    * { font-family: 'Pretendard', sans-serif; }
    .main-title { font-size: 42px; font-weight: 900; background: linear-gradient(120deg, #03C75A, #2DB400); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; }
    .section-box { background: white; padding: 25px; border-radius: 20px; border: 1px solid #EAEAEA; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌿 LUMIMI NAVER MASTER v64.2</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🏛️ 1. 정보성 (정부지원금/꿀팁)", "💰 2. 쇼핑커넥트 (리뷰 분석/수익)"])

# --- [Tab 1] 정보성 포스팅 (제목 6종 + 지침 완벽 복구) ---
with tab1:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🏛️ 정보성 마스터 조립기")
    col1, col2 = st.columns(2)
    with col1: i_mk = st.text_input("💎 메인 키워드", placeholder="예: 에코마일리지", key="i_mk")
    with col2: i_sk = st.text_input("🔍 세부 키워드", placeholder="예: 신청방법", key="i_sk")
    i_style = st.selectbox("💬 화법 선택", ["가격 & 분위기 반전형", "품절 대란 유도형", "뒤늦은 깨달음 자극형", "감성 공감 힐링형", "전문가 권위 활용형"], key="i_style")
    i_data = st.text_area("📄 분석 데이터 입력", height=150, key="i_data")
    
    c1, c2 = st.columns(2)
    
    # 💡 [정보성 전용 제목 6종 버튼 복구]
    if c1.button("🌟 정보성 제목 6종 추천", use_container_width=True):
        m = i_mk if i_mk else "꿀팁"; s = i_sk if i_sk else ""
        st.code(f"""[상위노출 검색형 - 자연스러운 문장 중심]
1. 2026 {m} {s} 직접 신청해보고 정리한 가장 쉬운 방법
2. {m} {s} 자격 조건 대상자라면 필독해야 할 체크리스트
3. {m} 정보 찾는다면? {s}까지 한 번에 해결하는 정석 가이드

[홈피드 후킹형 - 루미미 감성 중심]
1. 루미미가 {m} 직접 써보니 {s} 부분에서 소름 돋았던 이유 ✨
2. 솔직히 {m} {s} 모르면 나만 손해 보는 느낌이라 공유해요 🤐
3. {m} 혜택이 이정도? {s}까지 실속 있게 챙기는 꿀팁 공개 🔥""", language="markdown")
    
    if c2.button("✨ 정보성 2,500자 설계도 생성", use_container_width=True):
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        i_prompt = f"""너는 대한민국 No.1 인플루언서 '루미미'야. 아래 [데이터]로 정보성 포스팅을 작성해줘.
[마스터 지침]
1. 제목: [{i_mk}] 포함 문장형 (슬래시/기호 금지).
2. 도입부: 5줄 이내 [{i_sk}] 검색 의도 해결.
3. 광고유도: 본문 중간 광고 클릭 유도 앵커 멘트 필수 삽입.
4. 저품질방지: ** 기호/별표 금지. 사진위치 6곳 지정. 2,500자 이상 수다톤.
5. 화법: "{i_style}" 적용 및 "{sel_m[0]}", "{sel_m[1]}" 사용.
데이터: {i_data}"""
        st.text_area("📋 정보성 프롬프트", value=i_prompt, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

# --- [Tab 2] 쇼핑커넥트 (리뷰 분석 전략 유지) ---
with tab2:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 💰 쇼핑커넥트 수익 & 리뷰 분석기")
    col3, col4 = st.columns(2)
    with col3: s_mk = st.text_input("💎 제품명/메인 키워드", placeholder="예: 가성비 로봇청소기", key="s_mk")
    with col4: s_sk = st.text_input("🔍 세부/후킹 키워드", placeholder="예: 한달 사용후기", key="s_sk")
    s_style = st.selectbox("💬 화법 선택", ["가격 & 분위기 반전형", "품절 대란 유도형", "뒤늦은 깨달음 자극형", "감성 공감 힐링형", "전문가 권위 활용형"], key="s_style")
    s_data = st.text_area("📄 리뷰 데이터 분석 입력", height=150, key="s_data")
    
    sc1, sc2 = st.columns(2)
    if sc1.button("🌟 쇼핑커넥트 제목 6종 추천", use_container_width=True):
        sm = s_mk if s_mk else "꿀템"; ss = s_sk if s_sk else ""
        st.code(f"[상위노출형]\n1. {sm} {ss} 내돈내산 3개월 사용후기와 장단점 비교\n2. 가성비 끝판왕 {sm}, {ss} 정보까지 꼼꼼하게 따져봤어요\n\n[후킹형]\n1. 왜 난리인지 나만 몰랐네! {sm} {ss} 직접 써보고 정착한 템 🤐\n2. 이 가격에 이 무드 실화니? {sm} {ss} 고민하는 분들만 보세요 ✨", language="markdown")
    
    if sc2.button("✨ 리뷰 분석 기반 쇼핑 설계도 생성", use_container_width=True):
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        s_prompt = f"""너는 리뷰 전문 인플루언서 '루미미'야. [데이터] 속 리뷰를 분석해서 쇼핑커넥트형 포스팅을 써줘.
[마스터 지침]
1. 제목: [{s_mk}] 포함 문장형 (슬래시/기호 금지).
2. 서사: 타사 리뷰 단점 분석 후 루미미만의 장점으로 전환.
3. 수익: 품절 유도 멘트 포함.
4. 저품질방지: ** 기호/별표 금지. 사진위치 6곳 지정. 2,500자 이상.
5. 화법: "{s_style}" 적용 및 "{sel_m[0]}", "{sel_m[1]}" 사용.
데이터: {s_data}"""
        st.text_area("📋 쇼핑커넥트 프롬프트", value=s_prompt, height=400)
    st.markdown("</div>", unsafe_allow_html=True)
