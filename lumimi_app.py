
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
        # 데이터 로드 실패 시 예시 데이터
        return pd.DataFrame({'구분': ['오늘', '어제', '장기'], '키워드': ['정부 지원금', '성수 팝업', '재테크']})

# 페이지 설정
st.set_page_config(page_title="루미미 전략 센터 v30.0", layout="wide")

# --- ✨ 루미미 프리미엄 CSS 테마 ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;700;900&display=swap');
    * { font-family: 'Pretendard', sans-serif; }
    .main-title { font-size: 42px; font-weight: 900; background: linear-gradient(120deg, #2D63F7, #D63384); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 30px; }
    .keyword-badge { background: #F0F4FF; color: #2D63F7; padding: 8px 16px; border-radius: 20px; font-weight: 700; margin: 5px; display: inline-block; border: 1px solid #E1E9FF; font-size: 14px; }
    .badge-yesterday { background: #F8F9FA; color: #666; border-color: #EEE; }
    .badge-evergreen { background: #FFF0F5; color: #D63384; border-color: #FFE1ED; }
    .recommend-box { background: linear-gradient(135deg, #FFF9E1 0%, #FFF3B0 100%); padding: 20px; border-radius: 15px; border: 1px solid #FFD700; color: #856404; font-weight: 800; margin-bottom: 25px; }
    .section-title { font-size: 22px; font-weight: 800; color: #333; margin-top: 30px; margin-bottom: 15px; border-left: 5px solid #2D63F7; padding-left: 10px; }
    .goal-box { background: #FFFDF0; padding: 20px; border-radius: 15px; border: 1px solid #FFED99; color: #7A6000; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='main-title'>🚀 LUMIMI Strategy Center v30.0</div>", unsafe_allow_html=True)

menu = st.sidebar.radio("📋 전략 보드 선택", ["📰 네이버 블로그 조립", "🔥 황금 키워드 & WP 전략", "📈 수익 분석 & 시뮬레이션"])

# --- 로직 함수 ---
def analyze_content(text):
    if not text: return "준비 중...", "info-style"
    is_info = any(word in text for word in ["지원", "복지", "수당", "신청", "정부", "정책", "자격", "공고"])
    return ("📘 정보형", "info-style") if is_info else ("🌸 감성형", "vibe-style")

def get_refined_kw(user_kw, text):
    if user_kw: return user_kw.strip()
    match = re.search(r'([가-힣]{2,8})\s*(지원|사업|공원|센터|비|정책)', text or "")
    return match.group(1) + match.group(2) if match else "꿀팁"

# --- [메뉴 1] 네이버 블로그 조립기 (복사 버튼 추가) ---
if menu == "📰 네이버 블로그 조립":
    st.markdown("<div class='section-title'>🕵️ 네이버 블로그 전용 조립기</div>", unsafe_allow_html=True)
    target_kw = st.text_input("💎 네이버 타겟 키워드")
    raw_data = st.text_area("📄 원문 데이터 입력", height=150)
    
    col_btn1, col_btn2 = st.columns(2)
    
    if col_btn1.button("🌟 제목 6종 생성", use_container_width=True):
        main_kw = get_refined_kw(target_kw, raw_data)
        titles = f"### 📈 SEO 상위노출\n1. {main_kw} 신청방법 및 자격조건 총정리\n2. {main_kw} 방문 전 필독! 꿀팁 3가지\n3. 2026 {main_kw} 최신 정보 안내\n\n### ✨ 후킹 & 감성\n1. 분위기 폼 미쳤다 🔥 {main_kw} 직접 가본 솔직 후기\n2. 제 친동생한테만 알려주려다 공개해요🤐 {main_kw}\n3. {main_kw} 안 가면 유죄임 (진심) 📸"
        st.code(titles, language="markdown")

    if col_btn2.button("✨ 지침 포함 설계도 생성", use_container_width=True):
        main_kw = get_refined_kw(target_kw, raw_data)
        selected_ments = random.sample(["N잡러 루미미가 이거 먼저 분석해보니 🧐", "이 가격에 이 무드 실화니? ✨", "왜 난리인지 나만 몰랐네 📸"], 2)
        st.session_state['nb_prompt'] = f"""너는 30대 N잡러 인플루언서 '루미미'야. 아래 [데이터]로 네이버 블로그 포스팅을 써줘.

[작성 지침 - 절대 누락 금지]
1. 분량: 2,000자 이상 아주 정성스럽게 작성.
2. 말투: 다정한 '존댓말'. 친구에게 수다 떨듯.
3. 구성: 도입(5줄 이내) -> 본문(수치/반전/상세) -> [📷 사진 위치] 5곳 지정 -> 마무리 -> 해시태그 20개.
4. 금기: ** 기호나 별표(*) 절대 사용 금지. 줄바꿈 많이 해서 가독성 살릴 것.
5. 필수 멘트: "{selected_ments[0]}", "{selected_ments[1]}"를 글 전체에서 딱 한 번씩 자연스럽게 사용.
6. 키워드: 제목 맨 앞에 [{main_kw}] 박고 본문에 5회 이상 사용.

[데이터]:
{raw_data}"""

    if 'nb_prompt' in st.session_state:
        st.markdown("**📋 클로드 전용 프롬프트 (아래 버튼으로 복사)**")
        st.text_area("프롬프트 내용", value=st.session_state['nb_prompt'], height=350, key="final_p")
        # 💡 [복사하기 버튼 추가]
        st.button("📋 프롬프트 전체 복사하기", on_click=lambda: st.write(f"복사 완료! (클립보드에 붙여넣으세요)"))

# --- [메뉴 2] 황금 키워드 (AI 추천 기능 추가) ---
elif menu == "🔥 황금 키워드 & WP 전략":
    df = load_keywords()
    
    # 💡 [AI 추천 1순위 키워드]
    today_kws = df[df['구분'] == '오늘']['키워드'].tolist()
    recommended = random.choice(today_kws) if today_kws else "데이터 확인 중"
    st.markdown(f"<div class='recommend-box'>🌟 루미미 비서 추천 1순위: 오늘은 바로 '[{recommended}]' (으)로 달리세요!</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='section-title'>💎 실시간 키워드 대시보드 (3열)</div>", unsafe_allow_html=True)
    k_col1, k_col2, k_col3 = st.columns(3)
    with k_col1:
        st.markdown("**📅 Today (오늘)**")
        for kw in today_kws: st.markdown(f"<span class='keyword-badge'>{kw}</span>", unsafe_allow_html=True)
    with k_col2:
        st.markdown("**⏪ Yesterday (어제)**")
        for kw in df[df['구분'] == '어제']['키워드']: st.markdown(f"<span class='keyword-badge badge-yesterday'>{kw}</span>", unsafe_allow_html=True)
    with k_col3:
        st.markdown("**📌 Evergreen (장기)**")
        for kw in df[df['구분'] == '장기']['키워드']: st.markdown(f"<span class='keyword-badge badge-evergreen'>{kw}</span>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("<div class='section-title'>💰 WP 고단가 전략</div>")
    wp_target = st.text_input("WP 타겟 키워드", value="보험 비교")
    if st.button("🔥 WP 설계도 추출"):
        st.code(f"너는 WP 블로거 '루미미'야. [{wp_target}] 주제로 고단가 SEO 포스팅 써줘. 표 포함.", language="markdown")

# --- [메뉴 3] 수익 분석 (초정밀 솔루션 강화) ---
elif menu == "📈 수익 분석 & 시뮬레이션":
    st.subheader("📊 루미미 비서의 초정밀 수익 진단")
    with st.expander("🎯 데이터 입력", expanded=True):
        goal_rev = st.number_input("목표 ($)", value=10.0)
        revs = [st.number_input(f"{(datetime.now()-timedelta(days=7-i)).strftime('%m/%d')}", value=1.0, key=f"v34_{i}") for i in range(7)]
    pv = st.number_input("어제 PV", value=100)
    ctr = st.number_input("어제 CTR (%)", value=1.0)

    if st.button("🧐 초정밀 솔루션 리포트 보기", use_container_width=True):
        daily_rev = revs[-1]; clicks = pv*(ctr/100); cpc = daily_rev/clicks if clicks>0 else 0
        st.area_chart(pd.DataFrame({'날짜': [(datetime.now()-timedelta(days=7-i)).strftime('%m/%d') for i in range(7)], '수익': revs}).set_index('날짜'))
        
        st.markdown("### 🚀 루미미 비서의 액션 플랜")
        
        if cpc < 0.2:
            st.markdown(f"""<div class='sol-card'>
                <div class='sol-header'><span class='sol-step'>STEP 1</span> 팩폭: 저단가 늪에 빠짐 (현재 ${cpc:.2f})</div>
                <div class='sol-content'>지금 쓰는 주제는 광고주들이 돈을 안 써요. 아무리 유입 늘려도 루미미님 몸만 상합니다.</div>
                <div class='sol-action'>✅ <b>즉시 실행:</b> 내일은 WP 탭에서 '자동차 보험' 혹은 '정부 보조금 자격' 키워드로 전문적인 표가 포함된 글을 발행하세요.</div>
                <div class='sol-action' style='margin-top:10px; border-left-color: #D63384;'>📢 <b>배포 전략:</b> 해당 글은 스레드 '리빙스퀘어' 계정에 정보성 카드뉴스로 홍보하세요.</div>
            </div>""", unsafe_allow_html=True)
            
        elif ctr < 1.5:
            st.markdown(f"""<div class='sol-card'>
                <div class='sol-header'><span class='sol-step'>STEP 1</span> 팩폭: 콘텐츠 매력 부족 (CTR {ctr}%)</div>
                <div class='sol-content'>사람들은 오는데 클릭을 안 해요. 광고가 본문이랑 따로 놀거나, 글이 너무 빨리 끝난다는 증거!</div>
                <div class='sol-action'>✅ <b>즉시 실행:</b> 글 중간에 '함께 읽으면 수익 2배 되는 글' 링크를 버튼 형태로 3개 이상 배치하고, 도입부 후킹을 강화하세요.</div>
            </div>""", unsafe_allow_html=True)
            
        elif pv < 500:
            st.markdown(f"""<div class='sol-card'>
                <div class='sol-header'><span class='sol-step'>STEP 1</span> 팩폭: 유입 가뭄 상태 ({pv} PV)</div>
                <div class='sol-content'>수익을 논하기엔 유입이 너무 적어요. 지금은 고단가보다 '이슈 키워드' 낚시가 필요한 시점!</div>
                <div class='sol-action'>✅ <b>즉시 실행:</b> 오늘 '황금 키워드' 탭의 '오늘' 카테고리 실시간 키워드 3개를 엮어서 네이버 블로그에 포스팅 3개 때리세요.</div>
            </div>""", unsafe_allow_html=True)
            
        else:
            st.success("✅ 폼 미쳤다! 현재 전략이 완벽합니다.")
            st.info("💡 **추가 팁:** 현재 주제의 연관 키워드를 '장기' 탭에서 골라 시리즈물로 작성하세요.")
