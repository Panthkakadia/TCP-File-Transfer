import socket

# ── Configuration ──────────────────────────────────────────
SERVER_HOST = '127.0.0.1'   # Change to server's IP if on a different machine
SERVER_PORT = 5000
BUFFER_SIZE = 1024

# ── Filename to request from server ───────────────────────
filename = 'mytext.txt'

# ── Create TCP socket and connect to server ────────────────
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# ── Send the filename to the server ───────────────────────
client_socket.send(filename.encode())

#s
# ── Receive file data ──────────────────────────────────────
received_data = b''
print("\nreceiving data...")

while True:
    data = client_socket.recv(BUFFER_SIZE)
    if not data:
        break   # Server closed connection — end of file
    received_data += data

# ── Check for error response from server ──────────────────
if received_data.startswith(b'ERROR'):
    print(f"\n{received_data.decode()}")
else:
    # Save received content to a new file
    output_filename = 'received_' + filename
    with open(output_filename, 'wb') as f:
        f.write(received_data)
    print(f"\n{received_data}")
    print(f"\nSuccessfully got the file → saved as '{output_filename}'")

# ── Close connection ───────────────────────────────────────
client_socket.close()
print("\nconnection closed")
