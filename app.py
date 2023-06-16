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
st.image("https://cdn.pixabay.com/photo/2023/06/07/12/51/insect-8047159_1280.jpg") # 이미지 주소 입력 시 이미지 출력
st.image("img/img.jpg") # 로컬 파일
st.image(image="img/img.jpg")  # 키워드를 사용해서...
st.image("img/img.jpg", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/img.jpg", width=100)  # 파일 경로 (app.py)

# streamlit run app.py

# 마크다운
# https://www.markdownguide.org/cheat-sheet/

# st.write / st.markdown
# st.write -> 입력하는 것에 맞추서 알아서 결정 => 마크다운
# st.markdown => 명백하게 마크다운을 사용하겠다.

# s3까지만 streamlit에 메서드로 존재
st.write("""
# 가장 큰 제목 텍스트 (h1 - headline1 - st.title)
## 그 다음 큰 제목 (h2 - headline2 - st.header)
### 그것보다는 작은 제목 (h3 - headline3 - st.subheader)
#### 더 작은 제목
##### 더 작은 것도 있지롱
###### h6까지 지원
""")
# 문자열을 넣으면 마크다운임

# 서식
text = """
기울임: *별표*를 하나씩 또는 _언더바_를 하나씩 써주면 기울어짐  
볼드체: **별표** 또는 __언더바__를 두 개씩 써주면 볼드체  
취소선: ~~물결표~~  
밑줄: <u>밑줄 태그</u>  
형광펜: <mark>mark 태그</mark>
"""
# st.write(text)
st.markdown(text, unsafe_allow_html=True) # html의 태그를 허용하는 옵션