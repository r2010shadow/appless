# appless

## streamlit运行原理
. Streamlit的apps是从上到下执行的Python脚本；
. 每次当一个用户打开浏览器，访问你的app后，上述脚本就会重新执行；
. 当脚本执行时，Streamlit在浏览器渲染它的输出；
. 脚本使用Streamlit缓存来避免重复执行昂贵的运算，所以结果更新会非常快；
. 每次当用户与部件进行交互时，脚本就会重新运行，部件的返回值也会更新为最新状态。

## streamlit常用语法
. 基本的文字显示(markdown)
import streamlit as st
st.title("Streamlit的Title!")
st.header("Streamlit的header")
st.subheader("Streamlit的subheader")
st.text("Streamlit的text....")
st.markdown("### Streamlit的markdown\nctyunos\n #### 基础架构\n 操作系统 ![12]

. 消息状态显示
import streamlit as st
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

. 显示图片
配合pillow库，streamlit可以直接显示图形。
import streamlit as st
from PIL import Image
img = Image.open("12.png")
st.text("图片展示：")
st.image(img, width=500)

. check box用法
check box为可勾选框，如果被选择，则返回True。
import streamlit as st
if st.checkbox("Show/Hide"):
    st.text("Showing the widget")


. Radio Button
radio button为复选按钮，可以根据选择的项目，来返回不同值。

import streamlit as st

status = st.radio("今天天气", ("晴","雨","阴天"))
st.success(status)

- Selection Box
Selection Box为可选框，作用和Radio Button类似，会返回被选择的项目值。

import streamlit as st
status = st.selectbox("今天天气", ("晴","雨","阴天"))
st.success(status)

- Multi-SelectBox
Multi-SelectBox为可以选择多个选项的框，会返回所以选项值。
import streamlit as st
hobby = st.multiselect("兴趣:", ["Dancing", "Reading", "Sports"])
st.write("你有{}种兴趣，分別是{} ".format(len(hobby), hobby))

- Button
button为普通按钮，被点击时值会变为 True。
import streamlit as st
btn = st.button("按钮")
if btn:
    st.text("按下按钮!")

- Text Input
文本输入框，是指从前端获取文本。
import streamlit as st
name = st.text_input("输入名字", "Type Here …")
if(st.button("完成")):
    result = name.title()
    st.success(result)

- Slider
slider滑动条用于从窗体获取特定的数值。
import streamlit as st
level = st.slider("选择难度",1,10)
st.text('Selected: {}'.format(level))
--- 
- File uploader
File uploader上传文件工具，用于将特定文件上传到程序，并处理之。

import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Please choose an image file", type=["png","jpg","jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, width=None)

- SideBar 
SideBar侧边栏，如果在组件前加入SideBar 可以建立，一个两页式页面。

import streamlit as st
from PIL import Image

level = st.sidebar.slider("选择难度", 1, 10)
record = st.sidebar.checkbox("背景同阴影。")
btn = st.sidebar.button("请点击")

uploaded_image = st.file_uploader("Please choose an image file", type=["png","jpg","jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, width=None)


---
- 显示表格：

st.write(1234)
st.write(pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40],
 }))

- 显示仪表盘：

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

- 显示代码块：

st.code()

- 显示数学公式latex格式：

st.latex()

- 选择颜色：

st.color_picker()


