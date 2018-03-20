import requests
import pandas as pd
import time

headers = {
    "authorization": "Bearer Mi4xUTVFQUFBQUFBQUFBY01DY2lRajFDUmNBQUFCaEFsVk5rekRyV2dDaVdyYURMUy15NlFEaEV0R2hyb2thOG15LVFB|1509810835|f285d95ba27e60959c90defb9627757f9841441d",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}


def get_user_data(page):
    result = []
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/huo-gu-lao-shi-ren/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(
            i*20)
        response = requests.get(url, headers=headers).json()['data']

        print("正在爬取第%s页" % str(i+1))
        result.extend(response)
        time.sleep(1)

    return result

if __name__ == '__main__':
    result = get_user_data(108)
    df = pd.DataFrame.from_dict(result)
    df.to_csv('zhihu_user.csv')
