import requests
import urllib
import json
import os

headers = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
name = input('歌手：')
url = 'http://www.kugou.com/yy/html/search.html#searchType=song&searchKeyWord=' + name
r = requests.get(url, headers=headers)
singer_url = 'http://songsearch.kugou.com/song_search_v2?&keyword=' + name + '&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&_=1541903771954'
singer = requests.get(singer_url, headers=headers)
song_list = json.loads(singer.text)#返回json转为字典，方便提取
for i in song_list['data']['lists']:
    alnumid = i['AlbumID']
    filehash = i['FileHash']
    songing_list = 'http://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash=' + filehash + '&album_id=' + alnumid + '&_=1541908724162'
    song = requests.get(songing_list, headers=headers)
    html = json.loads(song.text)['data']#返回json转为字典，方便提取
    songname = html['song_name']#歌曲的名称
    url = html['play_url']#歌曲的网址
    print('下载中。。。。。')
    folder = os.path.exists('E:/music/' + name)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs('E:/music/' + name)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print('创建成狗了。。。。')
    html = requests.get(url, headers=headers)
    urllib.request.urlretrieve(html.url, 'E:/music/' + name + '/' + songname + '.mp3')#歌曲保存的路径
    print(songname + '下载完成')


