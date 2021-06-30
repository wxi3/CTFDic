#!/usr/bin/python2.7.8
#encoding:utf-8

import pyshark

captures = pyshark.FileCapture("s702.pcapng")
list = []
for c in captures:
    for pkt in c:
        if pkt.layer_name == "s7comm" and hasattr(pkt, "param_func"):
            param_func = pkt.param_func
            try:
                if param_func=='0x00000005':
                    list.append(pkt.resp_data)
                else:
                    continue
            except Exception as e:
                print(e)
print (list)