# Author: HAOJIALE
# 依赖 pip install dnspython
# 在系统未配置dns服务器的情况下将域名解析为IP地址

import dns.resolver
import dns.rdatatype
import ipaddress


def domain_name_resolve(domain_name: str, dnslist: list) -> list[str]:
    ip_list = []

    # A记录: 将主机名转换成IP地址
    # dns.rdatatype.A为内置类型，也可写为query_type = 'A'
    query_type = dns.rdatatype.A

    custom_resolver = dns.resolver.Resolver()

    # 指定dns服务器，如果指定，默认使用运行程序设备的dns服务器
    custom_resolver.nameservers = dnslist

    try:
        resp = custom_resolver.resolve(qname=domain_name, rdtype=query_type)
        for i in resp.response.answer:
            for ip in i.items:
                ipstr = str(ip)
                if isip(ipstr):
                    ip_list.append(ipstr)
    except Exception as e:
        print(e)

    return ip_list


# 判断字符串是否是IP地址
def isip(ipstr: str) -> bool:
    try:
        ipaddress.ip_address(ipstr)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    nameservers = ['114.114.114.114', '119.29.29.29']
    query_name = 'www.baidu.com'
    resp = domain_name_resolve(query_name, nameservers)
    print(resp)
