from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print(f"Source: {packet[IP].src} -> Destination: {packet[IP].dst}")

print("Network Sniffer Started... Press Ctrl+C to stop.")

sniff(prn=packet_callback, store=False)