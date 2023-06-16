# pip install streamlit
# streamlit hello

import streamlit as st

st.title("나의 파이썬 웹페이지")
st.header("수업 8일차에 만들었어요")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 Streamlit 페이지, 너를 위해 구웠지")

# 기능이 실행되는 순서대로 화면에서 표현
# 즉, 스크립트에서 위쪽 줄에 있는 것들이 먼저 실행됨
st.header("2023 LCK Summer Split 6월 15일 제2경기 DK vs BRO")
st.subheader("1세트")
st.video("https://youtu.be/HOuevBst6fw") # 유튜브 등 링크를 입력하면 자동으로 띄워주는 메서드
st.subheader("2세트")
st.video("https://youtu.be/QT5aaVPpHZE")
st.subheader("3세트")
st.video("https://youtu.be/yLDqGEngb0E")
st.subheader("MVP 인터뷰")
st.video("https://youtu.be/9OU_VzcO9Ag")
st.subheader("풀 경기 영상 및 분석데스크")
st.video("https://youtu.be/3f2EyaXkfLg")
st.subheader("총평")
st.write("수상할 정도로 DK만 만나면 강해지는 브리온")
st.image("https://cdn.pixabay.com/photo/2023/06/07/12/51/insect-8047159_1280.jpg") # 이미지 주소 입력 시 이미지 출력
st.image("img/img.jpg") # 로컬 파일
st.image(image="img/img.jpg")  # 키워드를 사용해서...
st.image("img/img.jpg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/img.jpg", width=100)  # 파일 경로 (app.py)

# streamlit run app.py
st.title("컴포넌트")
# 위아래로 한 줄로만
st.write("🔫")
cols = st.columns(2) # column 리스트
cols[0].write("🔫")
cols[1].write("🔫")
cols = st.columns(3)
# ⚔️ => 페이지를 n등분
# 최대 한도가 있는데 보통은 12등분까지만 하고, 일반적으로는 3등분까지만 사용
cols[0].write("⚔️")
cols[1].write("⚔️")
cols[2].write("⚔️")
cols_ = cols[0].columns(3)
cols_[0].write("⚔️")
cols_[1].write("⚔️")
cols_[2].write("⚔️")
col1, col2 = st.columns(2) # 리스트 언패킹
col1.write("왼쪽 열")
col2.write("오른쪽 열")

with col1: # col1을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col1에 종속
    st.write("왼쪽")
with col2:  # col2을 기준으로 streamlit을 써주겠다
    # 블록 (:) 을 열면 -> 이 안에서는 streamlit 기능 실행시 col2에 종속
    st.write("오른쪽")

tab_menus = st.tabs(["김치찌개", "된장찌개", "로제마라뭐시기"])
tab1, tab2, tab3 = tab_menus
img1 = "https://cdn.pixabay.com/photo/2017/01/05/09/18/food-1954424_1280.png"
tab1.image(img1)
with tab2:
    img2 = "https://cdn.pixabay.com/photo/2015/05/02/01/04/miso-soup-749368_1280.jpg"
    st.image(img2)
tab3.image("https://i.namu.wiki/i/_uGUJU9gCGPWvGRjxwe6keCc7r-6GqoMPBXZTT_RFqopcFhsjHwlfAB0D-_fhS3Z_K9lzKSgFrPWYcfxzCxbjg.webp")
tab3.write("잘 알아두세요. 그런 건 없어요!")

exp = st.expander("Surprise!!")
exp.image("https://i.namu.wiki/i/5lWwYGj-VC8ZqJxug7Exm5-7rHE97fdZui3DWEAjm0zdLiBCbcdw4mLyGhcbZ_KecZOQr4rtwNJSFs63Rsdd_Q.webp")
# with exp: 구문도 사용 가능합니다.

# 입력
st.title("입력")
name = st.text_input("나의 이름은") # 변수로 받을 수 있음
name2 = st.text_input("키미노 나마에와") # 변수로 받을 수 있음
# st.text_input("")
# st.write(name)
# st.write(name2)
st.write(f"신랑 {name}과 신부 {name2}는...")
age = st.number_input("당신의 나이는?", step=1)
st.write(f"나의 나이는 {age}세")
height = st.number_input("당신의 키는?", step=1, min_value=1)
st.write(f"나의 키는 {height}cm")

st.divider()
mode = st.checkbox("강사님 잔소리모드") # bool (T/F)
col1, col2, col3 = st.columns(3)
r = st.radio("잔소리 내용 선택", ["취업", "코딩", "지각"])
s = col2.slider("잔소리 강도 선택", min_value=0, max_value=10)
b = col3.selectbox("잔소리 말투 선택", ["친절하게", "반말", "모욕적"])
if mode:
    # r -> 취업, 코딩, 지각
    format = None
    if b == "친절하게":
        format = lambda x: f"여러분~ {x}"
    elif b == "반말":
        format = lambda x: f"야, {x}"
    elif b == "모욕적":
        format = lambda x: f"XXXXX! {x}"
    if r == "취업":
        st.write("여러분 8월에는 자소서 넣어야겠죠?")
    elif r == "코딩":
        st.write("여러분 저보다 파이썬 잘해요?")
    elif r == "지각":
        st.write("9시랑 9시 1분은 다른 거에요.")
