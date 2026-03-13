
import streamlit as st
import pandas as pd
import random
import re

# 1. 구글 시트 연결 및 기본 설정 (기존 로직 유지)
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

st.set_page_config(page_title="루미미 전략 센터 v18.0", layout="wide")

# CSS 스타일 (루미미 시그니처 컬러)
st.markdown("""
    <style>
    .keyword-badge { background-color: #E1E9FF; color: #2D63F7; padding: 6px 14px; border-radius: 15px; font-weight: bold; margin-right: 10px; display: inline-block; margin-bottom: 12px; border: 1px solid #D0DFFF; font-size: 14px; }
    .badge-evergreen { background-color: #FFF0F0; color: #FF4B4B; }
    .main-title { font-size: 35px; font-weight: 900; color: #1E1E1E; }
    .mode-info { padding: 10px 20px; border-radius: 8px; margin-bottom: 20px; font-weight: bold; }
    .info-style { background-color: #E8F4FD; color: #007BFF; border-left: 5px solid #007BFF; }
    .vibe-style { background-color: #FFF0F5; color: #D63384; border-left: 5px solid #D63384; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 루미미 AI 전략 센터 v18.0</div>", unsafe_allow_html=True)

menu = st.sidebar.radio("메뉴 선택", ["📰 블로그 완제품 조립", "🔥 오늘의 황금 키워드", "📈 수익 분석 및 전략"])

if menu == "📰 블로그 완제품 조립":
    st.subheader("🕵️ 네이버 블로그 AI 스마트 조립기")
    raw_data = st.text_area("기사 본문이나 키워드를 입력하세요", height=200, placeholder="예: 가족돌봄 청년 지원금 소식 / 화랑대 철도공원 나들이 후기")
    
    # --- 1. AI 주제 분석 및 모드 결정 ---
    def analyze_content(text):
        if not text: return "준비", "info-style", "꿀팁"
        
        # 키워드 분석 로직
        is_info = any(word in text for word in ["지원", "복지", "수당", "신청", "정부", "선포", "계획", "자격"])
        
        # 메인 키워드 추출 (가장 많이 언급된 명사)
        words = re.findall(r'[가-힣]{2,6}', text)
        stop_words = ['서울시', '대하여', '있습니다', '위한', '따라', '합니다']
        common_words = [w for w in words if len(w) >= 2 and w not in stop_words]
        main_kw = max(set(common_words), key=common_words.count) if common_words else "정보"
        
        if is_info:
            return "📘 정보형 모드 (신뢰/전문성)", "info-style", main_kw
        else:
            return "🌸 감성형 모드 (공감/후킹)", "vibe_style", main_kw

    mode_name, mode_class, main_kw = analyze_content(raw_data)
    
    if raw_data:
        st.markdown(f"<div class='mode-info {mode_class}'>현재 분석 모드: {mode_name} | 감지된 키워드: [{main_kw}]</div>", unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns(2)
    
    # --- 2. 동적 제목 생성 엔진 ---
    if col_btn1.button("🌟 [맞춤형] 제목 6종 생성", use_container_width=True):
        if raw_data:
            if "정보형" in mode_name:
                titles = f"""
### 📈 [SEO 상위노출형]
1. 2026 서울시 {main_kw} 지원금 신청방법 및 대상자 조건 정리 (중위 150%)
2. {main_kw} 혜택 놓치지 마세요! 월 30만원 자기돌봄비 신청 가이드
3. 서울 복지포털 {main_kw} 신청 기간 및 필수 제출 서류 안내

### 💡 [신뢰 후킹형]
1. "설마 나도 대상?" 서울시 {main_kw} 지원 소식, 루미미가 꼼꼼히 뜯어봤어요 🧐
2. 제 친동생에게만 알려주고 싶은 {main_kw} 꿀정보, 오늘 다 풉니다!
3. 복잡한 {main_kw} 정책, N잡러 루미미가 1분 요약해 드려요 📝
                """
            else:
                titles = f"""
### 📈 [SEO 상위노출형]
1. 서울 가볼만한곳 {main_kw} 주차 예약 및 봄나들이 코스 추천 (내돈내산)
2. {main_kw} 사진 찍기 좋은 스팟 명당! 주말 데이트 후기

### ✨ [감성 후킹형]
1. 와.. 서울에 이런 곳이 있었다고? "{main_kw}" 분위기 폼 미쳤다 🔥
2. 나만 알고 싶은 비밀 장소 "{main_kw}", 안 가면 유죄임 (진심) 📸✨
3. 갓벽한 주말을 위한 "{main_kw}" 나들이 후기, 감성 수치 200% 충전 ☁️
                """
            st.code(titles, language="markdown")

    # --- 3. 맞춤형 설계도 생성 ---
    if col_btn2.button("✨ [맞춤형] 랜덤 설계도 뽑기", use_container_width=True):
        if raw_data:
            # 모드별 멘트 풀
            info_ments = ["N잡러 루미미가 이거 먼저 분석해보니 🧐", "신청 기간 얼마 안 남았어요! 지금 안 하면 후회해요 🤐", "솔직히 저도 처음엔 광고인 줄 알았거든요?"]
            place_ments = ["이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸", "슬픈 하루였는데 내 마음을 풀어주네 ☁️"]
            
            selected_ments = random.sample(info_ments if "정보형" in mode_name else place_ments, 2)
            
            final_prompt = f"""너는 30대 N잡러 인플루언서 '루미미'야. 
[데이터]를 분석해서 네이버 블로그 글을 써줘. 

[중요 Vibe 지침]
- {mode_name} 컨셉에 맞춰서 작성할 것.
- 정보형일 경우 '똑 부러지는 전문가 언니' 말투로 신뢰감 있게!
- 감성형일 경우 '친근하고 힙한 언니' 말투로 생생하게!
- 추천 멘트: "{selected_ments[0]}", "{selected_ments[1]}"를 문맥에 맞게 한 번씩만 사용.

[작성 지침]
- 도입부는 5줄 이내 핵심 요약.
- 사진 위치 5곳 지정, ** 기호 금지, 줄바꿈 많이.
- [데이터]: {raw_data}"""
            
            st.session_state['prompt_result'] = final_prompt
            st.success("✅ 주제 분석 완료! 최적화된 설계도가 준비되었습니다.")

    if 'prompt_result' in st.session_state:
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
