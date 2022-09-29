# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

link menuju aplikasi Heroku : 

- https://pbptugas2jessica.herokuapp.com/todolist


1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?

{% csrf_token %} digunakan untuk menambah keamanan pada aplikasi. Memungkinkan adanya serangan dari domain tidak terpercaya, apabila tidak ada kode tersebut

2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.

Tanpa menggunakan generator, kita bisa membuat elemen form secara manual. Gambaran besarnya dengan menggunakan input dan button untuk elemen yang dapat menyimpan data dari user

3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Data yang diberikan dari user melalui form, akan disimpan dalam bentuk atribut Task yang ada di models.py. Setelah itu data akan disimpan di databse, dan akan dipanggil oleh template HTML.
  
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Melakukan inisiasi aplikasi todolist di command prompt, mengedit views.py dan urls.py sesuai kebutuhan, menambahkan kelas Task serta atribut yang sesuai pada models.py, menambahkan fungsi login-logout-register(pada views.py) serta template HTML-nya, membuat todolist.html serta mengisinya dengan elemen yang sesuai, membuat create-task.html serta forms.py yang sesuai agar bisa menerima input user, melakukan routing pada urls.py. Deployment dengan memantau workflows action pada github
