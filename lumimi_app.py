
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

elif menu == "📈 수익 분석 및 전략":
    st.subheader("📊 애드센스 수익 정밀 진단 & 처방전")
    st.info("💡 어제의 수치를 입력하면 루미미 비서가 수익화 전략을 제안합니다.")

    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1:
        daily_revenue = st.number_input("어제 수익 ($)", min_value=0.0, step=0.01, format="%.2f")
    with col_in2:
        daily_pv = st.number_input("어제 페이지뷰 (PV)", min_value=0, step=1)
    with col_in3:
        daily_ctr = st.number_input("어제 클릭률 (CTR %)", min_value=0.0, step=0.01, format="%.2f")

    if st.button("🧐 루미미 비서에게 진단받기", use_container_width=True):
        if daily_pv > 0:
            # 1. CPC(클릭당 단가) 역산
            clicks = daily_pv * (daily_ctr / 100)
            calculated_cpc = daily_revenue / clicks if clicks > 0 else 0
            
            st.divider()
            st.markdown("### 📝 루미미 비서의 실적 분석 보고서")
            
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric("추정 CPC (클릭당 단가)", f"${calculated_cpc:.2f}")
                st.metric("추정 클릭 수", f"{int(clicks)}회")
            
            # 2. 상황별 AI 맞춤 처방전 로직
            st.markdown("#### 🚀 오늘 당장 해야 할 수익화 처방")
            
            if daily_revenue == 0:
                st.warning("📍 아직 수익이 발생하지 않았어요! 일단 '장기 생존 키워드'로 검색 유입량을 늘리는 데 집중합시다.")
            elif calculated_cpc < 0.2:
                st.error("📍 **단가가 너무 낮아요!** 지금 쓰는 주제는 광고 단가가 낮습니다. '금융, 보험, 대출, 정부지원금' 같은 고단가 키워드로 주제를 전환하세요.")
            elif daily_ctr < 1.5:
                st.info("📍 **클릭률(CTR)이 아쉬워요!** 글 중간에 사진과 광고가 너무 겹치지 않는지 확인하고, 본문 중간에 '클릭을 유도하는 버튼형 링크'를 넣어보세요.")
            elif daily_pv < 100:
                st.info("📍 **유입량이 부족합니다!** 지금은 단가보다 '조회수'가 우선이에요. 네이버 블로그나 커뮤니티에 링크를 배포해서 외부 유입을 늘리세요.")
            else:
                st.success("✅ **훌륭합니다!** 현재 전략이 잘 먹히고 있어요. 동일한 카테고리의 글을 3개 더 작성해서 '전문성 점수'를 높이세요.")
            
            # 3. 구체적인 다음 행동 제안
            st.info(f"💡 **루미미를 위한 TIP:** 오늘 밤엔 황금 키워드 탭에 있는 **'2026 청년주택 더드림집+'** 키워드로 고단가 포스팅 어때요?")
        else:
            st.error("분석을 위해 최소한 페이지뷰(PV)는 입력해 주셔야 해요! 😂")
