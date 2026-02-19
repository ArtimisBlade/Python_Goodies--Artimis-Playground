import socket
import argparse
import ssl

def tcp_client():
    parser = argparse.ArgumentParser(description="Advanced TCP Client for Pentesting")
    parser.add_argument("host", help="Target Host (IPv4/IPv6 or DNS)")
    parser.add_argument("port", type=int, help="Target Port")
    parser.add_argument("--ipv6", action="store_true", help="Use IPv6")
    parser.add_argument("--ssl", action="store_true", help="Use SSL/TLS")
    parser.add_argument("--payload", default="GET / HTTP/1.1\r\nHost: google.com\r\n\r\n", help="Payload to send")
    
    args = parser.parse_args()

    # Determine Address Family
    family = socket.AF_INET6 if args.ipv6 else socket.AF_INET
    
    # Create socket object
    client = socket.socket(family, socket.SOCK_STREAM)
    
    # Wrap with SSL if requested
    if args.ssl:
        context = ssl.create_default_context()
        # For pentesting, we might want to disable cert verification in some cases, 
        # but let's keep it default/secure for now or add an option.
        client = context.wrap_socket(client, server_hostname=args.host)

    try:
        # Connect the client
        client.connect((args.host, args.port))

        # Send some data
        client.send(args.payload.encode())

        # Receive some data
        response = client.recv(4096)
        print(response.decode(errors='ignore'))
    except Exception as e:
        print(f"[*] Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    tcp_client()