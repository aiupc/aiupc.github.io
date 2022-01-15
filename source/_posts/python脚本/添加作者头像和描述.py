import os

path = "/Users/sunbaile/myHexoBlog/source/_posts/"
for file in os.listdir(path):
    if file[-3:]==".md":
        try:
            with open(os.path.join(path,file),"r") as f:
                if f.readlines()[15]!="---\n":
                    print(file)
        except:
            print("error",file)