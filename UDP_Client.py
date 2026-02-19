import socket
import argparse
import random
import string

def generate_random_payload(size=1024):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

def udp_client():
    parser = argparse.ArgumentParser(description="Advanced UDP Client for Pentesting / Fuzzing")
    parser.add_argument("host", help="Target Host")
    parser.add_argument("port", type=int, help="Target Port")
    parser.add_argument("--ipv6", action="store_true", help="Use IPv6")
    parser.add_argument("--fuzz", action="store_true", help="Send random data (fuzzing)")
    parser.add_argument("--payload", default="AAABBBCCC", help="Payload to send")
    
    args = parser.parse_args()

    family = socket.AF_INET6 if args.ipv6 else socket.AF_INET
    
    # create a socket object
    client = socket.socket(family, socket.SOCK_DGRAM)

    payload = generate_random_payload() if args.fuzz else args.payload

    try:
        # send some data
        client.sendto(payload.encode(), (args.host, args.port))

        # receive some data
        client.settimeout(2.0) # Set timeout for UDP
        data, addr = client.recvfrom(4096)
        print(f"[*] Received from {addr}:")
        print(data.decode(errors='ignore'))
    except socket.timeout:
        print("[!] Request timed out (no response from UDP server)")
    except Exception as e:
        print(f"[*] Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    udp_client()
