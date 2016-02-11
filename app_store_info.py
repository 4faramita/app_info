#-*- coding:utf-8 -*-

import urllib2
from bs4 import BeautifulSoup

#url = 'https://itunes.apple.com/cn/app/carcassonne/id375295479?mt=8'

#url 输入与转换
url_r = raw_input('please input the url of the app\n'
)

if url_r.find('/us/') != -1:
	url =  url_r.replace('/us/','/cn/')
elif url_r.find('/jp/') != -1:
	url =  url_r.replace('/jp/','/cn/')
elif url_r.find('/hk/') != -1:
	url =  url_r.replace('/hk/','/cn/')
else:
	url =  url_r
#下一版本加入更精确的矫正
#print (url)


html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")

# title
title = soup.h1.string
title_u = title.encode('utf-8')
#print (title)

# ver
ver_r = soup.find(itemprop="operatingSystem").string
ver = ver_r.split(' ')[2]
ver_u = ver.encode('utf-8')
#print (ver)

# device
if html.find('与 iPhone、iPad、iPod touch 兼容') != -1:
	device = 'iPhone 和 iPad'
elif html.find('与 iPad 兼容') != -1:
	device = 'iPad'
else:
	device = 'iPhone'
#print (device)

# space
space_r = html.split('<span class="label">大小： </span>')[1][0:10]
space = space_r.split('</')[0]
#print (space)


# price
price = soup.find(itemprop="price").string
price_u = price.encode('utf-8')
#print (price)

# iap
if html.find('热门 App 内购买项目') == -1:
	iap = False
else:
	iap = True

#result

if price == u'免费':
	if iap == False:
		result = '「'+title_u+'」适用于 iOS '+ver_u+' 的 '+device+'，大小 '+space+'，完全免费。' 
	else:
		result = '「'+title_u+'」适用于 iOS '+ver_u+' 的 '+device+'，大小 '+space+'，免费有内购。' 
else:
	result = '「'+title_u+'」适用于 iOS '+ver_u+' 的 '+device+'，大小 '+space+'，售价 '+price_u+'。'


print (result)
