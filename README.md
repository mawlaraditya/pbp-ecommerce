# pbp-ecommerce
Mawla Raditya Pambudi
2306275323


tautan menuju pws : http://mawla-raditya-pbpecommerce.pbp.cs.ui.ac.id
tautan menuju link html saya : http://127.0.0.1:8000/


1. Mengapa kita memerlukan data delivery dalam pengimplementasian platform?
   =
   Data delivery penting untuk mengirim dan menerima informasi antara berbagai komponen platform, seperti server dan klien. Ini memungkinkan sinkronisasi data real-time, pemrosesan data, dan komunikasi yang efisien antara sistem yang berbeda, mendukung fungsionalitas aplikasi.


2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
   =
   JSON lebih baik untuk kebanyakan aplikasi modern karena lebih ringan, lebih mudah dibaca oleh manusia, dan diintegrasikan lebih cepat dengan JavaScript. JSON lebih populer karena strukturnya yang simpel dan efisien dalam hal penggunaan bandwidth dan kecepatan parsing dibanding XML yang lebih verbose dan kompleks.


3. Fungsi method `is_valid()` pada form Django?
   =  
   Method `is_valid()` digunakan untuk memvalidasi input data yang diterima dari form berdasarkan aturan yang ditetapkan dalam form tersebut. Jika valid, method ini akan mengembalikan `True`, dan kita bisa mengakses data yang sudah bersih (cleaned data). Kita memerlukan method ini untuk memastikan data yang masuk sesuai dan aman sebelum diproses lebih lanjut.


4. Mengapa kita membutuhkan `csrf_token` pada form di Django? Apa yang terjadi jika tidak ada?
   =  
   `csrf_token` melindungi form dari serangan CSRF (Cross-Site Request Forgery) yang dapat dieksploitasi oleh penyerang untuk melakukan aksi berbahaya tanpa sepengetahuan pengguna. Tanpa `csrf_token`, penyerang bisa memalsukan permintaan ke server dan mengambil alih sesi pengguna.


5. Cara mengimplementasikan checklist secara step-by-step (tidak hanya mengikuti tutorial)
   =  
   - Identifikasi kebutuhan data platform dan pilih format data delivery yang tepat.
   - Tentukan apakah menggunakan JSON atau XML, sesuaikan dengan keperluan, seperti keringanan dan kompatibilitas.
   - Dalam Django, buat form dan pastikan validasi melalui `is_valid()` untuk memeriksa input.
   - Tambahkan `csrf_token` di template HTML form untuk mengamankan aplikasi dari serangan CSRF.
   - Lakukan pengujian dan debugging sendiri, bukan hanya mengikuti tutorial, agar mengerti secara mendalam setiap langkah yang diambil.