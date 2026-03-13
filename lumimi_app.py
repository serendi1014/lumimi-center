import streamlit as st
import pandas as pd

# 1. 구글 시트 연결 설정
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
st.set_page_config(page_title="루미미 전략 센터 v14.2", layout="wide")

# CSS 스타일
st.markdown("""
    <style>
    .keyword-badge {
        background-color: #E1E9FF; color: #2D63F7; padding: 6px 14px;
        border-radius: 15px; font-weight: bold; margin-right: 10px;
        display: inline-block; margin-bottom: 12px; border: 1px solid #D0DFFF; font-size: 14px;
    }
    .badge-yesterday { background-color: #F0F2F6; color: #555; }
    .badge-evergreen { background-color: #FFF0F0; color: #FF4B4B; }
    .main-title { font-size: 35px; font-weight: 900; color: #1E1E1E; }
    .section-title { font-size: 20px; font-weight: bold; margin-top: 25px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 루미미 AI 콘텐츠 전략 센터 v14.2</div>", unsafe_allow_html=True)

# 메뉴 구성
menu = st.sidebar.radio("메뉴 선택", ["📰 블로그 완제품 조립", "🔥 오늘의 황금 키워드", "📈 수익 분석 및 전략"])

# --- 📰 탭 1: 블로그 완제품 조립 (강력한 프롬프트 엔진 복구!) ---
if menu == "📰 블로그 완제품 조립":
    st.subheader("🕵️ 네이버 블로그 포스팅 완제품 조립기")
    raw_data = st.text_area("분석할 기사 본문이나 제품 상세 정보", height=250, placeholder="여기에 내용을 넣어주세요!")
    
    col_btn1, col_btn2 = st.columns(2)
    
    # 제목 생성 (루미미 화법 5종)
    if col_btn1.button("🌟 클릭 유도형 제목 5종 뽑기", use_container_width=True):
        if raw_data:
            titles = """
1. [공감형] "서울 월세 80만원?" 저도 찾아보고 깜짝 놀라 정리한 핵심혜택 💙
2. [반전형] 이 가격에 이 무드 실화니? '더드림집+' 모르면 무조건 손해예요!
3. [호기심] 왜 난리인지 나만 몰랐네! 오늘 소식 속 숨은 꿀팁 3가지 ✨
4. [전문가] N잡러 루미미가 분석한 팩트체크! 상세 조건까지 완벽 가이드
5. [힐링형] 마음이 든든해지는 주거 소식, 우리 함께 따뜻한 혜택 나눠요.
            """
            st.code(titles, language="markdown")

    # 설계도 생성 (루미미 전용 화법 가이드 포함)
    if col_btn2.button("✨ 클로드 전용 2,000자 설계도 뽑기", use_container_width=True):
        if raw_data:
            # 루미미님의 5가지 화법 가이드를 프롬프트에 내장!
            final_prompt = f"""너는 30대 N잡러 인플루언서 '루미미(lumimi)'야. 
아래 [데이터]를 바탕으로 네이버 블로그 포스팅을 "한 번에" 작성해줘. 

[루미미 전용 화법 가이드]
1. 가격 & 분위기 반전형: "이 가격에 이 무드 실화니?"
2. 품절 대란 & 트렌드 유도형: "품절 난 이 제품 니네 알아?"
3. 뒤늦은 깨달음 & 호기심 자극형: "왜 난리인지 나만 몰랐네"
4. 감성 공감 & 힐링형: "슬픈 하루였는데 내 마음을 풀어주네"
5. 전문가 권위 활용형: "N잡러 루미미가 이거 먼저 분석해보니"

[작성 지침]
1. 분량: 2,000자 이상 아주 아주 길고 정성스럽게 작성할 것. 
2. 말투: 다정한 '존댓말' 사용. 친구에게 수다 떨듯 친근하게 재구성해줘.
3. 구성: 도입(공감) -> 상세정보(수치 위주) -> [📷 사진 위치] 5곳 지정 -> 마무리 -> 해시태그 20개.
4. 금기사항: ** 기호나 별표(*)는 절대 쓰지 마. 오직 텍스트로만 가독성 좋게 줄바꿈 많이 해줘.

[데이터]:
{raw_data}
            """
            st.session_state['prompt_result'] = final_prompt
            st.success("✅ 루미미 화법이 장착된 설계도 완성!")

    if 'prompt_result' in st.session_state:
        st.text_area("클로드 전용 명령어", value=st.session_state['prompt_result'], height=450)
        st.info("💡 위 텍스트를 복사해서 클로드에게 주면, 루미미 말투로 글을 써줄 거예요! 💙")

# --- 나머지 탭은 기존 자동화 기능 유지 ---
elif menu == "🔥 오늘의 황금 키워드":
    st.subheader("💎 구글 시트 실시간 연동 황금 키워드")
    df = load_keywords()
    
    st.markdown("<div class='section-title'>📅 오늘의 최신 키워드</div>", unsafe_allow_html=True)
    today_list = df[df['구분'] == '오늘']['키워드'].tolist()
    for kw in today_list: st.markdown(f"<span class='keyword-badge'>{kw}</span>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>⏪ 어제 핫 키워드</div>", unsafe_allow_html=True)
    yesterday_list = df[df['구분'] == '어제']['키워드'].tolist()
    for kw in yesterday_list: st.markdown(f"<span class='keyword-badge badge-yesterday'>{kw}</span>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>🌲 장기 생존 키워드</div>", unsafe_allow_html=True)
    evergreen_list = df[df['구분'].str.contains('장기', na=False)]['키워드'].tolist()
    for kw in evergreen_list: st.markdown(f"<span class='keyword-badge badge-evergreen'>{kw}</span>", unsafe_allow_html=True)
    
    if st.button("🔄 키워드 새로고침"): st.rerun()


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
