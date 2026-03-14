
import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="루미미 네이버 마스터 v64.1", layout="wide")

# --- ✨ 루미미 프리미엄 CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
    * { font-family: 'Pretendard', sans-serif; }
    .main-title { font-size: 42px; font-weight: 900; background: linear-gradient(120deg, #03C75A, #2DB400); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; }
    .section-box { background: white; padding: 25px; border-radius: 20px; border: 1px solid #EAEAEA; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌿 LUMIMI NAVER MASTER v64.1</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🏛️ 1. 정보성 (정부지원금/꿀팁)", "💰 2. 쇼핑커넥트 (리뷰 분석/수익)"])

# --- [Tab 1] 정보성 포스팅 (지침 절대 사수) ---
with tab1:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🏛️ 정보성 마스터 조립기")
    col1, col2 = st.columns(2)
    with col1: i_mk = st.text_input("💎 메인 키워드", placeholder="예: 에코마일리지", key="i_mk")
    with col2: i_sk = st.text_input("🔍 세부 키워드", placeholder="예: 신청방법", key="i_sk")
    i_style = st.selectbox("💬 화법 선택", ["가격 & 분위기 반전형", "품절 대란 유도형", "뒤늦은 깨달음 자극형", "감성 공감 힐링형", "전문가 권위 활용형"], key="i_style")
    i_data = st.text_area("📄 분석 데이터 입력", height=150, key="i_data")
    
    if st.button("✨ 정보성 2,500자 설계도 생성", use_container_width=True):
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        
        # ❗ 이 부분이 루미미님이 강조하신 그 지침 그대로입니다!
        i_prompt = f"""너는 대한민국 No.1 인플루언서 '루미미'야. 아래 [데이터]로 정보성 포스팅을 작성해줘.

[마스터 지침 - 전자책 전략 반영]
1. 제목: [{i_mk}] 포함 문장형 (슬래시/기호 금지).
2. 도입부: 5줄 이내 [{i_sk}] 검색 의도 해결하여 체류시간 확보.
3. 광고유도: 본문 중간 정보 전환 지점에 "아래 내용을 확인하기 전에 내 자격요건부터 체크해보면 훨씬 이해가 빨라요" 식의 앵커 멘트 필수 삽입.
4. 저품질방지: ** 기호나 별표(*) 절대 사용 금지. [📷 사진 위치: OOO 장면 직접 촬영본] 가이드를 6곳 이상 지정. 
5. 분량/톤: 공백 제외 2,500자 이상의 묵직한 고퀄리티 글로 작성. "{i_style}" 화법과 "{sel_m[0]}", "{sel_m[1]}" 멘트 사용.
6. 키워드: [{i_mk}]를 제목 맨 앞에 배치하고, 본문 내 키워드 반복은 7회 이내로 제한.

데이터: {i_data}"""
        st.text_area("📋 정보성 프롬프트", value=i_prompt, height=400)
    st.markdown("</div>", unsafe_allow_html=True)

# --- [Tab 2] 쇼핑커넥트 (리뷰 분석 전략) ---
with tab2:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 💰 쇼핑커넥트 수익 & 리뷰 분석기")
    col3, col4 = st.columns(2)
    with col3: s_mk = st.text_input("💎 제품명/메인 키워드", placeholder="예: 가성비 로봇청소기", key="s_mk")
    with col4: s_sk = st.text_input("🔍 세부/후킹 키워드", placeholder="예: 한달 사용후기", key="s_sk")
    s_style = st.selectbox("💬 화법 선택", ["가격 & 분위기 반전형", "품절 대란 유도형", "뒤늦은 깨달음 자극형", "감성 공감 힐링형", "전문가 권위 활용형"], key="s_style")
    s_data = st.text_area("📄 타사 리뷰 데이터 붙여넣기", placeholder="경쟁사 리뷰들을 복사해서 넣어주세요.", height=200, key="s_data")
    
    if st.button("✨ 리뷰 분석 기반 쇼핑 설계도 생성", use_container_width=True):
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        s_prompt = f"""너는 리뷰 전문 인플루언서 '루미미'야. 붙여넣은 [데이터] 속의 리뷰들을 정밀 분석해서 쇼핑커넥트형 포스팅을 써줘.

[마스터 지침 - 리뷰 분석 특화]
1. 제목: [{s_mk}] 포함 문장형 (슬래시/기호 금지).
2. 리뷰 분석 서사: 타사 리뷰에서 공통적으로 언급되는 '단점'을 먼저 언급하여 신뢰를 확보한 뒤, 이를 상쇄하는 제품의 강력한 장점과 가성비를 강조할 것.
3. 쇼핑전략: "저도 리뷰 보고 고민했는데 직접 써보니 {s_mk}만한 게 없더라고요. 최저가 겟은 필수!" 멘트 포함.
4. 저품질방지: ** 기호/별표 금지. 사진위치 6곳 지정. 2,500자 이상 고퀄리티 수다톤.
5. 화법: "{s_style}" 적용 및 "{sel_m[0]}", "{sel_m[1]}" 사용.

데이터: {s_data}"""
        st.text_area("📋 쇼핑커넥트 분석 프롬프트", value=s_prompt, height=400)
    st.markdown("</div>", unsafe_allow_html=True)
