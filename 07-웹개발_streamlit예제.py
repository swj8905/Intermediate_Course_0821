import streamlit as st

st.text("일반 텍스트입니다.")
st.text("내가 쓰고 싶은 문장을")
st.text("여기에 쓰면 됩니다.")
st.text("아무말이나 써볼게요.")

st.write("---")
st.write("이렇게도 됩니다.")
st.write("# 이렇게도 됩니다.")
st.write("## 이렇게도 됩니다.")
st.write("### 이렇게도 됩니다.")
st.write("#### 이렇게도 됩니다.")
st.write("##### 이렇게도 됩니다.")
st.write("###### 이렇게도 됩니다.")
st.write("> 이렇게도 됩니다.")
st.write(">> 이렇게도 됩니다.")
st.write(">>> 이렇게도 됩니다.")

st.write("https://www.naver.com")

import webbrowser
if st.button("네이버"):
    webbrowser.open("https://www.naver.com")

foo = {"짜장면":5000, "짬뽕":6000, "탕수육":10000}
st.write(foo)

st.write("1 + 1 = ", 2)

st.code("print('Hello World')")

st.write("---")

"그냥 이렇게 해도 됩니다."

"""
# 매직 커맨드
---
> 표를 띄우고 싶으면, 코드에 표를 그리면 됩니다.

|             |   수학    |   평가     |
|-------------|:-----------:|:------------:|
| 철수        |  90       | 참잘했어요.|
| 영희        |  34       | 분발하세요.|

https://www.naver.com

```python
print("Hello World")
```
"""