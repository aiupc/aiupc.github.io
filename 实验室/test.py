import os

path = "/Users/sunbaile/myHexoBlog/实验室/井号文本.md"
with open(path,"r+") as f:
    lines = f.readlines()
    lines[0] = lines[0].replace("#","")
    print(lines)