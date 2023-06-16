import streamlit as st

# 마크다운
# https://www.markdownguide.org/cheat-sheet/
st.title("마크다운")
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

# 레이아웃
st.subheader("레이아웃")
st.write("""
#### 순서가 없는 리스트
* 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 들여쓰기1
            * 들여쓰기2
                * 들여쓰기3
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        - 들여쓰기1
            - 들여쓰기2
                - 들여쓰기3
""")
st.write("""
#### 순서가 있는 리스트
    1. 순서가
    2. 있는
    4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
        1. 들여쓰기1
            1. 들여쓰기2 # 1로 시작하지 않으면 들여쓰기는 무시
                1. 들여쓰기3
    1. 순서가
    1. 1로 넣어도
    1. 증가됨
    ### 가로줄
    ---
    (---)
    ___
    (___)
### 테이블 (표)
|팀|라인업|
|---|---|
|DK|Canna Canyon Showmaker Rahel Kellin|
|BRO|Morgan UmTi Ivory Hena Effort|
""")
# 테이블 생성은 판다스에서 다 강력한 기능을 지원하니, 여기서는 마크다운에도 이런 기능이 있다는 것만 알고 갑시다.

# 링크
st.divider()
st.subheader("링크")
l1 = "https://www.naver.com"
l2 = "https://cdn.pixabay.com/photo/2018/07/15/12/32/the-deer-bug-3539532_1280.jpg"
st.write(f"""
    * [표시할 텍스트]({l1})
    * ![사슴벌레]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 대충 뭔가 멋진 말 쓰고 궁서체로 넣으면 있어보인다. - 이말년


    > 진입 장벽은 수익이다. - 0인 강사님  

    책이나, 사람말 인용할 때...
    > 인용 첫줄
    > > 인용문 안에 인용임

    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시 (한줄)`
    ```
    여러 줄로 코드를 나타내고
    줄바꿈도 반영하고 싶으면...
    print("파이썬!")
    ```
    ```python
    print("파이썬!")
    ```
""")