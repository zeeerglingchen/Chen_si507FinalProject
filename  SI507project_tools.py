import urllib.request
import json
import csv

user_id='1787211337'
fan_id = "1785162243"


proxy_addr="122.241.72.191:808"
proxy_addr2="118.190.73.168:808"
proxy_addr_homepage="115.216.119.174:808"


dict_name_list = []
fans_name_list = []

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
    for i in range(1,20):
        url = "https://m.weibo.cn/api/container/getIndex?containerid=231051_-_fans_-_"+ userid +"&since_id=" + str(i)
        dict_name ="resp"+str(i)
        dict_name_list.append(dict_name)
        onepiecedata = json.loads(proxyipaddr(url,proxy_addr))
        dictionary[dict_name] = onepiecedata

    with open ('newfile.json',"w") as saveFile:
        saveFile.write(json.dumps(dictionary))
    saveFile.close()


getweibodata(user_id, proxy_addr2)

with open("newfile.json","r") as readFile:
    cache_content = readFile.read()
    cache_dic = json.loads(cache_content)
readFile.close()

card_groud_len = 0

fans_type = ["real","fake","unsure"]

# write data into csv file:
head = ["UserName","id","Rank","self_intro","other_intro","Gender","FollowerNum","FollowingNum","PostCounts","Type"]

with open('RawDatafromWEIBO.csv', 'w', newline = '') as csv_file:
    line = csv.writer(csv_file)
    line.writerow(head)
    try:
        for name in dict_name_list:
            card_group = cache_dic[name]["data"]["cards"][-1]["card_group"]
            for group in range(len(card_group)):
                group_index = card_group[group]

                fan_name = group_index["user"]["screen_name"]
                fan_id = group_index["user"]["id"]
                fan_self_intro = group_index["desc1"]
                other_self_intro = group_index["desc2"]
                fan_follower = group_index["user"]["followers_count"]
                fan_following = group_index["user"]["follow_count"]

                fan_homepage_url = "https://m.weibo.cn/profile/info?uid=" + str(fan_id)
                fan_info = json.loads(proxyipaddr(fan_homepage_url, proxy_addr_homepage))
                fan_statues_count = fan_info["data"]["user"]["statuses_count"]
                fan_gender = fan_info["data"]["user"]["gender"]
                fan_rank = fan_info["data"]["user"]["urank"]

                if "用户" in fan_name:
                    line.writerow([fan_name,fan_id,fan_rank,fan_self_intro,other_self_intro,fan_gender,fan_follower,fan_following,fan_statues_count,fans_type[1]])
                elif fan_following < fan_follower:
                    line.writerow([fan_name,fan_id,fan_rank,fan_self_intro,other_self_intro,fan_gender,fan_follower,fan_following,fan_statues_count,fans_type[0]])
                else:
                    line.writerow([fan_name,fan_id,fan_rank,fan_self_intro,other_self_intro,fan_gender,fan_follower,fan_following,fan_statues_count,fans_type[2]])




    except Exception as e:
        print(e)

csv_file.close()
