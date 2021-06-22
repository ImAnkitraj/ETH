#!/usr/bin/env python
import scapy.all as scapy
import argparse
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP/IP range")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify interface")
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request;
    # arp_request_broadcast.show()

    answered_list, unanswered_list  = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    print("IP\t\t\tMAC Address\n---------------------------------------------")
    for answer in answered_list:
        print(answer[1].psrc+"\t\t"+answer[1].hwsrc)
    # print(answered.summary(), unanswered.summary())
    # print(broadcast.summary())
    # scapy.ls(scapy.ARP())

options = get_arguments()
scan(options.target)



