# encoding: utf-8
__author__ = '4faramita'

import urllib2
from bs4 import BeautifulSoup

result_i = ''
result_a = ''
title = ''

url_i = raw_input('please input the URL of a iOS app (n for no iOS version)\n')
url_a = raw_input('please input the URL of a Android app(n for no Android version)\n')

#iOS
#url_i = 'https://itunes.apple.com/hk/app/wechat/id414478124?mt=8'

if url_i.find('itunes.apple.com') != -1:

	#url 输入与转换
	if url_i.find('/us/') != -1:
		url_i =  url_i.replace('/us/','/cn/')
	elif url_i.find('/jp/') != -1:
		url_i =  url_i.replace('/jp/','/cn/')
	elif url_i.find('/hk/') != -1:
		url_i =  url_i.replace('/hk/','/cn/')
	else:
		url_i =  url_i
	#下一版本加入更精确的矫正
	#print (url_i)


	html_i = urllib2.urlopen(url_i).read()
	soup_i = BeautifulSoup(html_i,"lxml")

	# title_i
	title_i = soup_i.h1.string
	title_i_u = title_i.encode('utf-8')
	#print (title_i)

	# ver_i
	ver_i = soup_i.find(itemprop="operatingSystem").string.split(' ')[2]
	ver_i_u = ver_i.encode('utf-8')
	#print (ver_i_u)

	# device_i
	if html_i.find('与 iPhone、iPad、iPod touch 兼容') != -1:
		device_i = 'iPhone 和 iPad'
	elif html_i.find('与 iPad 兼容') != -1:
		device_i = 'iPad'
	else:
		device_i = 'iPhone'
	#print (device_i)

	# size_i
	size_i = html_i.split('<span class="label">大小： </span>')[1][0:10].split('</')[0]
	#print (size_i)


	# price_i
	price_i = soup_i.find(itemprop="price").string
	price_i_u = price_i.encode('utf-8')
	#print (price_i)

	# iap_i
	if html_i.find('热门 App 内购买项目') == -1:
		iap_i = False
	else:
		iap_i = True

	#result_i

	if price_i == u'免费':
		if iap_i == False:
			result_i = '「'+title_i_u+'」适用于 iOS '+ver_i_u+'+ 的 '+device_i+'，大小 '+size_i+'，完全免费。' 
		else:
			result_i = '「'+title_i_u+'」适用于 iOS '+ver_i_u+'+ 的 '+device_i+'，大小 '+size_i+'，免费有内购。' 
	else:
		result_i = '「'+title_i_u+'」适用于 iOS '+ver_i_u+'+ 的 '+device_i+'，大小 '+size_i+'，售价 '+price_i_u+'。'


#Android
#url_a = 'https://play.google.com/store/apps/details?id=com.tencent.mm'
if url_a.find('play.google.com') != -1:

	#url 输入与转换
	if url_a.find('&hl='):
		url_a = url_a.split('&hl=')[0]
	#print (url)

	html_a = urllib2.urlopen(url_a).read()
	soup_a = BeautifulSoup(html_a,"lxml")

	# title_a
	title_a = soup_a.title.string.split('- Google Play')[0].strip()
	title_a_u = title_a.encode('utf-8')
	#print (title_a_u)

	# ver_a
	ver_a = soup_a.find(itemprop="operatingSystems").string.strip().split(u'及')[0]
	ver_a_u = ver_a.encode('utf-8')
	#print (ver_a_u)

	# size_a
	size_a = soup_a.find(itemprop="fileSize").string.strip().split('M')[0]
	size_a_u = size_a.encode('utf-8')
	#print (size_a_u)

	# price_a
	price_a = '0'
	#price_a = '0'
	if html_a.find('<span>安装</span>') == -1:
		position = html_a.find('<span>￥')
		price_a = html_a[position:position+30].split('<span>')[1].split(' ')[0]
	#price_a_u = price_a.encode('utf-8')

	#print (price_a)

	# iap_a
	if html_a.find('提供应用内购买内容') == -1:
		iap_a = False
	else:
		iap_a = True
	#print (iap_a)

	#result_a
	if price_a == '0':
		if iap_a == False:
			result_a = '「'+title_a_u+'」适用于 Android '+ver_a_u+'+ 的设备，大小 '+size_a_u+' MB，完全免费。'
		else:
			result_a = '「'+title_a_u+'」适用于 Android '+ver_a_u+'+ 的设备，大小 '+size_a_u+' MB，免费有内购。'
	else:
		result_a = '「'+title_a_u+'」适用于 Android '+ver_a_u+'+ 的设备，大小 '+size_a_u+' MB，售价 '+price_a+'。'
	if result_a.find('因设备而异+') != -1:
		result_a = result_a.replace('因设备而异+ 的','')
	if result_a.find('大小 因设备而异') != -1:
		result_a = result_a.replace('大小 因设备而异 MB','大小因设备而异')


if url_i == 'n':
	print (result_a)
elif url_a == 'n':
	print (result_i)
else:
	if price_i == u'免费':
		if iap_i == False:
			result = '「'+title_i_u+'」适用于 iOS '+ver_i_u+'+ 的 '+device_i+' 及 Android '+ver_a_u+'+ 的设备，iOS 版 '+size_i+'，完全免费，Android 版 '+size_a_u+' MB，售价 '+price_a+' 元。' 
		else:
			result = '「'+title_i_u+'」适用于 iOS '+ver_i_u+'+ 的 '+device_i+' 及 Android '+ver_a_u+'+ 的设备，iOS 版 '+size_i+'，免费有内购，Android 版 '+size_a_u+' MB，售价 '+price_a+' 元。' 
	else:
		result = '「'+title_i_u+'」适用于 iOS '+ver_i_u+'+ 的 '+device_i+' 及 Android '+ver_a_u+'+ 的设备，iOS 版 '+size_i+'，售价 '+price_i_u+'，Android 版 '+size_a_u+' MB，售价 '+price_a+' 元。'
	if result.find('因设备而异+') != -1:
		result = result.replace('因设备而异+ 的','')
	if result.find(' 因设备而异 MB') != -1:
		result = result.replace(' 因设备而异 MB','大小因设备而异')
	if result.find('售价 0 元') != -1:
		if iap_a == False:
			result = result.replace('售价 0 元','完全免费')
		else:
			result = result.replace('售价 0 元','免费有内购')

	print (result)
