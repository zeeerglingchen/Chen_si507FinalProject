import urllib.request
import json
import csv
import random
from random import choice

user_id='1787211337'
fan_id = "1785162243"





dict_name_list = []
fans_name_list = []
fans_type = ["real","fake","unsure"]
card_groud_len = 0


def proxyipaddr(url,proxy_addr):
    headers = {}
    # using header to fool the server
    headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
    req=urllib.request.Request(url,headers = headers)

    # using virtual ip address to fool the server
    proxy=urllib.request.ProxyHandler({'http':proxy_addr})
    opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(req).read().decode("UTF-8")

    return data



def getweibodata(userid , proxy_addr):
    dictionary ={}
    onepiecedata =""
    fans_num  = 0
    fan_homepage_url = "https://m.weibo.cn/profile/info?uid=" + str(userid)
    getfansnumber = json.loads(proxyipaddr(fan_homepage_url, proxy_addr))
    fansnumber = getfansnumber["data"]["user"]["followers_count"]
    pages = int(fansnumber / 14)

    for i in range(1,pages):
        url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_"+ userid +"&since_id=" + str(i)
        dict_name ="resp"+str(i)
        dict_name_list.append(dict_name)
        onepiecedata = json.loads(proxyipaddr(url,proxy_addr))
        dictionary[dict_name] = onepiecedata

    # with open ('newfile.json',"w") as saveFile:
    #     saveFile.write(json.dumps(dictionary))
    # saveFile.close()
    #
    # with open("newfile.json","r") as readFile:
    #     cache_content = readFile.read()
    #     cache_dic = json.loads(cache_content)
    # readFile.close()

    # write data into csv file:
    head = ["UserName","id","self_intro","FollowerNum","FollowingNum","Type"]
    csv_file_name = userid+ ".csv"
    with open(csv_file_name, 'w', newline = '') as csv_file:
        line = csv.writer(csv_file)
        line.writerow(head)
        try:
            for name in dict_name_list:
                card_group = dictionary[name]["data"]["cards"][-1]["card_group"]
                for group in range(len(card_group)):
                    group_index = card_group[group]

                    fan_name = group_index["user"]["screen_name"]
                    fan_id = group_index["user"]["id"]
                    fan_self_intro = group_index["desc1"]
                    fan_follower = group_index["user"]["followers_count"]
                    fan_following = group_index["user"]["follow_count"]

                    # fan_homepage_url = "https://m.weibo.cn/profile/info?uid=" + str(fan_id)
                    # fan_info = json.loads(proxyipaddr(fan_homepage_url, proxy_addr))
                    # fan_statues_count = fan_info["data"]["user"]["statuses_count"]
                    # fan_gender = fan_info["data"]["user"]["gender"]
                    # fan_rank = fan_info["data"]["user"]["urank"]

                    if "用户" in fan_name:
                        line.writerow([fan_name,fan_id,fan_self_intro,fan_follower,fan_following,fans_type[1]])
                    elif fan_following < fan_follower:
                        line.writerow([fan_name,fan_id,fan_self_intro,fan_follower,fan_following,fans_type[0]])
                    else:
                        line.writerow([fan_name,fan_id,fan_self_intro,fan_follower,fan_following,fans_type[2]])




        except Exception as e:
            print(e)

    csv_file.close()
    return csv_file_name
