import socket
import threading
import logging

# =========================
# CONFIGURATION
# =========================
LISTEN_IP = '0.0.0.0'  # Victim listens on all interfaces
LISTEN_PORT = 80        # Port to listen on (HTTP, can be changed)
HONEYPOT_IP = '192.168.56.103'
HONEYPOT_PORT = 80      # Port on honeypot (match service)

# =========================
# LOGGING SETUP
# =========================
logging.basicConfig(
    filename="deception_proxy.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

print(f"🔁 Deception proxy started on port {LISTEN_PORT}, redirecting to {HONEYPOT_IP}:{HONEYPOT_PORT}")
logging.info("Proxy started: Listening on port %s, redirecting to honeypot at %s:%s", LISTEN_PORT, HONEYPOT_IP, HONEYPOT_PORT)

def handle_connection(client_socket):
    try:
        # Connect to honeypot
        honeypot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        honeypot_socket.connect((HONEYPOT_IP, HONEYPOT_PORT))

        # Start forwarding in both directions
        threading.Thread(target=forward, args=(client_socket, honeypot_socket, "Attacker → Honeypot", client_socket.getpeername()[0])).start()
        threading.Thread(target=forward, args=(honeypot_socket, client_socket, "Honeypot → Attacker", client_socket.getpeername()[0])).start()

    except Exception as e:
        logging.error("Connection error: %s", e)
        client_socket.close()

def forward(source, destination, direction, ip):
    try:
        while True:
            data = source.recv(4096)
            if not data:
                break
            logging.info("Forwarding (%s) [%s]: %d bytes", direction, ip, len(data))
            destination.sendall(data)
    except Exception as e:
        logging.warning("Forwarding exception (%s) [%s]: %s", direction, ip, e)
    finally:
        source.close()
        destination.close()

# =========================
# START LISTENING
# =========================
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LISTEN_IP, LISTEN_PORT))
server.listen(100)

while True:
    client_socket, addr = server.accept()
    print(f"🚨 New connection from {addr[0]}:{addr[1]}")
    logging.info("New connection from %s:%s", addr[0], addr[1])
    threading.Thread(target=handle_connection, args=(client_socket,)).start()
