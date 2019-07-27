

baseAdd = "https://viewdns.info/"
ipLocation = baseAdd + "iplocation/?ip={}"
ipWhois = baseAdd + "whois/?domain={}"
ipReverseDNS = baseAdd + "reversedns/?ip={}"
portScan = baseAdd + "portscan/?host={}"


def get_ip_location(ip):
    return ipLocation.format(ip)


def get_ip_whois(ip):
    return ipWhois.format(ip)


def get_reverse_dns(ip):
    return ipReverseDNS.format(ip)


def get_port_scan(ip):
    return portScan.format(ip)
