"""
Python 2.7 & RHEL7.1 & fs:xfs
"""


# coding:utf-8
import urllib

domain = 'http://www.liaoxuefeng.com'           #廖雪峰的域名
path = r'/tmp/pythoncrawler1.result/'    #html要保存的路径

# 一个html的头文件
#input = open(r'', 'r')
#head = input.read()

# 打开python教程主界面
f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
home = f.read()
f.close()
#print "home: "+home

# 替换所有空格回车（这样容易好获取url）
geturl = home.replace("\n", "")
geturl = geturl.replace(" ", "")

# 得到包含url的字符串
list = geturl.split(r'em;"><ahref="')[1:]

# 强迫症犯了，一定要把第一个页面也加进去才完美
list.insert(0, '/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')

# 开始遍历url List
for li in list:
    url = li.split(r'">')[0]
    url = domain + url              #拼凑url
    print url
    f = urllib.urlopen(url)
    html = f.read()

    # 获得title为了写文件名
    title = html.split("<title>")[1]
    title = title.split(" - 廖雪峰的官方网站</title>")[0]

    # 要转一下码，不然加到路径里就悲剧了
    #title = title.decode('utf-8')
    """
    under python 2.7:
    we get utf-8 from html and Linux's file name is OK with utf-8 code.
    So, no need to decode here.
    """
    #print "title" + "%s" % title
    title = title.replace("/", "_")
    #print "title" + "%s" % title

    output = open(path + "%d" % list.index(li), 'w')
    output.write(html)
    output.close()


    # 截取正文
    html = html.split(r'<div class="x-wiki-content">')[1]
    html = html.split(r'<div id="x-wiki-prev-next"')[0]
    #html = html.split(r'<h3>分享给朋友</h3>')[0]
    #html = html.replace(r'src="', 'src="' + domain)

    # 加上头和尾组成完整的html
 #   html = head + html+"</body></html>"

    # 输出文件
    #print title
    output = open(path + "%d" % list.index(li) + title + '.html', 'w')
    output.write(html)
    output.close()
