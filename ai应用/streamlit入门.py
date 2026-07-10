import streamlit as st

st.set_page_config(
    page_title="streamlit演示案例",
    page_icon="🧊",
    layout="centered",  # 页面居中
    initial_sidebar_state="expanded",  # 控制侧边栏
    menu_items={
        'Get Help': 'https://www.baidu.com',  # 跳转链接按钮
        'Report a bug': "https://www.bilibili.com",
        'About': "这是我的第一个streamlit案例"
    }
)

st.title("我的第一个 Streamlit 应用程序")
st.header("这是一级标题")
st.subheader("这是二级标题")
st.write("这是正文内容")
st.image(r"D:\github\python-noob\ai应用\素材\猫.jpg", width=300,)  # 引入图片
st.logo(r"D:\github\python-noob\ai应用\素材\老虎.png")  # logo
st.audio(r"D:\github\python-noob\ai应用\素材\发条玩具mp3_爱给网_aigei_com.mp3")  # 音频
st.video(r"D:\github\python-noob\ai应用\素材\猫咪伸懒腰.mp4")  # 视频播放

# 表格
data = {
    "姓名": ["颜凡", "张三", "李四"],
    "语文": [100, 90, 89],
    "数学": [100, 100, 98],
    "英语": [100, 97, 90],
}
st.table(data)

# 输入
name = st.text_input("请输入您的名字：")  # 文本输入框
st.write(f"您的名字是：{name}")

password = st.text_input("请输入密码：", type="password")
st.write(f"密码是：{password}")

# 单选按钮
st.radio(f"请选择您的性别：", ["man", "woman"])
