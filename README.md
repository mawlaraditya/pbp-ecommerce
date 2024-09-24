# pbp-ecommerce
Mawla Raditya Pambudi
2306275323


tautan menuju pws : http://mawla-raditya-pbpecommerce.pbp.cs.ui.ac.id
tautan menuju link html : http://127.0.0.1:8000/

link bukti screenshot : https://drive.google.com/drive/folders/1kMHnL3tiG_iCHt4KbOoKyD-vxgqg24Hq?usp=drive_link



1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
   =
   Kedua fungsi ini digunakan untuk mengarahkan pengguna dari satu URL ke URL lain, tetapi ada perbedaan mendasar dalam cara penggunaannya. HttpResponseRedirect() adalah kelas yang mengembalikan objek respons HTTP yang menginstruksikan browser untuk melakukan pengalihan ke URL lain.  Di sisi lain, redirect() adalah fungsi shortcut yang memudahkan proses pengalihan. Fungsi ini memungkinkan kita langsung memberikan berbagai input seperti URL, objek tampilan, atau nama tampilan, yang kemudian secara otomatis dikonversi menjadi URL. Jadi, penggunaan redirect() lebih singkat dan lebih mudah saat kita hanya ingin melakukan pengalihan tanpa perlu menuliskan banyak baris kode tambahan untuk membangun URL secara manual.



2. Jelaskan cara kerja penghubungan model Product dengan User!
   =
   Dalam Django, hubungan antara model Product dan User bisa diwujudkan dengan menggunakan fitur relasi antar-model. Biasanya, ini dilakukan dengan menggunakan tipe relasi ForeignKey atau ManyToManyField, tergantung pada jenis hubungan yang diinginkan. Misalnya, jika ingin merepresentasikan bahwa setiap pengguna dapat memiliki beberapa produk, tetapi setiap produk hanya bisa dimiliki oleh satu pengguna, maka digunakan relasi ForeignKey. Dengan cara ini, setiap produk akan terhubung ke satu pengguna tertentu yang bertindak sebagai pemiliknya, sedangkan seorang pengguna dapat memiliki banyak produk.



3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
   =
   Authentication (otentikasi) dan authorization (otorisasi) adalah dua konsep penting dalam sistem keamanan aplikasi web.  Authentication merujuk pada proses memverifikasi identitas pengguna, yakni memastikan bahwa seseorang yang mencoba mengakses sistem adalah siapa yang mereka klaim. Proses ini biasanya terjadi saat pengguna login dengan memasukkan kredensial seperti username dan password.  Sebaliknya, authorization adalah proses yang menentukan hak akses pengguna setelah mereka berhasil terotentikasi.  Ini mencakup kontrol atas apa yang boleh dilakukan oleh pengguna, misalnya apakah mereka diizinkan untuk melihat halaman tertentu, mengedit data, atau mengakses fitur admin.  Dalam Django, otentikasi biasanya diimplementasikan melalui form login dan backend otentikasi, sedangkan otorisasi dapat dilakukan menggunakan izin yang dapat diatur pada level pengguna atau grup pengguna.



4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
   =
   Untuk mengingat pengguna yang sudah login, Django menggunakan mekanisme yang disebut sesi (session). Setiap kali pengguna berhasil login, Django menyimpan informasi tentang sesi tersebut di server, dan browser pengguna menyimpan session ID dalam bentuk cookie. Pada setiap permintaan selanjutnya, browser mengirimkan cookie ini ke server sehingga Django bisa mengidentifikasi pengguna dan mengingat status login mereka tanpa perlu login ulang pada setiap permintaan halaman.

   Cookies sendiri memiliki banyak kegunaan lain selain menyimpan session ID.  Mereka dapat digunakan untuk menyimpan preferensi pengguna seperti bahasa atau tema yang dipilih, melacak barang yang ditambahkan ke keranjang belanja, atau bahkan untuk keperluan analitik dan pelacakan perilaku pengguna di situs.  Namun, tidak semua cookies aman.  Untuk menjaga keamanan, Django menyediakan pengaturan seperti HttpOnly yang mencegah cookie diakses melalui JavaScript, mengurangi risiko serangan XSS (Cross-Site Scripting), serta Secure yang memastikan cookie hanya dikirim melalui koneksi HTTPS.  



5.  Jelaskan bagaimana cara mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   =
   1. Aktifkan virtual environment: Langkah pertama, mengaktifkan virtual environment di terminal

   2. Modifikasi views.py untuk register user: 
      - impor UserCreationForm dan messages ke views.py.
      - buat fungsi register untuk menangani pendaftaran pengguna baru. Saat pengguna mengisi dan submit form, akun baru akan dibuat.

   3. Buat template register.html:
      - Template ini berisi form pendaftaran yang buat menggunakan tag Django seperti {{ form.as_table }} untuk mempermudah pembuatan form dalam bentuk tabel.

   4. Tambahkan URL routing untuk register:
      - impor fungsi register ke urls.py dan tambahkan URL routing agar form pendaftaran bisa diakses melalui /register/.

   5. Tambahkan fitur login:
      - impor authenticate, login, dan AuthenticationForm di views.py.
      - Fungsi login_user tambahkan untuk autentikasi dan login pengguna.

   6. Buat template login.html:
      - Template ini berisi form login yang mengautentikasi pengguna dan menampilkan pesan jika ada kesalahan atau jika login berhasil.

   7. Tambahkan URL routing untuk login:
      - tambahkan path URL login di urls.py.

   8. Buat fitur logout:
      - impor logout dan buat fungsi logout_user untuk menghapus sesi pengguna dan mengarahkan pengguna kembali ke halaman login.

   9. Tambahkan tombol logout di halaman utama:
      - Di main.html, tambahkan tombol logout menggunakan hyperlink yang mengarah ke main:logout.

   10. Restriksi akses halaman utama:
      - menggunakan decorator @login_required(login_url='/login') untuk memastikan bahwa hanya pengguna yang telah login yang bisa mengakses halaman utama.

   11. Tambah fungsionalitas cookies (last login):
      - Saat pengguna login, menyimpan waktu terakhir login di dalam cookie bernama last_login.
      - tambahkan tampilan di halaman utama untuk menunjukkan waktu terakhir login dari cookie tersebut.

   12. Hubungkan model MoodEntry dengan User:
      - modifikasi model MoodEntry dengan menambahkan ForeignKey ke model User.
      - Setiap MoodEntry yang dibuat akan terhubung dengan pengguna yang membuatnya. 

   13. Tampilkan hanya MoodEntry milik pengguna yang sedang login:
      - modifikasi fungsi show_main agar hanya menampilkan MoodEntry yang terkait dengan pengguna yang sedang login.

   14. Lakukan migrasi model:
      - menjalankan python manage.py makemigrations dan python manage.py migrate untuk memigrasikan perubahan model.
      - Pastikan ada minimal satu pengguna yang terdaftar sebelum melakukan migrasi.

   15. Ubah setting untuk environment production:
      - Di settings.py, ubah variabel DEBUG untuk mendukung mode production.

   Setelah semua langkah selesai, jalankan proyek dengan python manage.py runserver, dan coba login dengan akun baru untuk memverifikasi semua fungsionalitas yang tambahkan.




