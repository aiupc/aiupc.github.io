import os
path = "/Users/sunbaile/myHexoBlog/source/_posts/"
num = 0

for file in os.listdir(path):
    if file[-3:]==".md":
        num += 1
        with open(os.path.join(path+file),"r+") as f:
            lines = f.readlines()
            lines[2] = "author: \n"
            lines[3] = "avatar: \n"
            lines[4] = "authorLink: \n"
            lines[5] = "authorAbout: \n"
            lines[6] = "authorDesc: \n"
            lines[7] = "categories: \n"
        with open(os.path.join(path+file),"w+") as f:
            f.writelines(lines)
        print(f"写入第{num}个",file)
        # print(lines)