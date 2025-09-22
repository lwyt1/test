# file_path = './新建文本文档.txt'  #文件位置

# try:
#     file = open(file_path,'r',encoding='utf-8') #打开txt文件
#     content = file.read()  #读取内容
#     file.close() #关闭文件
#     text = content
#     groups = [text[i:i + 30] for i in range(0, len(text), 30)]
#     new_text = "\n".join(groups)
#     print(new_text)

# except FileNotFoundError:
#      print("文件不存在")

print("nihao ")

#
# from datetime import datetime
# import time
#
# timestamp = 1702861200
# local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
# print("开始时间：",local_time)
#
# current_time = datetime.now()
# print("当前时间：", current_time)
#
# current_time = time.time()
# print("当前时间戳：", current_time)
#

# a=(current_time-timestamp)
# print("已经过了多少秒：",a)


# import threading
# import time
#
# def click_button():
#     # 模拟点击按钮的操作，这里可以替换为实际的业务逻辑
#     time.sleep(0.01)
#     print("按钮被点击")
#
# # 创建200个线程，每个线程模拟一个用户点击按钮
# threads = []
# for i in range(100):
#     t = threading.Thread(target=click_button)
#     threads.append(t)
#     t.start()
#
# # 等待所有线程执行完毕
# for t in threads:
#     t.join()

# print("所有用户点击按钮完成")
