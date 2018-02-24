import requests
url0 = 'http://edu.tv.sohu.com/info/course/play.do?vid=91840010&plat=1'
url1 = 'http://220.181.61.212/fmp4?prot=9&prod=flash&pt=1&file=&new=/232/210/EgtMZWsRRKW3h9h9XSRX9L.mp4&key=jiYZhZg4vnxctJuW_bZzXnkkuUsi0Ebv&vid=91840010_31&tvid=91840010&uid=15077751003084265141&sz=980_910&md=qczPDG4mFkzKaTwpP2T4dIG+LQpIFY0A106&iswebp2p=0&rb=1&t=0.7363633355125785'
url3 = 'http://220.181.61.240/fmp4?prot=9&prod=flash&pt=1&file=&new=/250/74/kgnE4TxwRUOKMPLqUhGkqD.mp4&key=slrJV72PYnBwrSdb-9XT9ePIFkcq7Njv&vid=91595480_31&tvid=91595480&uid=15077751003084265141&sz=980_910&md=qczPDG4mFkzKaTwpP2T4dIG+LQpIFY0A106&iswebp2p=0&rb=1&t=0.5871338662691414'
url4 = 'http://220.181.61.229/fmp4?prot=9&prod=flash&pt=1&file=&new=/85/227/6aoxV4GbRriOiKVOGfmiTD.mp4&key=95JZM00neykjcPm9zUaX_s2Wo7wUZvlf&vid=91595657_31&tvid=91595657&uid=15077751003084265141&sz=980_910&md=qczPDG4mFkzKaTwpP2T4dIG+LQpIFY0A106&iswebp2p=0&rb=1&t=0.0937083289027214'
url32 = 'http://220.181.61.229/fmp4?prot=9&prod=flash&pt=1&file=&new=/250/74/kgnE4TxwRUOKMPLqUhGkqD.mp4&key=znzH-WFpa5Vhnn9G8mcbvi3AuUKevN-Z&vid=91595480_31&tvid=91595480&uid=15077751003084265141&sz=980_910&md=qczPDG4mFkzKaTwpP2T4dIG+LQpIFY0A106&iswebp2p=0&rb=1&t=0.5275950995273888'

import requests,json

url = 'http://my.tv.sohu.com/play/videonew.do?vid=91837529&pflag=flash&ver=31&bw=452&api_key=0092470a2ce6ab9a179a003fc639ebbf&uid=15077742204646145637&out=0&g=8&referer=http%3A//edu.tv.sohu.com/info/course/play.do%3Fvid%3D91595455%26plat%3D1&t=0.8411342133767903'

r = requests.get(url)

a = json.loads(r.text)

urll = (a.get('data').get('su'))

for b in urll:
	url1 = 'http://al.vod.tv.itc.cn'+b
	print(url1)
	v = requests.get(url1).content
	file = open('1.mp4','wb')
	file.write(v)
	file.close()