
"""
MACS30200

Jingwen Ni
"""

import requests
import pandas as pd
import time
requests.packages.urllib3.disable_warnings()
def request_zb(prov_code, zb_code):
    cookies = {
        'JSESSIONID': 'On0_jSZcmgJ4_IJthLgaaqCJrXyAIbaLRbTW2fgJsvinXwvVWynk!-1028858781',
        'u': '1',
    }
    
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'JSESSIONID=On0_jSZcmgJ4_IJthLgaaqCJrXyAIbaLRbTW2fgJsvinXwvVWynk!-1028858781; u=1',
        # 'Referer': 'https://data.stats.gov.cn/easyquery.htm?cn=E0103',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'm': 'QueryData',
        'dbcode': 'fsnd',
        'rowcode': 'zb',
        'colcode': 'sj',
        'wds': '[{"wdcode":"reg","valuecode":"' + prov_code +'"}]',
        'dfwds': '[{"wdcode":"zb","valuecode":"'+ zb_code +'"}, {"wdcode":"sj","valuecode":"LAST20"}]',
        'k1': '1650334407532',
    }
    response = requests.get('https://data.stats.gov.cn/easyquery.htm', headers=headers, params=params, cookies=cookies, verify=False).json()
    datanodes = response["returndata"]["datanodes"]
    rows = []
    for datanode in datanodes:
        # if datanode['code'].startswith('zb.A030101'):
        value = datanode['data']['data']
        year = datanode['wds'][-1]['valuecode']
        prov_code = datanode['wds'][-2]['valuecode']
        dict_row = {'年份': year,
                    '省份id': prov_code,
                    '数值': value,
                    '指标id': zb_code
                    }
        rows.append(dict_row)
    df_rows = pd.DataFrame(rows, index = range(len(rows)))
    return df_rows

if __name__ == '__main__':
    dict_prov = {'北京市': '110000',
                 '天津市': '120000',
                 '河北省': '130000',
                 '山西省': '140000',
                 '内蒙古自治区': '150000',
                 '辽宁省': '210000',
                 '吉林省': '220000',
                 '黑龙江省': '230000',
                 '上海市': '310000',
                 '江苏省': '320000',
                 '浙江省': '330000',
                 '安徽省': '340000',
                 '福建省': '350000',
                 '江西省': '360000',
                 '山东省': '370000',
                 '河南省': '410000',
                 '湖北省': '420000',
                 '湖南省': '430000',
                 '广东省': '440000',
                 '广西壮族自治区': '450000',
                 '海南省': '460000',
                 '重庆市': '500000',
                 '四川省': '510000',
                 '贵州省': '520000',
                 '云南省': '530000',
                 '西藏自治区': '540000',
                 '陕西省': '610000',
                 '甘肃省': '620000',
                 '青海省': '630000',
                 '宁夏回族自治区': '640000',
                 '新疆维吾尔自治区': '650000',
                 }
    dict_zb = {'年末常住人口(万人)': 'A030101',
               '地区生产总值(亿元)': 'A020101',
               '第一产业增加值(亿元)': 'A020102',
               '第二产业增加值(亿元)': 'A020103',
               '第三产业增加值(亿元)': 'A020104',
               '普通高等学校本科毕(结)业生数(万人)': 'A0M0109',
               '普通高等学校专科预计毕业生数': 'A0M010A',
               '社会消费品零售总额(亿元)': 'A0H01', 
               '居民消费价格指数(上年=100)': 'A090101',
               '人口自然增长率': 'A030203',
               '城镇单位就业人员(万人)': 'A040101',
               }
    df_zbs = pd.DataFrame()
    for zb in dict_zb.keys():
        for prov in dict_prov.keys():
            print(prov, zb)
            prov_code = dict_prov[prov]
            zb_code = dict_zb[zb]
            try:
                df_zb = request_zb(prov_code, zb_code)
            except:
                time.sleep(4)
                df_zb = request_zb(prov_code, zb_code)
            df_zb['省份'] = prov
            df_zb['指标类别'] = zb
            df_zbs = pd.concat([df_zbs, df_zb], ignore_index=True)
            time.sleep(2)
    df_zbs_pivot = pd.pivot_table(df_zbs, values = '数值', index = ['年份', '省份'], columns = '指标类别').reset_index()
    df_zbs_pivot.to_csv('指标数据.csv', index = False, encoding = 'utf_8_sig')
