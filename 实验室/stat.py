with open("/Users/sunbaile/myHexoBlog/实验室/logs",'r+') as f:
    lines = f.readlines()
print(lines)

error = 0
correct = 0
cnt = 0
for i in lines:
    if i == '200\n':
        correct+=1
    if i == 'status_code错误 404\n':
        error+=1
    cnt+=1
print("error",error)
print("correct",correct)
print("cnt",cnt)