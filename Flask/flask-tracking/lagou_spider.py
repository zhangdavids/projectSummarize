import time
import requests
from pprint import pprint
from fake_useragent import UserAgent
ua = UserAgent()
import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.job

user_agent = ua.random

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'

headers = {
    "Cookie": "user_trace_token=20171105173814-0b824fa6-c20d-11e7-978b-5254005c3644; LGUID=20171105173814-0b825535-c20d-11e7-978b-5254005c3644; index_location_city=%E6%B7%B1%E5%9C%B3; TG-TRACK-CODE=index_search; SEARCH_ID=5bb5150d5d314f32a34bdb68f6e2dbbc; _gid=GA1.2.1886275699.1509874693; _ga=GA1.2.1197843841.1509874693; LGRID=20171105173909-2cac9846-c20d-11e7-978b-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1509874693; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1509874749; JSESSIONID=ABAAABAAAFCAAEG674AE53B34CFB49996425F9659B657CF",
    "Referer": "https://www.lagou.com/jobs/list_python?px=default&city=%E6%B7%B1%E5%9C%B3",
    "User-Agent": user_agent
}

def get_job_data(num):

    for i in range(num):
        payload = {
            "first": "false",
            "pn": str(i+1),
            "kd": "python"
        }

        response = requests.post(url, data=payload, headers=headers)
        time.sleep(5)
        # pprint(response.json()['content']['positionResult']['result'])
        for item in response.json()['content']['positionResult']['result']:
            db.my_collection.insert_one(item)


if __name__ == '__main__':
    get_job_data(10)