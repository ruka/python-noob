import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")


# 大模型的交互
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个精通计算机的专家，你的名字叫kk"},  # 智能体的人设
        {"role": "user", "content": "61的二进制是多少"},  # 用户提示词
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

# 输出大模型返回的内容
print(response.choices[0].message.content)
