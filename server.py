import socket  # Mengimpor modul socket

# Membuat objek socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Mengikat socket ke alamat dan port tertentu
server_socket.bind(('localhost', 8080))

# Mengatur server untuk mendengarkan koneksi
server_socket.listen(1)

print('Server siap menerima koneksi')  # Mencetak pesan bahwa server siap

while True:  # Mulai loop utama
    client_socket, client_address = server_socket.accept()  # Menerima koneksi dari client
    print('Menerima koneksi dari', client_address)  # Mencetak alamat client

    # Menerima data dari client
    data = client_socket.recv(1024).decode()
    request = data.split('\r\n')
    first_line = request[0]  # Ambil baris pertama dari request

    print('Request:', first_line)  # Mencetak baris pertama dari request

    filename = first_line.split()[1][1:]  # Mengambil nama file dari request

    try:
        # Mencoba membuka file
        with open(f'htdocs/{filename}', 'r') as file:
            content = file.read()  # Membaca konten file

        # Membuat response
        response = f'HTTP/1.0 200 OK\r\n\r\n{content}'
    except FileNotFoundError:
        # Jika file tidak ditemukan, kirim pesan "404 Not Found"
        response = 'HTTP/1.0 404 NOT FOUND\r\n\r\nFile Not Found'

    # Mengirimkan response ke client
    client_socket.sendall(response.encode())
    client_socket.close()  # Menutup koneksi dengan client

server_socket.close()  # Menutup server socket