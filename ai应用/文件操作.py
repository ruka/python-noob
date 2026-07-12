# 读取文件
f = open("D:\github\python-noob\\ai应用\素材\三字经.txt", 'r', encoding='utf-8')

content = f.read()
print(content)

f.close()


# 写入文件
f = open("D:\github\python-noob\\ai应用\素材\静夜思.txt", 'w', encoding='utf-8')

f.write("静夜思  李白\n\n")
f.write("窗前明月光，\n")
f.write("疑是地上霜。\n")
f.write("举头望明月，\n")
f.write("低头思故乡。")

f.close()


# 资源释放
with open("D:\github\python-noob\\ai应用\素材\静夜思.txt", 'w', encoding='utf-8')as f:

    f.write("静夜思  李白\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。")
