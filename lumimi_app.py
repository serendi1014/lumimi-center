
import streamlit as st
import pandas as pd
import random  # 랜덤 기능을 위해 이 줄이 상단에 꼭 있어야 해요!

# ... (기본 설정 및 CSS 생략: 기존 코드 유지) ...

# --- 📰 탭 1: 네이버 블로그 완제품 조립 (20종 화법 랜덤 엔진) ---
if menu == "📰 블로그 완제품 조립":
    st.subheader("🕵️ 네이버 블로그 포스팅 완제품 조립기")
    raw_data = st.text_area("분석할 기사 본문이나 제품 상세 정보", height=250, placeholder="여기에 내용을 넣어주세요!")
    
    # 루미미 전용 화법 20종 데이터베이스
    vibe_db = [
        "공감형: '저도 해보니 헷갈려서 정리해요'",
        "팩트형: '서울 월세 80만 원 시대, 통계 보고 손이 떨리더라고요'",
        "질문형: '혹시 나만 빼고 다 받는 혜택, 놓치고 계신 건 아닐까요?'",
        "시간 절약형: '10분 분량의 정책 자료를 1분 컷으로 요약했어요'",
        "결론 선포형: '오늘 이 글 하나로 모든 고민은 끝내 드릴게요'",
        "반전/감탄형: '이 가격에 이 무드 실화니?'",
        "비밀 공유형: '이건 사실 아는 사람들만 조용히 챙겨가는 꿀팁인데요'",
        "뒤늦은 깨달음: '왜 난리인지 나만 몰랐네'",
        "단계별 가이드: '첫 단추만 잘 끼우면 그다음부턴 알아서 굴러가요'",
        "비교 우위형: '다른 정책이랑 비교해 보니, 이게 압승이더라고요'",
        "품절/트렌드형: '품절 난 이 혜택 니네 알아?'",
        "전문가 권위형: 'N잡러 루미미가 이거 먼저 분석해보니'",
        "감성 힐링형: '슬픈 하루였는데 내 마음을 풀어주네'",
        "솔직 고백형: '솔직히 저도 처음엔 광고인 줄 알고 의심했거든요?'",
        "지인 추천형: '제 친동생에게만 몰래 알려주고 싶은 소식이에요'",
        "자신감 회복형: '지금 시작해도 늦지 않아요. 루미미가 응원할게요!'",
        "마감 임박형: '신청 기간 얼마 안 남았어요. 지금 안 누르면 다음은 없어요!'",
        "가치 강조형: '환경도 지키고 지갑도 지키는 이 선택, 안 할 이유가 없죠?'",
        "질문형 여운: '여러분이 생각하는 가장 매력적인 혜택은 무엇인가요?'",
        "액션 플랜형: '자, 이제 스마트폰 켜고 가입부터 하러 가볼까요?'"
    ]

    col_btn1, col_btn2 = st.columns(2)
    
    # 1. 제목 생성 (랜덤성 부여)
    if col_btn1.button("🌟 클릭 유도형 제목 5종 뽑기", use_container_width=True):
        if raw_data:
            titles = """
1. [공감] 나만 모르면 손해? 직접 분석한 핵심 혜택 💙
2. [반전] 이 가격 실화니? 혜택 뜯어보고 깜짝 놀랐어요
3. [꿀팁] 친동생에게만 알려주려다 공개하는 찐 정보
4. [팩트] 통계로 본 현실, 해결책은 바로 이것!
5. [응원] 지금도 안 늦었어요! 루미미와 함께 시작해요
            """
            st.code(titles, language="markdown")

    # 2. 설계도 생성 (20종 중 3개 랜덤 조합)
    if col_btn2.button("✨ 루미미 화법 20종 랜덤 설계도 뽑기", use_container_width=True):
        if raw_data:
            # 20개 중 오늘 사용할 3개 화법 무작위 추출
            selected_vibes = random.sample(vibe_db, 3)
            
            final_prompt = f"""너는 30대 N잡러 인플루언서 '루미미(lumimi)'야. 
아래 [데이터]를 바탕으로 네이버 블로그 포스팅을 "한 번에" 작성해줘. 

[오늘의 루미미 필수 화법 조합]
- 화법 1: {selected_vibes[0]}
- 화법 2: {selected_vibes[1]}
- 화법 3: {selected_vibes[2]}

[작성 지침]
1. 분량: 2,000자 이상 아주 아주 길고 정성스럽게 작성할 것. 
2. 말투: 다정한 '존댓말' 사용. 친구에게 수다 떨듯 친근하게 재구성해줘.
3. 구성: 도입부에서 첫 번째 화법을 사용하고, 본문과 결론에 나머지 화법을 자연스럽게 녹여줘.
4. 사진: 글 중간에 [📷 사진 위치]를 총 5곳 지정해줘.
5. 금기사항: ** 기호나 별표(*)는 절대 쓰지 마. 오직 텍스트로만 가독성 좋게 줄바꿈 많이 해줘.
6. 마무리: 마지막엔 해시태그 20개를 달아줘.

[데이터]:
{raw_data}
            """
            st.session_state['prompt_result'] = final_prompt
            st.session_state['current_vibes'] = selected_vibes
            st.success("✅ 새로운 화법 조합으로 설계도가 준비됐어요!")

    if 'prompt_result' in st.session_state:
        st.markdown(f"**💡 적용된 화법:** `{', '.join(st.session_state['current_vibes'])}`")
        st.text_area("클로드 전용 명령어", value=st.session_state['prompt_result'], height=450)
        st.info("💡 위 명령어를 복사해서 클로드에게 주면 매번 다른 느낌으로 글을 써줍니다! 💙")
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
