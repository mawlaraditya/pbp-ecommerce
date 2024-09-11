# pbp-ecommerce
Mawla Raditya Pambudi
2306275323


tautan menuju pws : http://mawla-raditya-pbpecommerce.pbp.cs.ui.ac.id
tautan menuju link html saya : http://127.0.0.1:8000/


1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
== Pertama saya membuat repository lokal dengan nama PBP-ECOMMERCE, Kemudian saya membuat virtual environment dengan menjalankan komen "python3 -m venv env" dan tidak lupa diikuti pengaktifan virtual environment dengan komen "source env/bin/activate" jika sudah aktif akan terlihat tulisan env pada terminal.  selanjutkan saya membuat file bernama requirements.txt yang didalamnya berisi "django,gunicorn,whitenoise,psycopg2-binary,requests,urllib3".  Kemudian saya melakukan instalasi terhadap dependecies dengan perintah "pip install -r requirements.txt" dan dilanjutkan dengan membuat proyek Django dengan perintah "django-admin startproject pbp_ecommerce .".  Setelah itu, saya melakukan perubahan dalam berkas settings.py yaitu pada (ALLOWED_HOSTS = ["localhost", "127.0.0.1"]).  Dan terakhir tinggal dijalankan servernya dengan perintah "python3 manage.py runserver" dan untuk menonaktifkannya tekan Control+C.  Tidak lupa juga saya menyambungkan dengan github dan juga PWS pacil. Dalam proses penyambungan terhadap PWS saya tidak lupa mengubah pada folder setting.py dengan menambahkan "mawla-raditya-pbpecommerce.pbp.cs.ui.ac.id" pada settingan ALLOWED_HOSTS dan tidak lupa juga melakukan git push pada pws ataupun github.  Kemudian saya menambahkan path ('', include'main.urls') pada berkas urls.py yang berada pada directory pbp_ecommerce.  Pada file models.py yang ada di directory main, saya menambahkan beberapa attribute yang dibutuhkan yaitu :
    name = tipe CharField()
    desc = tipe TextField()
    price = tipe IntegerField()
    stock = tipe IntegerField()
    image = tipe CharField()
Kemudian membuat fuction home pada pada views.py yang nantinya berguna untuk merender atau menampilkan file html yang ada pada templates



2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
== Client (Browser)
     |
     | 1. HTTP Request 
     |
     v
urls.py
     |
     | 2. URL pattern matching
     |
     v
views.py
     |
     | 3. View Function/Method is called
     |    - It interact with models.py
     v
models.py 
     |
     | 4. Query Database (optional)
     |    - Return data to views.py
     v
views.py
     |
     | 5. Render HTML Template
     |    - Pass data to template
     v
HTML Template (e.g., template.html)
     |
     | 6. HTML Response
     |
     v
Client (Browser)



3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
== - Melacak Perubahan: Git menyimpan catatan dari setiap perubahan yang dilakukan.
-Bekerja dalam Tim: Git memungkinkan banyak pengembang untuk bekerja pada proyek yang sama secara bersamaan tanpa saling mengganggu pekerjaan satu sama lain.
-Branching: Git memungkinkan pengembang membuat cabang (branch) dari kode utama untuk mengerjakan fitur atau perbaikan secara terpisah. 
-Repositori Lokal dan Jarak Jauh: Git bekerja dengan repositori lokal (di komputer pengembang) dan repositori jarak jauh (misalnya di GitHub, GitLab, atau Bitbucket). Ini memungkinkan pengembang bekerja secara offline dan menyinkronkan pekerjaan mereka dengan tim saat mereka online.
-Pull dan Push: Pengembang dapat "pull" (menarik) perubahan terbaru dari repositori jarak jauh atau "push" (mendorong) perubahan mereka sendiri ke repositori jarak jauh



4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
== Django cocok untuk pemula karena:
-Fitur Lengkap: Banyak fitur bawaan memudahkan belajar tanpa banyak tambahan.
-Struktur Jelas: Pola MVT membantu memahami arsitektur perangkat lunak.
-Dokumentasi Bagus: Dokumentasinya lengkap dan mudah diikuti.
-Komunitas Aktif: Banyak sumber belajar dan dukungan dari komunitas.
-Skalabilitas: Bisa digunakan untuk proyek kecil hingga besar.

Semua ini menjadikan Django ideal untuk memulai belajar pengembangan perangkat lunak.



5. Mengapa model pada Django disebut sebagai ORM?
== Model di Django disebut ORM karena menghubungkan database dengan kode Python. Ini memungkinkan kita mengelola data di database menggunakan objek Python tanpa menulis SQL langsung.