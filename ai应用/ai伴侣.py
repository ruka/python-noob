import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="ai智能伴侣",
    page_icon="💩",
    layout="centered",
    initial_sidebar_state="expanded",  # 控制侧边栏
    menu_items={
        'About': "这是一个ai智能伴侣"
    }
)
# 大标题
st.title("ai智能伴侣")

# 初始化聊天框
if "message" not in st.session_state:
    st.session_state.message = []
# 展示聊天框
for message in st.session_state.message:
    if message["role"] == "user":  # 用户
        st.chat_message("user").write(message["content"])
    else:                         # ai
        st.chat_message("assistant").write(message["content"])

# logo
st.logo("https://oss.5eplay.com/cloudx/p/sport/csgo/team/merge_d818n3cconkpudhr4jmg.png?x-oss-process=image/indexcrop,x_300,i_1/resize,h_150,m_lfit")

# 侧边栏设置
with st.sidebar:
    st.sidebar.title("AI智能伴侣您的智能好伙伴")
    ai_name = st.text_input("昵称")
    ai_nature = st.text_area("个性/人设")

text = f"你的名字叫{ai_name},{ai_nature}"

# 调用deepseek大模型
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


# 聊天框
prompt = st.chat_input("Say something")
if prompt:
    st.chat_message("user").write(prompt)  # 输出用户输入
    print(f"用户输出的是：{prompt}")
    # 保存用户输入
    st.session_state.message.append({"role": "user", "content": prompt})
    # 大模型的交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": text},  # 智能体的人设
            # {"role": "user", "content": prompt},  # 用户提示词
            *st.session_state.message  # 解包所存储的所有信息
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 输出大模型返回的内容(输出格式为非流式方式)
    # print(f"大模型输出的是：{response.choices[0].message.content}")
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的内容(输出格式为流式方式)
    full_content = ""
    with st.chat_message("assistant"):
        placeholder = st.empty()
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_content += content
                placeholder.markdown(full_content)

    # 保存大模型返回的内容
    st.session_state.message.append(
        {"role": "assistant", "content": full_content})
