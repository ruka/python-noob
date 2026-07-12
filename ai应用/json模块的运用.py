import json

# 序列化 写入文件
user = {
    "name": "颜凡",
    "hobbit": ["看电影", "看小说"],
    "age": 18,
    "sex": "男",

}
with open("D:\github\python-noob\\ai应用\素材\\user.json", "w", encoding="utf-8") as f:  # 打开文件
    json.dump(user, f, ensure_ascii=False, indent=4)

# 反序列化  读取文件
with open("D:\github\python-noob\\ai应用\素材\\user.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
