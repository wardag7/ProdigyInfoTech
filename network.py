import scapy.all as scapy

def sniff_packets(interface):
    # Start sniffing packets on the specified interface
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def process_packet(packet):
    # Extract relevant information from the packet
    if packet.haslayer(scapy.IP):
        source_ip = packet[scapy.IP].src
        destination_ip = packet[scapy.IP].dst
        protocol = packet[scapy.IP].proto

        # Display the information
        print(f"Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol}")

        # Check if the packet has TCP or UDP layer
        if packet.haslayer(scapy.TCP):
            source_port = packet[scapy.TCP].sport
            destination_port = packet[scapy.TCP].dport
            print(f"Source Port: {source_port} | Destination Port: {destination_port}")

            # Display payload data (first 100 bytes)
            payload = packet[scapy.Raw].load
            print("Payload Data:")
            print(payload[:100])

        elif packet.haslayer(scapy.UDP):
            source_port = packet[scapy.UDP].sport
            destination_port = packet[scapy.UDP].dport
            print(f"Source Port: {source_port} | Destination Port: {destination_port}")

            # Display payload data (first 100 bytes)
            payload = packet[scapy.Raw].load
            print("Payload Data:")
            print(payload[:100])

# Main function
def main():
    interface = input("Enter the interface to sniff packets (e.g., eth0, wlan0): ")
    print(f"Sniffing packets on interface {interface}...")
    sniff_packets(interface)

if __name__ == "__main__":
    main()
