# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

link menuju aplikasi Heroku : 

- https://pbptugas2jessica.herokuapp.com/todolist


## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
Inline CSS: kode CSS yang ditulis secara langsung pada setiap atribut HTML
kelebihan Inline CSS: load website menjadi lebih cepat dan HTTP request menjadi lebih kecil
kekurangan Inline CSS: jika kode css kompleks, maka akan sulit dibaca kode css tersebut


Internal CSS: Internal CSS adalah kode CSS yang ditulis dalam tag <style> dan lokasinya berada pada file HTML. Internal CSS biasanya digunakan untuk membuat style khusus dalam satu halaman website.
kelebihan Internal CSS: dapat membuat kustomisasi per halaman/per file html
kekurangan Internal CSS: tidal efektif jika digunakan pada banyak file karena akan terjadi duplikasi kode



External CSS: kode CSS yang penulisannya dipisah dengan file HTML. Jadi file CSS ditulis pada file terpisah. File External CSS biasanya dipanggil pada bagian <head> dari file html.
kelebihan External CSS: lebih mudah dibaca dan kode dapat digunakan pada banyak file tanpa adanya duplikasi kode
kekurangan External CSS: 	halaman website rawan berantakan saat file CSS gagal load dengan sempurna sehingga tampilan website berantakan.




## Jelaskan tag HTML5 yang kamu ketahui.
1. <title> = Mengatur title website (pada bagian tab)
2. <form> = Membuat form untuk input user
3. <a> = Mendefinisikan link
4. <div> = Mendefinisikan bagian tertentu dalam document.
5. <h…> = Mendefinisikan header pada dokumen html.
6. <nav> = Mendefinisikan navigasi link.
7. <style> = Mendefinisikan style untuk css.
8. <button> = Membuat tombol

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Tag Selector = selector yang menuju tag html (seperti h1, button, dll).
2. ID Selector = selector yang menunjuk pada id dari elemen html. Implementasi dengan (#)
3. Class Selector = selector yang menunjuk pada eleven html yang mempunyai class tertentu. Implements dengan (.)


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
Menggunakan kustomisasi halaman-halaman dan elemen-elemen dengan menggunakan css dan framework css bootstrap. Lalu melakukan save lulu, git add, dan commit. Serta melakukan push untuk dideploy sehingga web sudah terdeploy dengan style.
