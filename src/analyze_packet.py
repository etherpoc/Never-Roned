
import pyshark
import os

def packet_capture():
    capture = pyshark.LiveCapture ('イーサネット', bpf_filter='net 160.16.0.0/16 and tcp port 443', override_prefs={'tls.keylog_file':os.environ["SSLKEYLOGFILE"]})
    for packet in capture:
        #print(packet.layers)
        if "DATA-TEXT-LINES" in packet:
            print(packet['DATA-TEXT-LINES'])



