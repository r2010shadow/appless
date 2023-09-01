# code from 30days.streamlit.app
import streamlit as st
from datetime import time, datetime
import time

## one line cartoon tips ##
# st.balloons() 
## ##

# 14

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
  #st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://www.labware.com/hs-fs/hubfs/_LabWare.com/Logos/LabWare%20Corporate%20Logo%20Color.png?width=250&height=143&name=LabWare%20Corporate%20Logo%20Color.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')


# 样例 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# 样例 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# 样例 3
st.header('st.button')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')

# 样例 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
# 5
import pandas as pd
import numpy as np

st.header('Line chart')
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)
# 6
st.header('st.selectbox')
option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

# 7
st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)

# 8
st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee:
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")


#  9
#import pandas as pd
#import pandas_profiling
#from streamlit_pandas_profiling import st_profile_report

#st.header('`streamlit_pandas_profiling`')

#df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

#pr = df.profile_report()
#st_profile_report(pr)

# 10
st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

# 11
st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


# 12
#st.title('st.secrets')
#st.write(st.secrets['message'])

#13 notepad -> save *.csv(utf8)
st.title('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')


# 15
#st.title('st.progress')
#my_bar = st.progress(0)

#for percent_complete in range(100):
#     time.sleep(0.05)
#     my_bar.progress(percent_complete + 1)

#st.balloons()

# 16
st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)


# 17
# Using cache


# 18
st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)

# 19
import requests

st.title('🏀 Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
  with st.expander('JSON data'):
    st.write(suggested_activity)

st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
  st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
  st.metric(label='Price', value=suggested_activity['price'], delta='')

# 20
import json
import streamlit as st
from pathlib import Path

# 然后我们需要 Streamlit Elements 中的这些对象
# 有关全部对象及其用法的说明请见：https://github.com/okld/streamlit-elements#getting-started

from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

# 更改页面布局，让仪表盘占据整个页宽

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Build a draggable and resizable dashboard with Streamlit Elements.")
    st.write("---")

    # 媒体播放器所用的 URL
    media_url = st.text_input("Media URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

# 初始化代码编辑器和图表的默认数据
#
# 在这篇教程中，我们会用到 Nivo Bump 图的数据
# 你能在“data”标签页下获取随机的数据：https://nivo.rocks/bump/
#
# 如下所示，当代码编辑器发生更改时，会话状态就会被更新
# 然后会被读入至 Nivo Bump 图并将其绘制出来

if "data" not in st.session_state:
    st.session_state.data = Path("data.json").read_text()

# 定义默认的仪表盘布局
# 默认情况下仪表盘会分为 12 列
#
# 更多可用参数见：
# https://github.com/react-grid-layout/react-grid-layout#grid-item-props

layout = [
    # 编辑器对象定位在坐标 x=0 且 y=0 处，占据 12 列中的 6 列以及 3 行
    dashboard.Item("editor", 0, 0, 6, 3),
    # 图表对象定位在坐标 x=6 且 y=0 处，占据 12 列中的 6 列以及 3 行
    dashboard.Item("chart", 6, 0, 6, 3),
    # 媒体播放器对象定位在坐标 x=0 且 y=3 处，占据 12 列中的 6 列以及 4 行
    dashboard.Item("media", 0, 3, 12, 4),
]

# 创建显示各元素的框体

with elements("demo"):

    # 使用以上指定的布局创建新仪表盘
    #
    # draggableHandle 是一个 CSS 查询选择器，定义了仪表盘中可拖拽的部分
    # 以下为将带 'draggable' 类名的元素变为可拖拽对象
    #
    # 更多仪表盘网格相关的可用参数请见：
    # https://github.com/react-grid-layout/react-grid-layout#grid-layout-props
    # https://github.com/react-grid-layout/react-grid-layout#responsive-grid-layout-props

    with dashboard.Grid(layout, draggableHandle=".draggable"):

        # 第一个卡片，代码编辑器
        #
        # 我们使用 'key' 参数来选择正确的仪表盘对象
        #
        # 为了让卡片的内容自动填充占满全部高度，我们将使用 flexbox CSS 样式
        # sx 是所有 Material UI 组件均可使用的参数，用于定义其 CSS 属性
        #
        # 有关卡片、flexbox 和 sx 的更多信息，请见：
        # https://mui.com/components/cards/
        # https://mui.com/system/flexbox/
        # https://mui.com/system/the-sx-prop/

        with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):

            # 为了让标题可拖拽，我们只需要将其类名设为 'draggable'
            # 与 dashboard.Grid 当中 draggableHandle 的查询选择对应

            mui.CardHeader(title="Editor", className="draggable")

            # 要使卡片内容占满全高，我们需要将 CSS 样式中 flex 的值设为 1
            # 同时我们也想要卡片内容随卡片缩放，因此将其 minHeight 设为 0

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 以下是我们的 Monaco 代码编辑器
                #
                # 首先，我们将其默认值设为之前初始化好的 st.session_state.data
                # 其次，我们将设定所用的语言，这里我们设为 JSON
                #
                # 接下来，我们想要获取编辑器中内容的变动
                # 查阅 Monaco 文档后，我们发现可以用 onChange 属性指定一个函数
                # 这个函数会在每次变动发生后被调用，并且变更后的内容将被传入函数
                # (参考 onChange: https://github.com/suren-atoyan/monaco-react#props)
                #
                # Streamlit Elements 提供了一个特殊的 sync() 函数
                # 能够创建一个自动将其参数同步到 Streamlit 会话状态的回调函数
                #
                # 样例
                # --------
                # 创建一个自动将第一个参数同步至会话状态中 "data" 的回调函数：
                # >>> editor.Monaco(onChange=sync("data"))
                # >>> print(st.session_state.data)
                #
                # 创建一个自动将第二个参数同步至会话状态中 "ev" 的回调函数：
                # >>> editor.Monaco(onChange=sync(None, "ev"))
                # >>> print(st.session_state.ev)
                #
                # 创建一个自动将两个参数同步至会话状态的回调函数：
                # >>> editor.Monaco(onChange=sync("data", "ev"))
                # >>> print(st.session_state.data)
                # >>> print(st.session_state.ev)
                #
                # 那么问题来了：onChange 会在每次发生变动时被调用
                # 那么意味着每当你输入一个字符，整个 Streamlit 应用都会重新运行
                #
                # 为了避免这个问题，可以使用 lazy() 令 Streamlit Elements 等待其他事件发生
                # （比如点击按钮）然后再将更新后的数据传给回调函数
                #
                # 有关 Monaco 其他可用参数的说明，请见：
                # https://github.com/suren-atoyan/monaco-react
                # https://microsoft.github.io/monaco-editor/api/interfaces/monaco.editor.IStandaloneEditorConstructionOptions.html

                editor.Monaco(
                    defaultValue=st.session_state.data,
                    language="json",
                    onChange=lazy(sync("data"))
                )

            with mui.CardActions:

                # Monaco 编辑器已经将一个延迟回调函数绑定至 onChange 了，因此即便你更改了 Monaco 的内容
                # Streamlit 也不会立刻接收到，因此不会每次都重新运行
                # 因此我们需要另一个非延迟的事件来触发更新
                #
                # 解决方法就是创建一个在点击时回调的按钮
                # 我们的回调函数实际上不需要做任何事
                # 你可以创建一个空的函数，或者直接使用不带参数的 sync()
                #
                # 然后每当你点击按钮的时候，onClick 回调函数会被调用
                # 而期间其他延迟调用了的回调函数也会被一并执行

                mui.Button("Apply changes", onClick=sync())

        # 第二个卡片，Nivo Bump 图
        # 我们将使用和第一个卡片同样的 flexbox 配置来自动调整内容高度

        with mui.Card(key="chart", sx={"display": "flex", "flexDirection": "column"}):

            # 为了让标题可拖拽，我们只需要将其类名设为 'draggable'
            # 与 dashboard.Grid 当中 draggableHandle 的查询选择对应

            mui.CardHeader(title="Chart", className="draggable")

            # 和前面一样，我们想要让我们的内容随着用户缩放卡片而缩放
            # 因此将 flex 属性设为 1，minHeight 设为 0

            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 以下我们将绘制 Bump 图
                #
                # 在这个练习里，我们就借用一下 Nivo 的示例，将其用在 Streamlit Elements 里面
                # Nivo 的示例可以在这里此页面的 'code' 标签页中找到：https://nivo.rocks/bump/
                #
                # data 参数接收一个字典，因此我们需要用 `json.loads()` 将 JSON 数据从字符串转化为字典对象
                #
                # 有关更多其他类型的 Nivo 图表，请见：
                # https://nivo.rocks/

                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )

        # 仪表盘的第三个元素是媒体播放器

        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="Media Player", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

                # 这个元素实现基于 ReactPlayer，它支持很多除了 YouTube 以外的媒体
                # 你能在这里查看完整列表：https://github.com/cookpete/react-player#props

                media.Player(url=media_url, width="100%", height="100%", controls=True)


#









