from lxml import html
import requests
import markdown
import re

# create url
root = "http://192.168.0.180:8086/";
begin = requests.get("http://192.168.0.180:8086/index.php?s=/32&page_id=980");
urls = [];

if(begin.status_code == 200):
    html_tree = html.fromstring(begin.text)
    intro_raw = html_tree.xpath('//li/a/@href') # / 表示元素下子标签
    # print("get urls:")
    for url in intro_raw:
        if url.startswith("/index.php?s=/home/page/index/page_id"):
            # print(root + url)
            urls.append(root + url)

    # 根据存放的url开始爬取数据
    for url in urls:
        url_page = requests.get(url);
        url_page_tree = html.fromstring(url_page.text)
        code_path = url_page_tree.xpath('//textarea')
        code_path_h3 = url_page_tree.xpath('//h3')
        for i in range(len(code_path)):
            res_tr = r'`(.*?)`'
            m_tr = re.findall(res_tr, code_path[i].text, re.S | re.M)
            if len(m_tr) != 0:
                print('private final static String '+ m_tr[0].strip().replace("/" , "_").lower() +' = "' + m_tr[0].strip() + '"; // ' + code_path_h3[i].text)

else:
    print(begin.status_code)

