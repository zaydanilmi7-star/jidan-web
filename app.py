from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

# =====================================
# DATABASE AKUN (DICTIONARY)
# =====================================

akun = {
    "Jidan": "Jidan1234",
    "Salwa": "Salwa1234"
}

# =====================================
# DATA NOTES & TODO
# =====================================

notes = []

todo_list = []


# =====================================
# LOGIN
# =====================================
@app.route("/")
def login():

    return """
    <h1>LOGIN</h1>

    <form action="/cek_login" method="post">

        Username:
        <input type="text" name="username">

        <br><br>

        Password:
        <input type="password" name="password">

        <br><br>

        <button type="submit">Login</button>

    </form>
    """


# =====================================
# CEK LOGIN
# =====================================
@app.route("/cek_login", methods=["POST"])
def cek_login():

    username = request.form["username"]
    password = request.form["password"]

    # Mengecek username dan password
    if username in akun and akun[username] == password:

        return redirect("/menu")

    else:

        return """
        <h1>Login gagal</h1>

        <a href="/">Kembali</a>
        """


# =====================================
# MENU
# =====================================
@app.route("/menu")
def menu():

    return """
    <h1>MENU UTAMA</h1>

    <a href="/kalkulator">1. Kalkulator</a>

    <br><br>

    <a href="/notes">2. Notes</a>

    <br><br>

    <a href="/todo">3. To Do List</a>

    <br><br>

    <a href="/umur">4. Kalkulator Umur</a>

    <br><br>

    <a href="/konverter">5. Konverter</a>

    <br><br>

    <a href="/">Logout</a>
    """


# =====================================
# KALKULATOR
# =====================================
@app.route("/kalkulator")
def kalkulator():

    return """
    <h1>Kalkulator</h1>

    <form action="/hasil_kalkulator" method="post">

        Angka 1:
        <input type="number" step="any" name="angka1">

        <br><br>

        Angka 2:
        <input type="number" step="any" name="angka2">

        <br><br>

        <select name="operator">

            <option value="+">Tambah</option>
            <option value="-">Kurang</option>
            <option value="*">Kali</option>
            <option value="/">Bagi</option>

        </select>

        <br><br>

        <button type="submit">Hitung</button>

    </form>

    <br>

    <a href="/menu">Kembali ke Menu</a>
    """


@app.route("/hasil_kalkulator", methods=["POST"])
def hasil_kalkulator():

    angka1 = float(request.form["angka1"])
    angka2 = float(request.form["angka2"])
    operator = request.form["operator"]

    if operator == "+":
        hasil = angka1 + angka2

    elif operator == "-":
        hasil = angka1 - angka2

    elif operator == "*":
        hasil = angka1 * angka2

    elif operator == "/":

        if angka2 != 0:
            hasil = angka1 / angka2

        else:
            return """
            <h1>Tidak bisa dibagi 0</h1>

            <a href="/kalkulator">Kembali</a>
            """

    return f"""
    <h1>Hasil: {hasil}</h1>

    <a href="/kalkulator">Hitung Lagi</a>

    <br><br>

    <a href="/menu">Kembali ke Menu</a>
    """


# =====================================
# NOTES MENU
# =====================================
@app.route("/notes")
def notes_menu():

    return """
    <h1>NOTES</h1>

    <a href="/tambah_notes">1. Tambah Catatan</a>

    <br><br>

    <a href="/lihat_notes">2. Lihat Catatan</a>

    <br><br>

    <a href="/hapus_notes">3. Hapus Semua Catatan</a>

    <br><br>

    <a href="/menu">Kembali ke Menu</a>
    """


# =====================================
# TAMBAH NOTES
# =====================================
@app.route("/tambah_notes")
def tambah_notes():

    return """
    <h1>Tambah Catatan</h1>

    <form action="/simpan_notes" method="post">

        <input type="text" name="note">

        <button type="submit">Tambah</button>

    </form>

    <br>

    <a href="/notes">Kembali</a>
    """


@app.route("/simpan_notes", methods=["POST"])
def simpan_notes():

    note = request.form["note"]

    notes.append(note)

    return redirect("/lihat_notes")


# =====================================
# LIHAT NOTES
# =====================================
@app.route("/lihat_notes")
def lihat_notes():

    hasil = ""

    if len(notes) == 0:

        hasil = "<p>Belum ada catatan</p>"

    else:

        nomor = 1

        for note in notes:

            hasil += f"<li>{nomor}. {note}</li>"

            nomor += 1

    return f"""
    <h1>Daftar Catatan</h1>

    <ul>
        {hasil}
    </ul>

    <br>

    <a href="/notes">Kembali</a>
    """


# =====================================
# HAPUS NOTES
# =====================================
@app.route("/hapus_notes")
def hapus_notes():

    notes.clear()

    return """
    <h1>Semua catatan berhasil dihapus</h1>

    <a href="/notes">Kembali</a>
    """


# =====================================
# TODO MENU
# =====================================
@app.route("/todo")
def todo_menu():

    return """
    <h1>TO DO LIST</h1>

    <a href="/tambah_todo">1. Tambah Tugas</a>

    <br><br>

    <a href="/lihat_todo">2. Lihat Tugas</a>

    <br><br>

    <a href="/selesai_todo">3. Tandai Selesai</a>

    <br><br>

    <a href="/hapus_todo">4. Hapus Semua Tugas</a>

    <br><br>

    <a href="/menu">Kembali ke Menu</a>
    """


# =====================================
# TAMBAH TODO
# =====================================
@app.route("/tambah_todo")
def tambah_todo():

    return """
    <h1>Tambah Tugas</h1>

    <form action="/simpan_todo" method="post">

        <input type="text" name="tugas">

        <button type="submit">Tambah</button>

    </form>

    <br>

    <a href="/todo">Kembali</a>
    """


@app.route("/simpan_todo", methods=["POST"])
def simpan_todo():

    tugas = request.form["tugas"]

    todo_list.append({
        "nama": tugas,
        "selesai": False
    })

    return redirect("/lihat_todo")


# =====================================
# LIHAT TODO
# =====================================
@app.route("/lihat_todo")
def lihat_todo():

    hasil = ""

    if len(todo_list) == 0:

        hasil = "<p>Belum ada tugas</p>"

    else:

        nomor = 1

        for tugas in todo_list:

            status = "✅" if tugas["selesai"] else "❌"

            hasil += f"<li>{nomor}. {tugas['nama']} {status}</li>"

            nomor += 1

    return f"""
    <h1>Daftar Tugas</h1>

    <ul>
        {hasil}
    </ul>

    <br>

    <a href="/todo">Kembali</a>
    """


# =====================================
# TANDAI TODO SELESAI
# =====================================
@app.route("/selesai_todo", methods=["GET", "POST"])
def selesai_todo():

    if request.method == "POST":

        nomor = int(request.form["nomor"]) - 1

        if 0 <= nomor < len(todo_list):

            todo_list[nomor]["selesai"] = True

        return redirect("/lihat_todo")

    return """
    <h1>Tandai Tugas Selesai</h1>

    <form method="post">

        Nomor tugas:
        <input type="number" name="nomor">

        <button type="submit">Selesai</button>

    </form>

    <br>

    <a href="/todo">Kembali</a>
    """


# =====================================
# HAPUS TODO
# =====================================
@app.route("/hapus_todo")
def hapus_todo():

    todo_list.clear()

    return """
    <h1>Semua tugas berhasil dihapus</h1>

    <a href="/todo">Kembali</a>
    """


# =====================================
# KALKULATOR UMUR
# =====================================
@app.route("/umur")
def umur():

    return """
    <h1>Kalkulator Umur</h1>

    <form action="/hasil_umur" method="post">

        Tanggal lahir:
        <input type="number" name="tanggal">

        <br><br>

        Bulan lahir:
        <input type="number" name="bulan">

        <br><br>

        Tahun lahir:
        <input type="number" name="tahun">

        <br><br>

        <button type="submit">Hitung Umur</button>

    </form>

    <br>

    <a href="/menu">Kembali ke Menu</a>
    """


@app.route("/hasil_umur", methods=["POST"])
def hasil_umur():

    tanggal = int(request.form["tanggal"])
    bulan = int(request.form["bulan"])
    tahun = int(request.form["tahun"])

    sekarang = datetime.now()

    umur = sekarang.year - tahun

    if (sekarang.month, sekarang.day) < (bulan, tanggal):

        umur -= 1

    return f"""
    <h1>Umur kamu sekarang: {umur} tahun</h1>

    <a href="/umur">Hitung Lagi</a>

    <br><br>

    <a href="/menu">Kembali ke Menu</a>
    """


# =====================================
# KONVERTER MENU
# =====================================
@app.route("/konverter")
def konverter():

    return """
    <h1>KONVERTER</h1>

    <a href="/konversi_suhu">1. Suhu</a>

    <br><br>

    <a href="/konversi_panjang">2. Panjang</a>

    <br><br>

    <a href="/konversi_berat">3. Berat</a>

    <br><br>

    <a href="/konversi_volume">4. Volume</a>

    <br><br>

    <a href="/menu">Kembali ke Menu</a>
    """


# =====================================
# KONVERSI SUHU
# =====================================
@app.route("/konversi_suhu", methods=["GET", "POST"])
def konversi_suhu():

    if request.method == "POST":

        c = float(request.form["celcius"])

        f = (c * 9/5) + 32

        return f"""
        <h1>Hasil: {f} Fahrenheit</h1>

        <a href="/konversi_suhu">Kembali</a>
        """

    return """
    <h1>Celcius ke Fahrenheit</h1>

    <form method="post">

        <input type="number" step="any" name="celcius">

        <button type="submit">Convert</button>

    </form>

    <br>

    <a href="/konverter">Kembali</a>
    """


# =====================================
# KONVERSI PANJANG
# =====================================
@app.route("/konversi_panjang", methods=["GET", "POST"])
def konversi_panjang():

    if request.method == "POST":

        meter = float(request.form["meter"])

        hasil = meter / 1000

        return f"""
        <h1>Hasil: {hasil} Kilometer</h1>

        <a href="/konversi_panjang">Kembali</a>
        """

    return """
    <h1>Meter ke Kilometer</h1>

    <form method="post">

        <input type="number" step="any" name="meter">

        <button type="submit">Convert</button>

    </form>

    <br>

    <a href="/konverter">Kembali</a>
    """


# =====================================
# KONVERSI BERAT
# =====================================
@app.route("/konversi_berat", methods=["GET", "POST"])
def konversi_berat():

    if request.method == "POST":

        kg = float(request.form["kg"])

        hasil = kg * 1000

        return f"""
        <h1>Hasil: {hasil} Gram</h1>

        <a href="/konversi_berat">Kembali</a>
        """

    return """
    <h1>Kilogram ke Gram</h1>

    <form method="post">

        <input type="number" step="any" name="kg">

        <button type="submit">Convert</button>

    </form>

    <br>

    <a href="/konverter">Kembali</a>
    """


# =====================================
# KONVERSI VOLUME
# =====================================
@app.route("/konversi_volume", methods=["GET", "POST"])
def konversi_volume():

    if request.method == "POST":

        liter = float(request.form["liter"])

        hasil = liter * 1000

        return f"""
        <h1>Hasil: {hasil} Mililiter</h1>

        <a href="/konversi_volume">Kembali</a>
        """

    return """
    <h1>Liter ke Mililiter</h1>

    <form method="post">

        <input type="number" step="any" name="liter">

        <button type="submit">Convert</button>

    </form>

    <br>

    <a href="/konverter">Kembali</a>
    """


# =====================================
# MENJALANKAN WEBSITE
# =====================================
app.run(host="0.0.0.0", port=5000, debug=True)