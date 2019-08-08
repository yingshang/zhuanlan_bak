import requests
from bs4 import BeautifulSoup
import os
import pdfkit
import re
BASE_DIR = os.getcwd()

# page = input("please input crawl page")
page = 3
for i in range(0, page):
    url = "https://www.freebuf.com/author/%E9%99%8C%E5%BA%A6?page=" + str(i + 1)
    r = requests.get(url=url)

    soup = BeautifulSoup(r.text, "lxml")

    # JS
    js_html = ""
    for i in range(len(soup.find_all("script"))):
        js_html =js_html+str(soup.find_all("script")[i])+"\n"
        if soup.find_all("script")[i].get("src") != None:

            js_url = soup.find_all("script")[i].get("src")
            js_name = js_url.split('?')[0].split('/')[-1]
            js_path = js_url.split('?')[0].split('/')[3:-1]
            try:
                os.mkdir("static")
            except FileExistsError:
                pass
            try:
                os.makedirs("static/" + '/'.join(js_path))
            except FileExistsError:
                pass
            if js_url.split('/')[2] == "static.3001.net":
                if os.path.isfile("static/" + '/'.join(js_path) + "/" + js_name) == False:
                    os.system("wget -O " + "static/" + '/'.join(js_path) + "/" + js_name + "  " + js_url.split('?')[0])

            elif js_url.split('/')[2] == "www.freebuf.com":
                headers = {
                    "Host": "www.freebuf.com",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
                    "Accept": "*/*",
                    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Referer": "https://www.freebuf.com/column/149807.html",
                    "Connection": "keep-alive",
                    "Cookie": "acw_tc=2760823715651430204251399efb7ce2008f65e6aa7f8b18dede83f4765802; 3cb185a485c81b23211eb80b75a406fd=1565143022; PHPSESSID=o68pjrjqhbdnrg8rfcd6knhgv3; Hm_lvt_cc53db168808048541c6735ce30421f5=1565143020; Hm_lpvt_cc53db168808048541c6735ce30421f5=1565143020",
                    "If-Modified-Since": "Fri, 26 Oct 2018 12:46:18 GMT",
                    "If-None-Match": "5bd30c9a-189f",
                    "Cache-Control": "max-age=0",
                }
                if os.path.isfile("static/" + '/'.join(js_path) + "/" + js_name) == False:
                    r1 = requests.get(url=js_url.split('?')[0], headers=headers)
                    f = open("static/" + '/'.join(js_path) + "/" + js_name, "w")
                    f.write(r1.text)
                    f.close()


            else:
                pass

    # CSS
    css_html = ""
    for i in range(len(soup.find_all("link"))):
        css_html = css_html + str(soup.find_all("link")[i])+'\n'
        css_url = soup.find_all("link")[i].get("href")
        css_name = css_url.split('?')[0].split('/')[-1]
        css_path = css_url.split('?')[0].split('/')[3:-1]
        try:
            os.makedirs("static/" + '/'.join(css_path))
        except FileExistsError:
            pass

        if css_url.split('/')[2] == "static.3001.net":
            if os.path.isfile("static/" + '/'.join(css_path) + "/" + css_name) == False:
                os.system(
                    "wget -O " + "static/" + '/'.join(css_path) + "/" + css_name + "  " + css_url.split('?')[0])

        elif css_url.split('/')[2] == "www.freebuf.com":
            headers = {
                "Host": "www.freebuf.com",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://www.freebuf.com/column/149807.html",
                "Connection": "keep-alive",
                "Cookie": "acw_tc=2760823715651430204251399efb7ce2008f65e6aa7f8b18dede83f4765802; 3cb185a485c81b23211eb80b75a406fd=1565143022; PHPSESSID=o68pjrjqhbdnrg8rfcd6knhgv3; Hm_lvt_cc53db168808048541c6735ce30421f5=1565143020; Hm_lpvt_cc53db168808048541c6735ce30421f5=1565143020",
                "If-Modified-Since": "Fri, 26 Oct 2018 12:46:18 GMT",
                "If-None-Match": "5bd30c9a-189f",
                "Cache-Control": "max-age=0",
            }
            if os.path.isfile("static/" + '/'.join(css_path) + "/" + css_name) == False:
                r1 = requests.get(url=css_url.split('?')[0], headers=headers)
                f = open("static/" + '/'.join(css_path) + "/" + css_name, "w")
                f.write(r1.text)
                f.close()


    static_html = '<head> <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> </head>'+js_html+'\n'+css_html
    static_html = static_html.replace("https://static.3001.net","static").replace("https://www.freebuf.com","static")



    for i in range(len(soup.find_all("dl")[0].find_all("dd"))):
    #for i in range(1):
        url2 = soup.find_all('dd')[i].a.get("href")
        name = soup.find_all('dd')[i].a.string

        r1 = requests.get(url=url2)
        #try:
        s = re.findall('<div id="contenttxt">[\S\s]*?<div class="wechatcodeDiv">',r1.text)[0]
        #except IndexError:
        #    soup1 = BeautifulSoup(r1.text, "lxml")
        #    s = str(soup1.find('div', {'id': 'contenttxt'}))
        for i in range(len(re.findall('<img.*?data-original="(.*?)".*?>', s))):
            img_path = re.findall('<img.*?data-original="(.*?)".*?>', s)[i]
            pattern = r'<img.*?data-original="' + img_path + '"' + ".*?>"
            find_img = re.findall(pattern, s)[0].replace("https://www.freebuf.com/buf/themes/freebuf/images/grey.gif",
                                                         img_path)
            imgages_path = '/'.join(img_path.split('/')[3:-1])
            try:
                os.makedirs(imgages_path)
            except FileExistsError:
                pass
            if os.path.isfile(imgages_path + "/" + img_path.split('/')[-1].split('!')[0]) == False:
                os.system("wget -O " + imgages_path + "/" + img_path.split('/')[-1].split('!')[0] + " " + img_path.split('!')[0])
            s = s.replace(re.findall(pattern, s)[0], find_img)


        for i in range(len(re.findall('<img [alt|style].*?src="(.*?)".*?>', s))):
            img_path = re.findall('<img [alt|style].*?src="(.*?)".*?>', s)[i]

            imgages_path = '/'.join(img_path.split('/')[3:-1])
            try:
                os.makedirs(imgages_path)
            except FileExistsError:
                pass
            if os.path.isfile(imgages_path + "/" + img_path.split('/')[-1].split('!')[0]) == False:
                os.system("wget -O " + imgages_path + "/" + img_path.split('/')[-1].split('!')[0] + " " + img_path.split('!')[0])



        f = open(name+".html","w")
        f.write(static_html+"\n"+s.replace('https://image.3001.net/','').replace("!small","").replace('<div class="column-tags"><a href="https://zhuanlan.freebuf.com">专栏</a></div>','').replace("!",''))
        f.close()


