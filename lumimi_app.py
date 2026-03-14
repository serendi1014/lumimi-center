
import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="루미미 네이버 마스터 v65.0", layout="wide")

# --- ✨ 루미미 프리미엄 CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
    * { font-family: 'Pretendard', sans-serif; }
    .main-title { font-size: 42px; font-weight: 900; background: linear-gradient(120deg, #03C75A, #2DB400); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; }
    .section-box { background: white; padding: 25px; border-radius: 20px; border: 1px solid #EAEAEA; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .deep-guide { background: #FFF9F9; padding: 15px; border-radius: 10px; border-left: 5px solid #FF4B4B; font-size: 13px; color: #333; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🌿 LUMIMI NAVER MASTER v65.0</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🏛️ 1. 정보성 (체류시간 극대화)", "💰 2. 쇼핑커넥트 (리뷰 분석/수익)"])

# --- [Tab 1] 정보성 포스팅 (초정밀 지침) ---
with tab1:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 🏛️ 정보성 마스터 초정밀 조립기")
    st.markdown("<div class='deep-guide'><b>⚠️ 지침 강화:</b> 단순히 정보를 나열하지 말고, 검색자가 가장 귀찮아하는 '서류 준비'나 '주의사항'을 본문 중간에 배치해 체류시간을 3분 이상으로 유도합니다.</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1: i_mk = st.text_input("💎 메인 키워드", key="i_mk_65")
    with col2: i_sk = st.text_input("🔍 세부 키워드", key="i_sk_65")
    i_style = st.selectbox("💬 화법 선택", ["가격 & 분위기 반전형", "품절 대란 유도형", "뒤늦은 깨달음 자극형", "감성 공감 힐링형", "전문가 권위 활용형"], key="i_style_65")
    i_data = st.text_area("📄 분석 데이터 입력", height=150, key="i_data_65")
    
    c1, c2 = st.columns(2)
    if c1.button("🌟 정보성 제목 6종 추천", use_container_width=True):
        m = i_mk if i_mk else "꿀팁"; s = i_sk if i_sk else ""
        st.code(f"[상위노출형]\n1. 2026 {m} {s} 직접 신청해보고 정리한 가장 쉬운 방법\n2. {m} {s} 자격 조건 대상자라면 필독해야 할 체크리스트\n3. {m} 정보 찾는다면? {s}까지 한 번에 해결하는 정석 가이드\n\n[후킹형]\n1. 루미미가 {m} 직접 써보니 {s} 부분에서 소름 돋았던 이유 ✨\n2. '{s} 때문에 고민이라면?' {m} 직접 겪어보고 놀란 후기 🔥\n3. 나만 알고 싶은 {m} 꿀정보, {s}까지 싹 다 알려줌 📸", language="markdown")
    
    if c2.button("✨ 정보성 초정밀 설계도 생성", use_container_width=True):
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        i_prompt = f"""너는 대한민국 상위 1% 인플루언서 '루미미'야. 아래 [데이터]로 '체류시간 3분 이상'을 확보하는 고퀄리티 포스팅을 써줘.

[초정밀 지침 - 절대 사수]
1. **제목**: [{i_mk}]가 제목 맨 앞에 오도록 문장형으로 구성 (슬래시/기호 절대 금지).
2. **서론(도입부)**: [{i_sk}]를 검색한 사람의 '불안함'이나 '궁금함'을 5줄 이내로 공감하고 "이 글 하나로 끝내주겠다"는 확신을 줄 것.
3. **본론 구조**:
   - **섹션 1**: [{i_mk}]의 기본 정보와 팩트 체크.
   - **섹션 2**: [{i_sk}]의 구체적 실행법. 여기서 "아래 내용을 보기 전 내 조건부터 체크해보세요"라며 광고 클릭을 유도하는 앵커 멘트 삽입.
   - **섹션 3**: 사람들이 가장 많이 실수하는 부분(전자책 꿀팁 로직)을 경험담처럼 상세히 설명 (체류시간 확보 핵심).
4. **저품질 회피**: 
   - ** 기호나 별표(*) 절대 금지. 빈번한 줄바꿈과 텍스트로만 가독성 확보.
   - [📷 사진 위치: OOO 하는 장면 직접 촬영본] 가이드를 8곳 이상 지정.
5. **화법**: "{i_style}" 톤앤매너 유지 및 "{sel_m[0]}", "{sel_m[1]}" 멘트 배치.
6. **마무리**: 정성스러운 해시태그 20개와 독자 질문 유도. 
7. **분량**: 공백 제외 3,000자 목표 (최소 2,500자 이상).

데이터: {i_data}"""
        st.text_area("📋 정보성 초정밀 프롬프트", value=i_prompt, height=450)

# --- [Tab 2] 쇼핑커넥트 (리뷰 분석 심화 지침) ---
with tab2:
    st.markdown("<div class='section-box'>", unsafe_allow_html=True)
    st.markdown("### 💰 쇼핑커넥트 수익 전환 조립기")
    st.markdown("<div class='deep-guide'><b>⚠️ 지침 강화:</b> 타사 리뷰의 '단점'을 구체적으로 인용(예: 무거워요, 배송이 느려요 등)한 뒤, 이를 반전시키는 화법으로 쇼핑커넥트 링크 클릭률을 높입니다.</div>", unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3: s_mk = st.text_input("💎 제품명/메인 키워드", key="s_mk_65")
    with col4: s_sk = st.text_input("🔍 세부/후킹 키워드", key="s_sk_65")
    s_style = st.selectbox("💬 화법 선택", ["가격 & 분위기 반전형", "품절 대란 유도형", "뒤늦은 깨달음 자극형", "감성 공감 힐링형", "전문가 권위 활용형"], key="s_style_65")
    s_data = st.text_area("📄 타사 리뷰/제품 정보 입력", height=200, key="s_data_65")
    
    sc1, sc2 = st.columns(2)
    if sc1.button("🌟 쇼핑커넥트 제목 6종 추천", use_container_width=True):
        st.code(f"[상위노출형]\n1. {s_mk} {s_sk} 내돈내산 3개월 사용후기와 장단점 비교\n2. 가성비 끝판왕 {s_mk}, {s_sk} 정보까지 꼼꼼하게 따져봤어요\n\n[후킹형]\n1. 왜 난리인지 나만 몰랐네! {s_mk} {s_sk} 직접 써보고 정착한 템 🤐\n2. 이 가격에 이 무드 실화니? {s_mk} {s_sk} 고민하는 분들만 보세요 ✨", language="markdown")
    
    if sc2.button("✨ 수익 전환 초정밀 설계도 생성", use_container_width=True):
        sel_m = random.sample(["N잡러 루미미가 분석해보니 🧐", "솔직히 광고인 줄 알았는데 아니더라고요?", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        s_prompt = f"""너는 대한민국 No.1 리뷰어 '루미미'야. [데이터] 속 타사 리뷰들을 분석해서 '구매하지 않고는 못 배기는' 포스팅을 작성해줘.

[쇼핑커넥트 초정밀 지침]
1. **제목**: [{s_mk}] 포함 문장형 제목. 후킹 요소 필수.
2. **리뷰 분석의 기술**: 
   - 데이터에서 발견한 사용자들의 불만(단점)을 최소 2가지 실감나게 언급 (예: ~라는 후기가 많아서 걱정했는데).
   - 이를 극복하는 실사용 꿀팁이나 반전 장점을 제시하며 쇼핑커넥트 링크로 유도.
3. **수익 멘트**: "품절 되기 전에 서둘러야 해요", "저도 여기서 최저가로 겨우 구했어요" 등 트렌드 유도 화법 3회 이상 사용.
4. **저품질 회피**: ** 기호 금지. [📷 사진 위치: OOO 하는 생생한 장면] 가이드 8곳 지정. 
5. **화법/분량**: "{s_style}" 적용. 2,500자 이상의 묵직한 볼륨으로 정성 강조. "{sel_m[0]}", "{sel_m[1]}" 사용.
6. **비교표**: 데이터 기반으로 타사 제품과의 차별점을 '텍스트 기반 비교표'로 가독성 있게 작성.

데이터: {s_data}"""
        st.text_area("📋 쇼핑커넥트 초정밀 프롬프트", value=s_prompt, height=450)
