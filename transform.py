# 这一段是baidu sdk 示例， 改了部分没有大改
import requests
import json
import sys
import base64
import time

IS_PY3 = sys.version_info.major == 3

from urllib.request import urlopen
from urllib.request import Request
from urllib.error import URLError
from urllib.parse import urlencode
from transfer import *
from error import *

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

"""  获取请求TOKEN start 通过开通音频文件转写接口的百度应用的API_KEY及SECRET_KEY获取请求token"""


class DemoError(Exception):
    pass


TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
# SCOPE = 'brain_bicc'  # 有此scope表示有asr能力，没有请在网页里勾选 bicc
SCOPE = 'brain_asr_async'  # 有此scope表示有asr能力，没有请在网页里勾选


# SCOPE = 'brain_enhanced_asr'  # 有此scope表示有asr能力，没有请在网页里勾选

def fetch_token():
    config_info = get_config()
    baidu_id = config_info[2]
    baidu_key = config_info[3]
    params = {'grant_type': 'client_credentials',
              'client_id': baidu_id,
              'client_secret': baidu_key}
    post_data = urlencode(params)
    post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req)
        result_str = f.read()
    except URLError as err:
        print('token http response http code : ' + str(err.code))
        result_str = err.read()

    result_str = result_str.decode()
    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if SCOPE in result['scope'].split(' '):
            return result['access_token']

    print("BaiduAI Build Token Wrong, maybe because scope is not correct. ")
    return Error(BAIDU_BUILD_TOKEN_WRONG)


def create_task(url_list):
    task_list = []
    response_url = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/create'
    for audio_url in url_list:
        body = {
            "speech_url": audio_url,
            "format": "mp3",
            # 音频格式，支持pcm,wav,mp3，音频格式转化可通过开源ffmpeg工具（https://ai.baidu.com/ai-doc/SPEECH/7k38lxpwf）或音频处理软件
            "pid": 1537,  # 模型pid，1537为普通话输入法模型，1737为英语模型
            "rate": 16000  # 音频采样率，支持16000采样率，音频格式转化可通过开源ffmpeg工具（https://ai.baidu.com/ai-doc/SPEECH/7k38lxpwf）或音频处理软件
        }
        token_value = fetch_token()
        if type(token_value) == Error:
            return token_value
        token = {"access_token": token_value}
        headers = {'content-type': "application/json"}
        try:
            t = requests.post(response_url, params=token, data=json.dumps(body), headers=headers)
        except:
            return Error(USE_POST_ERROR)
        response_item = eval(t.text)
        if response_item.get("error_code") is None and response_item.get("task_id") is not None:
            task_list.append(response_item.get("task_id"))
        else:
            error_code = str(response_item.get("error_code"))
            print("BaiduAI create task error, error code: %s" % error_code)
            return Error(error_code)
    return task_list


def get_result(task_list):
    token_value = fetch_token()
    if type(token_value) == Error:
        return token_value
    response_url = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/query'  # 查询音频任务转写结果请求地址
    body = {"task_ids":task_list}
    token = {"access_token": token_value}
    headers = {'content-type': "application/json"}
    task_num = 0
    print("等待baiduAI进行翻译")
    try:
        response_item = eval(requests.post(response_url, params=token, data=json.dumps(body), headers=headers).text)
        while task_num < len(response_item.get("tasks_info")):
            response_item = eval(requests.post(response_url, params=token, data=json.dumps(body), headers=headers).text)
            if response_item["tasks_info"][task_num]["task_status"] == "Running":
                task_num = 0
                time.sleep(10)
            else:
                task_num += 1


        for task in response_item.get("tasks_info"):
            words = ""
            if task.get("Status") == "Failure":
                print("BaiduAI transform something wrong by query result , error code: %s" % str(
                    task["task_result"]["err_no"]))
                print("有切片没有成功翻译， 需注意")
            else:
                words += task["task_result"]["result"][0]

    except:
        with open("fix_problem.txt", "w", encoding="utf8") as writer:
            writer.write(requests.post(response_url, params=token, data=json.dumps(body), headers=headers).text)
        return Error(BAIDU_QUERY_TASK_FORMAT_CHANGE)
    with open("result.txt", "w", encoding="utf8") as writer:
        print("翻译成功， 译文文件已写入同一目录下的result.txt中，请及时查看")
        writer.write(words)

    input("Transform Done,  按任意键结束软件")
