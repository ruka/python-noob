import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json


SAVE_DIR = r"D:\github\python-noob\ai应用\素材\会话信息"


def save_session(ai_name, ai_nature, message):
    # 从 session_state 中读取当前输入值
    if ai_name and ai_nature:
        session_data = {
            "ai_nature": ai_nature,
            "ai_name": ai_name,
            "message": st.session_state.get("message", []),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        os.makedirs(SAVE_DIR, exist_ok=True)
        filename = os.path.join(
            SAVE_DIR, f"{ai_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)
        st.success("会话已保存！")
    else:
        st.warning("请先填写昵称和个性/人设")


def get_sessions():
    """扫描保存目录，返回会话列表（按时间倒序）"""
    os.makedirs(SAVE_DIR, exist_ok=True)
    sessions = []
    for filename in os.listdir(SAVE_DIR):
        if filename.endswith(".json"):
            filepath = os.path.join(SAVE_DIR, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)
                sessions.append({
                    "filename": filename,
                    "ai_name": data.get("ai_name", "未知"),
                    "timestamp": data.get("timestamp", "未知时间"),
                    "message_count": len(data.get("message", []))
                })
            except (json.JSONDecodeError, KeyError):
                continue
    sessions.sort(key=lambda s: s["timestamp"], reverse=True)
    return sessions


def load_session_file(filename):
    """加载指定会话文件"""
    filepath = os.path.join(SAVE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    st.session_state.message = data.get("message", [])
    st.session_state.ai_name = data.get("ai_name", "")
    st.session_state.ai_nature = data.get("ai_nature", "")
    st.success(f"已加载会话：{data.get('ai_name', '')}")


def delete_session_file(filename):
    """删除指定会话文件"""
    filepath = os.path.join(SAVE_DIR, filename)
    os.remove(filepath)
    st.success(f"已删除会话：{filename}")


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
    # 保存会话
    if st.button("开始新的对话", use_container_width=True):
        ai_name = st.session_state.get("ai_name", "")
        ai_nature = st.session_state.get("ai_nature", "")
        save_session(ai_name, ai_nature, st.session_state.message)

        st.session_state.message = []
        st.session_state.current_message = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.header("历史会话")
    sessions = get_sessions()
    if sessions:
        for session in sessions:
            col1, col2, col3 = st.columns([3, 0.5, 0.5])
            with col1:
                st.write(f"**{session['ai_name']}**")
                st.caption(
                    f"{session['timestamp']} | {session['message_count']} 条消息")
            with col2:
                if st.button("📂", key=f"load_{session['filename']}", help="加载会话"):
                    st.session_state["pending_load"] = session['filename']
                    st.rerun()
            with col3:
                if st.button("🗑️", key=f"del_{session['filename']}", help="删除会话"):
                    delete_session_file(session['filename'])
                    st.rerun()
    else:
        st.caption("暂无保存的会话")

    # 处理待加载的会话（在按钮回调外执行，确保状态同步正确）
    if st.session_state.get("pending_load"):
        filename = st.session_state.pop("pending_load")
        load_session_file(filename)
        st.rerun()

    st.header("AI控制器")

    ai_name = st.text_input(
        "昵称", value=st.session_state.get("ai_name", ""), key="ai_name")
    ai_nature = st.text_area(
        "个性/人设", value=st.session_state.get("ai_nature", ""), key="ai_nature")

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
            # 智能体的人设
            {"role": "system",
                "content": f"你的名字是{st.session_state.get('ai_name', 'AI助手')}。{st.session_state.get('ai_nature', '你是一个有帮助的AI助手。')}"},
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
