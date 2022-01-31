# 批量重命名

import os
# print("hel")
path = "/Users/sunbaile/myHexoBlog/source/_posts/"
num = 0
for file in os.listdir(path):
    if file[-3:]==".md":
        with open(os.path.join(path,file),"r+") as f:
            text = f.readlines()
            title = text[1].replace("title: ","").replace("\n","")
        os.rename(os.path.join(path,file),os.path.join(path,title+".md"))
        num+=1
        print(f"重命名第{num}个文件:{os.path.join(path,title+'.md')}")
# print(title)

