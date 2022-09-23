import os
import requests

NBA_DICT = {
    "1": {"title": "威少奇才首秀三双",
          "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300fc20000bvi413nedtlt5abaa8tg&ratio=720p&line=0"},
    "2": {"title": "塔图姆三分准绝杀",
          "url": "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0d00fb60000bvi0ba63vni5gqts0uag&ratio=720p&line=0"},
    "3": {"title": "东北F4模仿秀",
          'url': "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"}
}


def dowload(url):
    res = requests.get(
        url=url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 FS"
        }
    )
    res.encoding = 'utf-8'
    return res.content


for i in NBA_DICT.values():
    print(i)
    url = i.get('url')
    resu = dowload(url)
    with open(r"G:\usr\video\{}.mp4".format(i.get('title')), mode='wb') as file:
        file.write(resu)
print('over')
