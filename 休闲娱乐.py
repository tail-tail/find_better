def web(find):
	import requests
	import re

	head = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
		'Cookie': 'BIDUPSID=8918540DA010B15020E7033AFF56B848; PSTM=1592990274; BAIDUID=8918540DA010B150E24364EF96BC5B3D:FG=1; BD_UPN=12314753; ISSW=1; ISSW=1; BDUSS_BFESS=FpSkRjbnhoUFRxRWtEeTZDdUpmV2xGT0dQTU5UQWwzYkpXa1lsTkdXNlZtQ1pmSUFBQUFBJCQAAAAAAAAAAAEAAACejU86y-nS4sauxq7C0gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJUL~16VC~9eNW; BDUSS=ZCY3pBUkVtd1BGUXB0OFl-d096cTgzc3hzYWNTQ0U3dkFVVGZhVVIzcWFhVFpmSVFBQUFBJCQAAAAAAAAAAAEAAACEc-hyU0pMMTk5MTEyMTYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJrcDl-a3A5faE; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; COOKIE_SESSION=244960_0_1_0_12_0_1_0_1_0_0_0_244985_0_29_0_1595818639_0_1595818610%7C9%230_0_1595992426%7C1%7C1; BDRCVFR[pNjdDcNFITf]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=7; H_PS_645EC=d786CBPV0YzX9iHrIOE4NgQc%2BYu4JsltynzFXmAm39qnd5UDRSHD9fT4%2B9%2BFvk01txn10A; BD_HOME=1; H_PS_PSSID=32293_1445_32379_32045_32399_32117_31321_32298; sug=3; sugstore=1; bdime=0; ORIGIN=2'
	}
	r = requests.get('https://www.baidu.com/s?tn=02049043_8_pg&ch=9&word=' + find, headers=head)
	r.encoding = 'utf-8'
	a = r.text
	b = re.findall(
		r'text-decoration:none;position:relative;"[\s\S]*?>(.*?)</a>|</p><div class="g">(.*?)<div class="c-tools " id="tools_',
		a)
	print(b)
	gd = []
	for i in b:
		for j in i:
			if j != '':
				gd.append(j)
	b = gd
	return b   #含关键词列表


def analyse(b): #分析
	import re

	game=['4399小游戏','4399.com','游侠网','ali213.net','3DMGAME','3dmgame.com','游民星空','gamersky.com']
	novel=['起点中文网','qidian.com','简书','jianshu.com','笔趣阁','biquge.info']
	video=['爱奇艺','iqiyi.com','腾讯视频','v.qq.com','哔哩哔哩','bilibili.com','优酷网','youku.com']
	game0 = 0
	novel0 = 0
	video0=0

	# 越多越智能，速度。。
	for i in b:
		for j in game:
			if re.search(j, i) != None:
				game0 += 1
		for j in novel:
			if re.search(j, i) != None:
				novel0 += 1
		for j in video:
			if re.search(j, i) != None:
				video0 += 1
	sz = [game0, novel0, video0]
	sz.sort(reverse=True)
	print(sz)

	zd = {'游戏': game0, '小说': novel0, '视频':video0}  # todo key不能为同值
	i = 0
	while True:
		for k, v in sorted(zd.items()):
			if sz[i] == v:
				print(i)
				import pyautogui as ag
				b = ag.confirm('你想要找《' + k + '》,对吗?')
				key = k
				break
		if b == 'OK':
			break
		else:
			i += 1
			del zd[key]
	return key   #你的搜索类型



def search(key,find):
	import pyautogui as ag
	import time
	if key=='游戏':
		sz = [
			'http://so.cr173.com/search/d/' + find + '_all_rank.html',
			'https://s.fxxz.com/search/d/' + find + '_pc_hits.html',
			'http://zhannei.baidu.com/cse/site?q=' + find + '&click=1&cc=52pojie.cn&s=&nsid='
		]
	elif key=='视频':
		sz=[
			'https://v.qq.com/x/search/?q='+find+'&stag=104&smartbox_ab=',
			'https://so.iqiyi.com/so/q_'+find+'?source=default&sr=384435684489',
			'https://so.youku.com/search_video/q_'+find,
			'https://search.bilibili.com/all?keyword=' + find
		]
	elif key=='小说':
		sz=[
			'https://www.baidu.com/s?tn=02049043_8_pg&ch=9&word=' + '还没准备好(；д；)'
		]

	import subprocess
	subprocess.Popen(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"])
	time.sleep(0.5)
	for i in sz:
		ag.hotkey('ctrl', 't')
		import pyperclip
		pyperclip.copy(i)
		ag.hotkey('ctrl','v')
		ag.press('enter')
		ag.press('enter')
		time.sleep(0.5)


import pyautogui as ag
find=ag.prompt('搜索内容')
search(analyse(web(find)),find)