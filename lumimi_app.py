
import streamlit as st
import pandas as pd
import random
import re
from datetime import datetime, timedelta

# 1. 데이터 로드 설정
SHEET_ID = "1zaERVga9_efXnpNL1mmXNdOrJ3syRctLt6hmeJjVgN8"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

def load_keywords():
    try:
        df = pd.read_csv(SHEET_URL)
        df['구분'] = df['구분'].astype(str).str.strip()
        df['키워드'] = df['키워드'].astype(str).str.strip()
        return df
    except:
        return pd.DataFrame({'구분': ['오늘'], '키워드': ['시트 연동을 확인해주세요']})

# 페이지 설정
st.set_page_config(page_title="루미미 전략 센터 v48.0", layout="wide")

# --- ✨ 루미미 프리미엄 CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
    * { font-family: 'Pretendard', sans-serif; }
    .main-title { font-size: 42px; font-weight: 900; background: linear-gradient(120deg, #2D63F7, #D63384); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; }
    .keyword-badge { background: #F0F4FF; color: #2D63F7; padding: 8px 16px; border-radius: 20px; font-weight: 700; margin: 5px; display: inline-block; border: 1px solid #E1E9FF; font-size: 14px; }
    .sol-card { background: white; padding: 25px; border-radius: 20px; border: 1px solid #EAEAEA; box-shadow: 0 10px 30px rgba(0,0,0,0.08); margin-bottom: 25px; }
    .sol-badge { background: #2D63F7; color: white; padding: 4px 12px; border-radius: 8px; font-size: 13px; font-weight: 800; margin-bottom: 10px; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 LUMIMI Strategy Center v48.0</div>", unsafe_allow_html=True)

menu = st.sidebar.radio("📋 전략 보드 선택", [
    "📰 1. 네이버 블로그 전략 (제목 6종)", 
    "💸 2. 네이버 애드포스트 & 쇼핑커넥트", 
    "🔥 3. 오늘의 황금키워드 (새로고침)", 
    "📈 4. 워프 애드센스 수익화 전략"
])

# --- [메뉴 1] 네이버 블로그 (제목 6종 + 전자책 심화 지침 100% 복구) ---
if menu == "📰 1. 네이버 블로그 전략 (제목 6종)":
    st.subheader("🕵️ 전자책 전략 기반 마스터 조립기")
    col1, col2 = st.columns(2)
    with col1: mk = st.text_input("💎 메인 키워드")
    with col2: sk = st.text_input("🔍 스마트블록 키워드")
    
    style = st.selectbox("💬 루미미 시그니처 화법", [
        "가격 & 분위기 반전형 (이 가격에 이 무드 실화니?)", 
        "품절 대란 & 트렌드 유도형 (니네 이거 알아?)", 
        "뒤늦은 깨달음 & 호기심 자극형 (나만 몰랐네)", 
        "감성 공감 & 힐링형 (내 마음을 풀어주네)", 
        "전문가 권위 활용형 (메이크업 쌤이 이거 먼저)"
    ])
    raw_data = st.text_area("📄 분석 데이터 입력", height=150)
    
    col_btn1, col_btn2 = st.columns(2)
    
    if col_btn1.button("🌟 프리미엄 제목 6종 추천", use_container_width=True):
        main_kw = mk if mk else "꿀팁"; sub_kw = sk if sk else ""
        st.code(f"""[상위노출 검색형]
1. {main_kw} {sub_kw} 신청방법 및 자격조건 (2026 최신판)
2. {main_kw} {sub_kw} 직접 확인해본 혜택과 주의사항 정리
3. 2026 {main_kw} 정보, {sub_kw} 모르면 손해 보는 이유

[홈피드 후킹형]
1. 루미미가 분석한 {main_kw}, 의외의 반전 포인트 실화니? 🤐
2. "{sub_kw} 때문에 고민이라면?" {main_kw} 직접 겪어보고 놀란 후기 🔥
3. 나만 알고 싶은 {main_kw} 꿀정보, {sub_kw}까지 싹 다 알려줌 📸""", language="markdown")

    if col_btn2.button("✨ 2,500자 상세 지침 설계도 생성", use_container_width=True):
        main_kw = mk if mk else "꿀팁"; sub_kw = sk if sk else ""
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        
        # ❗ [전자책 & 루미미 지침 완전 박제 - 이 텍스트가 절대 빠지면 안 됨]
        heavy_prompt = f"""너는 대한민국 No.1 인플루언서 '루미미'야. 아래 [데이터]를 바탕으로 네이버 스마트블록 [{sub_kw}] 노출을 정조준한 프리미엄 포스팅을 작성해줘.

### [루미미 마스터 지침 - 절대 누락 금지] ###
1. **제목 전략 (Search Intent)**: 
   - [{main_kw}]를 제목 맨 앞에 배치하고 [{sub_kw}]를 자연스럽게 섞은 '문장형' 제목을 작성할 것. 
   - 슬래시(/)나 특수기호는 전자책 지침에 따라 절대 금지.
2. **검색 의도 우선 설계**: 
   - [{sub_kw}]를 검색한 사람이 당장 원하는 해답을 도입부 5줄 이내에 배치하여 체류시간을 확보해줘.
3. **인간미 로직 (DIA+ 서사)**: 
   - AI 특유의 '첫째, 둘째' 같은 기계적인 나열은 저품질의 원인이 됨. 절대 사용 금지.
   - "{style}" 화법을 녹여낸 다정한 수다톤 존댓말로, 본인의 직접적인 경험담인 것처럼 서사를 만들어.
4. **저품질 회피 & 이미지 가이드**:
   - [📷 사진 위치: OOO 하는 장면 직접 촬영본] 가이드를 글 흐름에 맞춰 6곳 이상 지정해. (이미지 메타데이터까지 고려한 정성 강조)
   - ** 기호나 별표(*) 절대 사용 금지. 빈번한 줄바꿈으로만 가독성을 확보할 것.
   - 키워드 반복은 전체 글에서 7회 이내로 제한.
5. **시그니처 화법 적용**: 
   - "{sel_m[0]}", "{sel_m[1]}"를 문맥의 반전 포인트에 딱 한 번씩만 자연스럽게 배치해.
6. **분량**: 공백 제외 2,500자 이상의 묵직한 고퀄리티 글로 작성.

[데이터]: {raw_data}"""
        st.session_state['p_v48'] = heavy_prompt
        st.success("✅ 상세 지침이 100% 반영된 설계도 완료!")

    if 'p_v48' in st.session_state:
        st.text_area("📋 클로드용 마스터 프롬프트 (전체 복사)", value=st.session_state['p_v48'], height=450)


# --- [메뉴 2] 네이버 수익 (솔루션 구체화) ---
elif menu == "💸 2. 네이버 애드포스트 & 쇼핑커넥트":
    st.subheader("💰 네이버 전용 수익화 로드맵")
    pv = st.number_input("어제 일일 방문자 (PV)", value=100)
    
    if st.button("🧐 단계별 수익화 솔루션", use_container_width=True):
        if pv < 500:
            st.markdown(f"""<div class='sol-card'><div class='sol-badge'>1단계: 유입 확보</div>
            <div class='sol-step'><b>팩폭:</b> 지금 방문자 {pv}명으로는 쇼핑커넥트 수익 안 납니다.</div>
            <div class='sol-step'><b>솔루션:</b> 3번 탭의 '오늘' 키워드 3개를 엮어 정보성 포스팅 2개를 당장 발행하세요.</div></div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class='sol-card'><div class='sol-badge'>2단계: 제휴 확장</div>
            <div class='sol-step'><b>진단:</b> 방문자 수가 충분합니다. 이제 '쇼핑커넥트'를 활용할 때입니다.</div>
            <div class='sol-step'><b>솔루션:</b> 정보형 글 하단에 관련 상품 링크를 네이버 공식 시스템으로 삽입하여 저품질 없이 추가 수익을 창출하세요.</div></div>""", unsafe_allow_html=True)

# --- [메뉴 3] 황금키워드 (새로고침 기능 고정) ---
elif menu == "🔥 3. 오늘의 황금키워드":
    st.subheader("💎 실시간 키워드 대시보드")
    if st.button("🔄 최신 데이터 불러오기 (새로고침)", use_container_width=True):
        st.cache_data.clear()
        st.rerun()
    df = load_keywords()
    k1, k2, k3 = st.columns(3)
    for i, (cat, lab, css) in enumerate(zip(['오늘','어제','장기'],['📅 Today','⏪ Yesterday','📌 Evergreen'],['','badge-yesterday','badge-evergreen'])):
        with [k1,k2,k3][i]:
            st.markdown(f"**{lab}**")
            for k in df[df['구분']==cat]['키워드']: st.markdown(f"<span class='keyword-badge {css}'>{k}</span>", unsafe_allow_html=True)

# --- [메뉴 4] 워프 애드센스 (이중 그래프 & 팩폭 솔루션) ---
elif menu == "📈 4. 워프 애드센스 수익화 전략":
    st.subheader("📊 애드센스 고단가 진단 및 시뮬레이션")
    with st.expander("🎯 데이터 입력", expanded=True):
        goal = st.number_input("일일 목표 ($)", value=10.0)
        revs = [st.number_input(f"{(datetime.now()-timedelta(days=7-i)).strftime('%m/%d')} 수익", value=1.0, key=f"wp_{i}") for i in range(7)]
        pv_wp = st.number_input("어제 WP PV", value=150); ctr_wp = st.number_input("어제 CTR (%)", value=1.2)

    if st.button("🧐 애드센스 마스터 솔루션 보기", use_container_width=True):
        daily_rev = revs[-1]; clicks = pv_wp*(ctr_wp/100); cpc = daily_rev/clicks if clicks>0 else 0
        st.area_chart(pd.DataFrame({'날짜': [(datetime.now()-timedelta(days=7-i)).strftime('%m/%d') for i in range(7)], '수익($)': revs}).set_index('날짜'))
        
        if cpc > 0:
            req_pv = goal / ((ctr_wp/100) * cpc)
            st.line_chart(pd.DataFrame({'PV': [f"{p:,}" for p in sorted([pv_wp, pv_wp*5, int(req_pv)])], '예상': [p*(ctr_wp/100)*cpc for p in sorted([pv_wp, pv_wp*5, int(req_pv)])], '목표': [goal]*3}).set_index('PV'))

            st.markdown("### 🚀 루미미 비서의 팩폭 & 액션 플랜")
            if cpc < 0.2:
                st.error(f"📍 **팩폭:** 단가 ${cpc:.2f}는 심각합니다. 취미로 하시는 거 아니죠?")
                st.markdown("<div class='sol-step'><b>솔루션:</b> 당장 '정부 지원금 신청' 키워드로 갈아타세요. 제목에 '방법'보다 '자격'을 넣어야 돈이 됩니다.</div>", unsafe_allow_html=True)
                st.markdown("<div class='sol-step'><b>배포:</b> 해당 글은 '루미홈' 스레드 계정에 정보성 카드뉴스로 뿌리세요.</div>", unsafe_allow_html=True)
            else:
                st.success("✅ 현재 수익 구조가 훌륭합니다! 발행량만 2배로 늘리세요.")
            if daily_rev >= goal: st.balloons()
