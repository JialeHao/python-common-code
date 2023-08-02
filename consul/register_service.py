# Author: HAOJIALE
# 依赖 pip install requests
# consul注册接口调用

import json
import requests

payload = {
    "name": "node_exporter",
    "id": "node_exporter-192.168.100.100",
    "tags": ["prometheus"],
    "address": "192.168.100.100",
    "port": 9100,
    "meta": {
        "os": "linux",
        "os_version": "CentOS7.9_2009",
        "app": "prometheus"
    },
    "checks": [
        {
            "http": "http://192.168.100.100:9100/metrics",
            "interval": "5s"
        }
    ],
    "weights": {
        "Passing": 10,
        "Warning": 1
    }
}

headers = {
    "Content-Type": "application/json",
    # "X-Consul-Token": "your_token"  # 如果启用了acl配置此选项
}

r = requests.put(
    url="http://192.168.100.100:8500/v1/agent/service/register",
    headers=headers,
    data=json.dumps(payload)
)

print(r.status_code)