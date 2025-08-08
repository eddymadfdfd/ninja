import requests
import time
import json

# 多个钱包地址
wallet_addresses = ['0x.....', '0x......', '0x......', '0x......']

# ETH主网的RPC接口URL,使用lava的RPC进行查询
rpc_url = 'https://eth1.lava.build/XXXXX/'

while True:
    for wallet_address in wallet_addresses:
        # 创建JSON-RPC请求
        request = {
            'jsonrpc': '2.0',
            'method': 'eth_getBalance',
            'params': [wallet_address, 'latest'],
            'id': 1,
        }

        # 发送请求
        response = requests.post(rpc_url, json=request)

        # 检查响应
        if response.status_code == 200:
            # 解析响应的JSON数据
            response_data = response.json()

            # 检查"result"
            if 'result' in response_data:
                # 将余额从十六进制转换为十进制
                balance = int(response_data['result'], 16)
                # 打印余额
                print(f'ETH 余额 {wallet_address}: {balance}')
            else:
                # 打印
                print(f'Error querying ETH balance for {wallet_address}: "result" key not found in response data. Response data: {response_data}')
        else:
            print(f'Error querying ETH balance for {wallet_address}: {response.status_code}')

    # 等待3分钟
    time.sleep(20)