import requests
import os
import re


def download_img(img_url, path):
    filename = img_url[img_url.rindex("/") + 1:]
    # print (filename)
    try:
        r = requests.get(img_url, stream=True)
        # print(r.status_code)  # 返回状态码
        if r.status_code == 200:
            f = open(f'/Users/sunbaile/myHexoBlog/实验室/{filename}', 'wb').write(r.content)
            return True
        else:
            print("status_code错误", r.status_code)
            return False
    except:
        print("下载失败", filename)
        return False


def get_pic_name(img_url):
    return img_url[img_url.rindex("/") + 1:]


if __name__ == '__main__':
    dir_path = "/Users/sunbaile/myHexoBlog/source/_posts/"
    cnt = 0
    for file in os.listdir(dir_path):
        cnt += 1
        if file[-3:] == ".md":
            with open(os.path.join(dir_path, file), "r+") as f:
                text = f.read()

            url_lst = re.findall('!\[.*?\]\((.*?)\)', text)
            # print(url_lst)
            for url in url_lst:
                if "aiupc" in url:
                    ret = download_img(url, dir_path)
                    if ret:
                        text = text.replace(url, f"https://cdn.jsdelivr.net/gh/aiupc/drawingbed/img/{get_pic_name(url)}")
            with open(os.path.join(dir_path, file), "w+") as f2:
                f2.write(text)
            print(f"{cnt}.{file},替换{len(url_lst)}个")

