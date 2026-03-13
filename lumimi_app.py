
import streamlit as st
import pandas as pd
import random

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

st.set_page_config(page_title="루미미 전략 센터 v16.5", layout="wide")

st.markdown("""
    <style>
    .keyword-badge { background-color: #E1E9FF; color: #2D63F7; padding: 6px 14px; border-radius: 15px; font-weight: bold; margin-right: 10px; display: inline-block; margin-bottom: 12px; border: 1px solid #D0DFFF; font-size: 14px; }
    .badge-evergreen { background-color: #FFF0F0; color: #FF4B4B; }
    .main-title { font-size: 35px; font-weight: 900; color: #1E1E1E; }
    .sub-info { background-color: #F8F9FA; padding: 15px; border-radius: 10px; border-left: 5px solid #2D63F7; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 루미미 AI 전략 센터 v16.5</div>", unsafe_allow_html=True)

menu = st.sidebar.radio("메뉴 선택", ["📰 블로그 완제품 조립", "🔥 오늘의 황금 키워드", "📈 수익 분석 및 전략"])

if menu == "📰 블로그 완제품 조립":
    st.subheader("🕵️ 네이버 블로그 MZ 스마트 조립기")
    raw_data = st.text_area("기사 본문이나 상세 정보 입력", height=200, placeholder="여기에 내용을 넣어주세요!")
    
    # 힙한 멘트 데이터베이스
    mz_ment_db = [
        "진심 폼 미쳤다..", "이거 안 가면 유죄임 (진지)", "완전 갓벽 그 자체 ✨", "비주얼 무엇? 실물 깡패임", 
        "현생 탈출 지대로 하고 옴 ☁️", "진짜 나만 알고 싶었는데.. 특별히 공개!", "이 분위기 어쩔 거야.. 감성 터짐 🔥",
        "여기 완전 사진 맛집인 거 다들 알지?", "진심 내돈내산 찐 후기임!", "이거 모르면 진짜 손해라구 🤐"
    ]

    col_btn1, col_btn2 = st.columns(2)
    
   # --- 1. [v16.7] 더블 타겟 제목 생성 (SEO vs 후킹) ---
    if col_btn1.button("🌟 [전략적] 제목 6종 생성", use_container_width=True):
        if raw_data:
            # 키워드 추출
            keyword = raw_data[:10].replace(" ", "").strip()
            
            titles = f"""
### 📈 [SEO 상위노출형] - 검색 유입 타겟
1. {keyword} 가는법 예약 주차 및 봄나들이 명소 총정리 (2026 최신)
2. 서울 아이와 가볼만한곳 {keyword} 체험 및 레스토랑 이용 꿀팁
3. {keyword} 방문 전 필수 체크리스트! 입장료부터 주변 맛집까지

### 🔥 [홈판/피드 후킹형] - 클릭 유도 타겟
1. 와.. 서울에 이런 곳이 있었다고? "{keyword}" 분위기 폼 미쳤다.. 🔥
2. 제 친동생한테만 알려주려다 공개함🤐 "{keyword}" 안 가면 유죄임 (진심)
3. 갓생 살기 딱 좋은 "{keyword}" 무드 실화냐? 📸✨ (광고아님)
            """
            st.code(titles, language="markdown")

    # --- 2. 스마트 랜덤 설계도 & 힙한 멘트 추천 ---
    if col_btn2.button("✨ [MZ특화] 랜덤 설계도 뽑기", use_container_width=True):
        if raw_data:
            # 주제 감지 (나들이 vs 정보)
            is_place = any(word in raw_data for word in ["공원", "역", "여행", "카페", "나들이", "기차"])
            
            # 화법 선택
            vibe_db = ["공감형", "팩트형", "반전/감탄형", "비밀 공유형", "뒤늦은 깨달음", "지인 추천형", "감성 힐링형"]
            selected_vibes = random.sample(vibe_db, 3)
            # 힙한 멘트 3개 추천
            selected_mz_ments = random.sample(mz_ment_db, 3)
            
            final_prompt = f"""너는 30대 N잡러 인플루언서 '루미미'야. 
[데이터]를 분석해서 네이버 블로그 글을 써줘. 

[오늘의 루미미 Vibe 조합]
- 화법: {', '.join(selected_vibes)}
- 힙한 멘트 (본문에 자연스럽게 섞어줘): 
  1. "{selected_mz_ments[0]}"
  2. "{selected_mz_ments[1]}"
  3. "{selected_mz_ments[2]}"

[작성 지침]
- 도입부는 5줄 이내로 임팩트 있게 시작할 것.
- 추천된 힙한 멘트들을 문맥에 맞게 한 번씩 툭툭 던지듯 넣어줘. (MZ느낌 뿜뿜!)
- 기사 내용의 핵심 팩트는 놓치지 말고 포함할 것.
- 사진 위치 5곳 지정, ** 기호 절대 금지, 해시태그 20개.

[데이터]: {raw_data}"""
            st.session_state['prompt_result'] = final_prompt
            st.session_state['current_vibes'] = selected_vibes
            st.session_state['current_mz'] = selected_mz_ments
            st.success("✅ MZ 감성 듬뿍 담긴 설계도 완성!")

    if 'prompt_result' in st.session_state:
        st.markdown(f"""
        <div class='sub-info'>
        <b>💡 오늘의 화법:</b> {', '.join(st.session_state['current_vibes'])}<br>
        <b>🔥 추천 MZ 멘트:</b> {', '.join(st.session_state['current_mz'])}
        </div>
        """, unsafe_allow_html=True)
        st.text_area("클로드 전용 명령어", value=st.session_state['prompt_result'], height=400)

# --- 🔥 탭 2: 황금 키워드 ---
elif menu == "🔥 오늘의 황금 키워드":
    st.subheader("💎 구글 시트 실시간 연동 황금 키워드")
    df = load_keywords()
    
    st.markdown("<div class='section-title'>📅 오늘의 최신 키워드</div>", unsafe_allow_html=True)
    today_list = df[df['구분'] == '오늘']['키워드'].tolist()
    for kw in today_list: st.markdown(f"<span class='keyword-badge'>{kw}</span>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>⏪ 어제 핫 키워드</div>", unsafe_allow_html=True)
    yesterday_list = df[df['구분'] == '어제']['키워드'].tolist()
    for kw in yesterday_list: st.markdown(f"<span class='keyword-badge badge-yesterday'>{kw}</span>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>📌 언제나 통하는 장기 키워드</div>", unsafe_allow_html=True)
    long_list = df[df['구분'] == '장기']['키워드'].tolist()
    for kw in long_list: st.markdown(f"<span class='keyword-badge badge-evergreen'>{kw}</span>", unsafe_allow_html=True)

    if st.button("🔄 키워드 새로고침"): st.rerun()

# --- 📈 탭 3: 수익 분석 및 전략 (정밀 로직 완전 복구) ---
elif menu == "📈 수익 분석 및 전략":
    st.subheader("📊 애드센스 수익 정밀 진단 & 처방전")
    st.info("💡 어제의 수치를 입력하면 루미미 비서가 수익화 전략을 제안합니다.")

    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1: daily_revenue = st.number_input("어제 수익 ($)", min_value=0.0, step=0.01, format="%.2f")
    with col_in2: daily_pv = st.number_input("어제 페이지뷰 (PV)", min_value=0, step=1)
    with col_in3: daily_ctr = st.number_input("어제 클릭률 (CTR %)", min_value=0.0, step=0.01, format="%.2f")

    if st.button("🧐 루미미 비서에게 진단받기", use_container_width=True):
        if daily_pv > 0:
            clicks = daily_pv * (daily_ctr / 100)
            calculated_cpc = daily_revenue / clicks if clicks > 0 else 0
            
            st.divider()
            st.markdown("### 📝 루미미 비서의 실적 분석 보고서")
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric("추정 CPC (클릭당 단가)", f"${calculated_cpc:.2f}")
            with res_col2:
                st.metric("추정 클릭 수", f"{int(clicks)}회")
            
            st.markdown("#### 🚀 오늘 당장 해야 할 수익화 처방")
            if daily_revenue == 0:
                st.warning("📍 아직 수익이 발생하지 않았어요! '장기 키워드' 탭에 있는 주제들로 유입량을 늘리는 데 집중합시다.")
            elif calculated_cpc < 0.2:
                st.error("📍 **단가가 너무 낮아요!** 지금 쓰는 주제는 광고 단가가 낮습니다. '금융, 보험, 대출, 정부지원금' 같은 고단가 키워드로 주제를 전환하세요.")
            elif daily_ctr < 1.5:
                st.info("📍 **클릭률(CTR)이 아쉬워요!** 글 중간에 '클릭을 유도하는 버튼형 링크'를 넣고, 광고와 사진이 겹치지 않는지 확인해 보세요.")
            elif daily_pv < 100:
                st.info("📍 **유입량이 부족합니다!** 지금은 단가보다 '조회수'가 우선이에요. 네이버 블로그나 스레드에 링크를 적극 배포해 보세요.")
            else:
                st.success("✅ **훌륭합니다!** 현재 전략이 매우 좋습니다. 같은 카테고리의 글을 3개 더 작성해서 블로그 전문성 지수를 높이세요.")
            
            st.info(f"💡 **루미미를 위한 TIP:** 오늘 밤엔 황금 키워드 탭에 있는 고단가 주제로 클로드 설계도 하나 더 뽑아볼까요? 🚀")
        else:
            st.error("분석을 위해 최소한 페이지뷰(PV)는 입력해 주셔야 해요! 😊")
