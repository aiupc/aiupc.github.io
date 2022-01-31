import os


path = "/Users/sunbaile/myHexoBlog/source/_posts/"
num = 0
for file in os.listdir(path):
    if file[-3:]==".md":
        with open(os.path.join(path,file),"r+") as f:
            lines = f.readlines()
            i = 0
            while "photos:" not in lines[i]:
                i += 1
            print(lines[i])
            split = lines[i].split(":",1)
            lines[i] = split[0].strip() + ": " + split[1].strip() + "\n"
        with open(os.path.join(path,file),"r+") as f2:
            f2.writelines(lines)