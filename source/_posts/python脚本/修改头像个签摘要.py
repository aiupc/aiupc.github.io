from cmath import e
import os
import re
from tkinter import E

conf = {
    "孙百乐": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/孙百乐头像.jpg","读万卷书，行万里路"],
    "孙鹏程": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/孙鹏程头像.jpg", "昨晚上大分"],
    "蒋月宁": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/蒋月宁头像.jpg", "都别争了无限大人是我老婆"],
    "留欣阁": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/班徽压缩.png", "求真,务实,快乐,有为"],
    "代鹏" : ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/代鹏头像.jpg", "这个人什么也没写"],
    "张耀翔": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/张耀翔头像.png", "这个人什么也没写"],
    "苏唯靖": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/苏唯靖头像.jpg", "这个人什么也没写"],
    "刘原歌": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/刘原歌头像.jpg", "这个人什么也没写"],
    "万舒成": ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/万舒成头像.jpg", "这个人什么也没写"],
    "何为" : ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/何为头像.jpg", "这个人什么也没写"],
    "郑啸" : ["https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/郑啸头像.jpg", "这个人什么也没写"],
}

# ['---\n', 'title: 3.19查寝通知\n', 'author: 万舒成\n', 'avatar: \n', 'authorLink: \n', 'authorAbout: \n', 'authorDesc: \n', 'categories: 班级周记\n', 'comments: true\n', 'tags: []\n', "id: '723'\n", 'date: 2021-03-19 17:11:50\n', 'keywords:\n', 'description:\n', 'photos:\n', '---\n', '\n', '作为开学第一次查寝，感觉还是不错的，大家并没有将宿舍搞得很乱。被子情况的话还是有一部分同学没有叠，这里特别表扬一下刘逸霄同学叠了被子，希望继续保持。宿舍位置上也没有闻到异味，说明大家袜子都比较及时清洗了，室内空气还是比较重要的。接下来也就是比较多问题的就是杂物比较多看起来就比较乱，希望大家以后有什么不要的东西及时清理，不要堆积。 查寝评分如下 [![](https://www.aiupc.xyz/wp-content/uploads/2021/03/wp_editor_md_a7d76ff6ad33798d82f64a7740f5612d.jpg)](https://www.aiupc.xyz/wp-content/uploads/2021/03/wp_editor_md_a7d76ff6ad33798d82f64a7740f5612d.jpg)']

path = "/Users/sunbaile/myHexoBlog/source/_posts/"
for file in os.listdir(path):
    if file[-3:]==".md":
        try:
            with open(os.path.join(path,file),"r") as f:
                lines = f.readlines()
                if lines[15] == "---\n":
                    name = lines[2].split(":")[1].strip()
                    # print(conf[name])
                    lines[3] = "avatar: " + conf[name][0] + "\n"
                    lines[5] = "authorAbout: " + conf[name][1] + "\n"
                    lines[13] = lines[13].replace("#","")
                    if len(lines[13])<15:
                        substr = re.sub(r"(\!\[.*?\]\(.*?\))|\n","",lines[17])
                        if len(substr) > 50:
                            lines[13] = "description: " + substr[:50] + "...\n"
                        else:
                            lines[13] = "description: " + substr + "\n"
                else:
                    print(file)
            with open(os.path.join(path,file),"w+") as f2:
                f2.writelines(lines)
        except Exception(e):
            print(e)
            print("error",file)