
import time
#import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt

st.title("This is my first app")
st.write("hello")
st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
    'first column': [5, 6, 7, 8],
    'second column': [50, 60, 70, 80]
})

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
# 其中df定义的位置，并不影响最后的输出位置！
# df

# 绘制图表
# 折线图
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# 区域图的可视化
# “streamlit”中的“area_chart”方法显示区域图，方法原型和折线图用到的方法一致，所以这里就不做过多的赘述，例如下面的代码

chart_data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

# 柱状图的可视化
# “streamlit”的“bar_chart()”方法显示柱状图，例如下面的代码

chart_data = pd.DataFrame(np.random.randn(50, 3),
                          columns=['a', 'b', 'c'])
st.bar_chart(chart_data)

# 显示图像
# “streamlit”中的“image”方法可以用来显示一张或多张图像，其中的方法原型，

# streamlit.image(image, caption=None, width=None, use_column_width=False, clamp=False, channels='RGB', format='JPEG')
# 参数:
# image：要显示的图像，类型可以是numpy.ndarray, [numpy.ndarray], BytesIO, str, 或 [str]) – 单色图像为(w,h) 或 (w,h,1)
# 彩色图像为(w,h,3)
# RGBA图像为(w,h,4)
# 也可以指定一个图像url，或url列表
# caption：图像标题，字符串。如果显示多幅图像，caption应当是字符串列表
# width ：图像宽度，None表示使用图像自身宽度
# use_column_width：如果设置为True，则使用列宽作为图像宽度
# clamp：是否将图像的像素值压缩到有效域（0~255） ，仅对字节数组图像有效。
# channels：图像通道类型，'RGB' 或 'BGR'，默认值：RGB
# format：图像格式：'JPEG' 或'PNG')，默认值：JPEG


# 绘制一个地图
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
#
# st.map(map_data)

# 调整地图的中心到沈阳
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [41.8, 123.4],
    columns=['lat', 'lon'])
st.map(map_data)

# 增加交互性，显示单选框
# st.checkbox()**单选框，更多请查询API reference

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    chart_data
# 增加复选框
option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected: ', option

# 调整布局
# 为了使得你的webApp更加好看，你可以将一些不必要的内容放置到其他区域。这样可以使得你的webApp居中。
# **st.sidebar()**将刚才的边框设置在左侧
# tips：可以发现每次选择不同的数字，整个页面都会刷新，包括刚才设置的地图上的点也会跟着刷新，和刚才的折线图

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# 你也可以使用st.beta_columns来并排布置小部件，或者使用st.beta_expander来隐藏大型内容以节省空间

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

# 添加进度条
# 当在一个应用程序中添加长期运行的计算时，你可以使用st.progress()来实时显示状态。
# 首先，让我们导入时间。我们将使用time.sleep()方法来模拟一个长期运行的计算
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...and now we\'re done!'


# 现在让我们使用st.echo()让中间部分的代码可视化：
# st.echo - 显示应用源代码
# 在with块中使用streamlit的echo方法显示应用源代码，然后执行。

def get_user_name():
    return 'John'


with st.echo():
    # Everything inside this block will be both printed to the screen
    # and executed.

    def get_punctuation():
        return '!!!'


    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')

# st.pyplot - 显示pyplot图表
# streamlit的pyplot方法显示指定的matplotlib.pyplot图表。
#
# 方法原型
# streamlit.pyplot(fig=None, **kwargs)
# 参数：
# fig：要使用的绘制面板，当为None时，使用整个绘图区域
# **kwargs ：传入Matplotlib的savefig函数的关键字参数


# st.vega_lite_chart
# Streamlit Version   v1.1.0
# Display a chart using the Vega-Lite library.

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

# st.altair - 显示altair图表
# streamlit的altair方法使用Altair库显示指定的图表。
#
# 方法原型
# streamlit.altair_chart(altair_chart, width=0)
# 参数：
#
# altair_chart：要显示的Altair图表对象，类型：altair.vegalite.v2.api.Chart
# width：宽度模式，0 表示拉伸图表到文档宽度，-1表示使用Altair的默认值，大于0表示 设置的宽度像素。默认值：0。注意如果顶层宽度已定义，那么将覆盖这里的设定。
# 示例代码

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c')
st.altair_chart(c, use_container_width=True)

