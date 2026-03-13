
import streamlit as st
import pandas as pd
import random
import re

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
st.set_page_config(page_title="루미미 전략 센터 v21.0", layout="wide")

# CSS 스타일 (루미미 시그니처 테마)
st.markdown("""
    <style>
    .keyword-badge { background-color: #E1E9FF; color: #2D63F7; padding: 6px 14px; border-radius: 15px; font-weight: bold; margin-right: 10px; display: inline-block; margin-bottom: 12px; border: 1px solid #D0DFFF; font-size: 14px; }
    .badge-yesterday { background-color: #F0F2F6; color: #555; }
    .badge-evergreen { background-color: #FFF0F0; color: #FF4B4B; }
    .main-title { font-size: 35px; font-weight: 900; color: #1E1E1E; margin-bottom: 25px; }
    .mode-info { padding: 12px 20px; border-radius: 10px; margin-bottom: 20px; font-weight: bold; font-size: 16px; }
    .info-style { background-color: #E8F4FD; color: #007BFF; border-left: 5px solid #007BFF; }
    .vibe-style { background-color: #FFF0F5; color: #D63384; border-left: 5px solid #D63384; }
    .section-title { font-size: 20px; font-weight: bold; margin-top: 30px; margin-bottom: 15px; border-bottom: 2px solid #EEE; padding-bottom: 5px; }
    .goal-box { background-color: #FFF9E1; padding: 15px; border-radius: 10px; border: 1px solid #FFD700; color: #856404; font-weight: bold; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 루미미 AI 전략 센터 v21.0</div>", unsafe_allow_html=True)

# 메뉴 정의
menu = st.sidebar.radio("메뉴 선택", ["📰 블로그 완제품 조립", "🔥 오늘의 황금 키워드", "📈 수익 분석 및 전략"])

# --- AI 주제 분석 함수 ---
def analyze_content(text):
    if not text: return "준비 중...", "info-style"
    is_info = any(word in text for word in ["지원", "복지", "수당", "신청", "정부", "정책", "자격", "공고"])
    return ("📘 정보형 모드 (신뢰/전문성)", "info-style") if is_info else ("🌸 감성형 모드 (공감/후킹)", "vibe-style")

# --- 키워드 정교화 추출 함수 ---
def get_refined_kw(user_kw, text):
    if user_kw: return user_kw.strip()
    if not text: return "꿀팁"
    match = re.search(r'([가-힣]{2,8})\s*(지원|사업|공원|센터|비|정책)', text)
    if match: return match.group(1) + match.group(2)
    words = re.findall(r'[가-힣]{3,6}', text)
    return max(set(words), key=words.count) if words else "꿀팁"

# --- [메뉴 1] 블로그 조립기 (SEO & MZ 통합) ---
if menu == "📰 블로그 완제품 조립":
    st.subheader("🕵️ 네이버 블로그 AI 스마트 조립기")
    target_kw = st.text_input("💡 타겟 키워드", placeholder="노출시키고 싶은 핵심 단어 (예: 가족돌봄청년)")
    raw_data = st.text_area("기사 본문 또는 내용 입력", height=200)

    mode_name, mode_class = analyze_content(raw_data)
    if raw_data:
        st.markdown(f"<div class='mode-info {mode_class}'>현재 감지된 모드: {mode_name}</div>", unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns(2)

    if col_btn1.button("🌟 [전략적] 제목 6종 생성", use_container_width=True):
        if raw_data or target_kw:
            main_kw = get_refined_kw(target_kw, raw_data)
            if "정보형" in mode_name:
                titles = f"### 📈 [SEO 상위노출형]\n1. {main_kw} 신청방법 및 자격조건 (2026 최신 가이드)\n2. {main_kw} 지원금 대상자 확인 및 복지포털 접수 방법\n3. {main_kw} 혜택 누락 주의! 중위소득 150% 기준 안내\n\n### 🔥 [홈판 후킹형]\n1. 설마 나도 대상? {main_kw} 소식 루미미가 분석해봤어요 🧐\n2. 제 친동생에게만 알려주고 싶은 {main_kw} 꿀정보 공개!\n3. 갓생 사는 {main_kw}들을 위한 서울시의 선물 🎁"
            else:
                titles = f"### 📈 [SEO 상위노출형]\n1. {main_kw} 주차 예약 및 봄나들이 코스 추천 (내돈내산)\n2. 서울 가볼만한곳 {main_kw} 사진 찍기 좋은 명당 꿀팁\n3. {main_kw} 방문 후기 및 이용 시간/입장료 총정리\n\n### ✨ [감성 후킹형]\n1. 와.. 서울에 이런 곳이? {main_kw} 분위기 폼 미쳤다 🔥\n2. 나만 알고 싶은 비밀 장소 {main_kw} 안 가면 유죄임 (진심) 📸\n3. 감성 수치 200% 충전! {main_kw} 나들이 루미미 찐 후기 ☁️"
            st.code(titles, language="markdown")

    if col_btn2.button("✨ [MZ특화] 랜덤 설계도 뽑기", use_container_width=True):
        if raw_data or target_kw:
            main_kw = get_refined_kw(target_kw, raw_data)
            info_ments = ["N잡러 루미미가 이거 먼저 분석해보니 🧐", "신청 기간 얼마 안 남았어요! 지금 안 하면 후회해요 🤐", "솔직히 저도 처음엔 광고인 줄 알았거든요?"]
            place_ments = ["이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸", "이거 안 가면 유죄임 (진지) 🔥", "슬픈 하루였는데 내 마음을 풀어주네 ☁️"]
            selected_ments = random.sample(info_ments if "정보형" in mode_name else place_ments, 2)
            
            final_prompt = f"""너는 30대 N잡러 인플루언서 '루미미'야. 
[{main_kw}]를 제목 맨 앞에 박고 본문에 5회 이상 자연스럽게 사용해줘.

[지침]
- 컨셉: {mode_name} (말투 수위 조절: 정보형은 신뢰감 있게, 감성형은 힙하게)
- 필수 화법 멘트: "{selected_ments[0]}", "{selected_ments[1]}"를 자연스럽게 한 번씩 사용.
- 구성: 도입부 5줄 이내 -> 본문 상세 정보(수치 정확히) -> 사진 위치 5곳 지정 -> 마무리 -> 해시태그 20개.
- 주의: ** 기호 절대 금지, 줄바꿈 많이 해서 가독성 극대화.
- 데이터: {raw_data}"""
            st.session_state['prompt_result'] = final_prompt
            st.session_state['current_kw'] = main_kw
            st.success("✅ 타겟 키워드 맞춤형 설계도 완성!")

    if 'prompt_result' in st.session_state:
        st.info(f"💡 현재 타겟 키워드: {st.session_state['current_kw']}")
        st.text_area("클로드 전용 명령어", value=st.session_state['prompt_result'], height=450)

# --- [메뉴 2] 황금 키워드 (3열 완벽 배치) ---
elif menu == "🔥 오늘의 황금 키워드":
    st.subheader("💎 실시간 황금 키워드 대시보드")
    df = load_keywords()
    k_col1, k_col2, k_col3 = st.columns(3)
    with k_col1:
        st.markdown("<div class='section-title'>📅 오늘 최신</div>", unsafe_allow_html=True)
        for kw in df[df['구분'] == '오늘']['키워드']: st.markdown(f"<span class='keyword-badge'>{kw}</span>", unsafe_allow_html=True)
    with k_col2:
        st.markdown("<div class='section-title'>⏪ 어제 핫</div>", unsafe_allow_html=True)
        for kw in df[df['구분'] == '어제']['키워드']: st.markdown(f"<span class='keyword-badge badge-yesterday'>{kw}</span>", unsafe_allow_html=True)
    with k_col3:
        st.markdown("<div class='section-title'>📌 장기(Evergreen)</div>", unsafe_allow_html=True)
        for kw in df[df['구분'] == '장기']['키워드']: st.markdown(f"<span class='keyword-badge badge-evergreen'>{kw}</span>", unsafe_allow_html=True)
    if st.button("🔄 리스트 새로고침"): st.rerun()

# --- [메뉴 3] 수익 분석 (그래프 + 목표 라인 + 게이지 바) ---
elif menu == "📈 수익 분석 및 전략":
    st.subheader("📊 수익 정밀 진단 & 목표 시뮬레이션")
    with st.expander("🎯 나의 수익 목표 설정", expanded=True):
        goal_revenue = st.number_input("나의 일일 수익 목표 ($)", min_value=1.0, value=10.0, step=1.0)
    
    col_in1, col_in2, col_in3 = st.columns(3)
    with col_in1: daily_revenue = st.number_input("어제 수익 ($)", min_value=0.0, step=0.1, format="%.2f")
    with col_in2: daily_pv = st.number_input("어제 페이지뷰 (PV)", min_value=0, step=10)
    with col_in3: daily_ctr = st.number_input("어제 클릭률 (CTR %)", min_value=0.0, step=0.1, format="%.2f")

    if st.button("🧐 루미미 비서의 정밀 진단받기", use_container_width=True):
        if daily_pv > 0:
            clicks = daily_pv * (daily_ctr / 100)
            cpc = daily_revenue / clicks if clicks > 0 else 0
            attainment_rate = min(daily_revenue / goal_revenue, 1.0)
            
            st.divider()
            # 메트릭 표시
            m1, m2, m3 = st.columns(3)
            m1.metric("클릭당 단가(CPC)", f"${cpc:.2f}")
            m2.metric("예상 클릭수", f"{int(clicks)}회")
            m3.metric("방문자당 수익", f"${(daily_revenue/daily_pv):.4f}")

            # 목표 달성 게이지
            st.markdown(f"#### 🚩 현재 목표 달성률: {int((daily_revenue/goal_revenue)*100)}%")
            st.progress(attainment_rate)

            # 그래프 및 시뮬레이션
            if cpc > 0 and daily_ctr > 0:
                required_pv = goal_revenue / ((daily_ctr/100) * cpc)
                st.markdown(f"""<div class='goal-box'>💡 목표 ${goal_revenue} 달성을 위해 일일 약 {int(required_pv):,} PV가 필요합니다! (현재의 약 {round(required_pv/daily_pv, 1) if daily_pv > 0 else 0}배 유입 필요)</div>""", unsafe_allow_html=True)
                
                pv_steps = sorted(list(set([daily_pv, daily_pv*2, daily_pv*5, daily_pv*10, int(required_pv)])))
                chart_data = pd.DataFrame({
                    'PV 단계': [f"{p Daisy:,} PV" for p in pv_steps],
                    '예상 수익($)': [(p * (daily_ctr/100) * cpc) for p in pv_steps],
                    '목표 선($)': [goal_revenue] * len(pv_steps)
                }).set_index('PV 단계')
                st.line_chart(chart_data)

            # 처방전
            st.markdown("#### 🚀 루미미 비서의 처방전")
            if cpc < 0.2: st.error("📍 단가가 낮아요! 금융, 보험, 정부지원금 카테고리로 주제를 전환하세요.")
            elif daily_ctr < 1.5: st.info("📍 클릭률이 낮아요! 글 중간에 버튼형 링크를 넣거나 광고 배치를 확인하세요.")
            elif daily_pv < 100: st.warning("📍 유입량이 부족해요! 지금은 조회수가 우선! 스레드 배포를 2배로 늘리세요.")
            else: st.success("✅ 전략이 아주 좋습니다! 이 페이스로 글 발행량을 늘려 목표 PV를 달성합시다!")
