
b = ['豆瓣电影</span>', 'v.youku.com/v_show/id_XM...&nbsp;', 'www.mca.gov.cn/article/xw/mtbd...', 'www.iqiyi.com/v_19rrk40a...&nbsp;']

import re

game=['4399小游戏','4399.com','游侠网','ali213.net','3DMGAME','3dmgame.com','游民星空','gamersky.com']
novel=['起点中文网','qidian.com','简书','jianshu.com','笔趣阁','biquge.info']
video=['爱奇艺','iqiyi.com','腾讯视频','v.qq.com','哔哩哔哩','bilibili.com','优酷网','youku.com']
cs = []
game0 = 0
novel0 = 0
video0=0
cs0 = 0

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
sz = [game0, novel0, video0,cs0]
print(sz)
sz.sort(reverse=True)
print(sz)




