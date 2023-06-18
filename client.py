import socket  # Mengimpor modul socket
import time  # Mengimpor modul waktu

while True:  # Mulai loop
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Membuat objek socket
        client_socket.connect(('localhost', 8080))  # Menghubungkan ke server

        request = 'GET /index.html HTTP/1.0\r\n\r\n'  # Membuat request HTTP
        client_socket.sendall(request.encode())  # Mengirimkan request ke server

        response = ''  # Membuat variabel untuk menyimpan response
        while True:  # Mulai loop untuk menerima data
            data = client_socket.recv(1024)  # Menerima data dari server
            if not data:  # Jika tidak ada data yang diterima
                break  # Keluar dari loop
            response += data.decode()  # Menambahkan data ke response

        print('Response:', response)  # Mencetak response

        client_socket.close()  # Menutup koneksi
        time.sleep(1)  # Menunggu selama satu detik sebelum mengirim request selanjutnya

    except ConnectionRefusedError:  # Menangani jika koneksi ditolak
        print('Server telah berhenti')  # Mencetak pesan
        break  # Keluar dari loop