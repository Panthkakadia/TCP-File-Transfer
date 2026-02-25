import socket

# ── Configuration ──────────────────────────────────────────
HOST = ''        # Listen on all available interfaces
PORT = 5000      # Port to listen on
BUFFER_SIZE = 1024

# ── Create TCP socket ──────────────────────────────────────
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server listening....")

# ── Accept incoming connection ─────────────────────────────
conn, addr = server_socket.accept()
print(f"\nGot connection from {addr}")

# ── Receive the requested filename from client ─────────────
filename = conn.recv(BUFFER_SIZE).decode()
print(f"\nServer received the file name '{filename}'")

# ── Try to open and send the file ─────────────────────────
try:
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            conn.send(data)
            print(f"\nSent  {data}")
    print("\nDone sending.")

except FileNotFoundError:
    # Send error message if file does not exist
    error_msg = f"ERROR: File '{filename}' not found on server."
    conn.send(error_msg.encode())
    print(f"\n{error_msg}")

# ── Close connection (signals end of transfer to client) ───
conn.close()
server_socket.close()
