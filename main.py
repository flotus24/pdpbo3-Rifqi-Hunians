from apartemen import Apartemen
from rumah import Rumah
from tkinter import *
from tkinter import messagebox

hunians = []

root = Tk()
root.title("HUNIANS")

def details(index):
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
    d_summary = Label(d_frame, text="Pemilik: " + hunians[index].get_dokumen(), anchor="w").grid(row=1, column=0, sticky="w")
    d_summary = Label(d_frame, text="Jenis kelamin: " + hunians[index].get_jenis_kelamin(), anchor="w").grid(row=2, column=0, sticky="w")
    d_summary = Label(d_frame, text="Jumlah Kamar: " + hunians[index].get_jml_kamar(), anchor="w").grid(row=3, column=0, sticky="w")
    d_summary = Label(d_frame, text="Fasilitas tambahan: ", anchor="w").grid(row=4, column=0, sticky="w")
    if hunians[index].get_kolam() != "0":
        d_summary = Label(d_frame, text=hunians[index].get_kolam(), anchor="w").grid(row=5, column=0, sticky="w")
    if hunians[index].get_halaman() != "0":
        d_summary = Label(d_frame, text=hunians[index].get_halaman(), anchor="w").grid(row=6, column=0, sticky="w")
    if hunians[index].get_garasi() != "0":
        d_summary = Label(d_frame, text=hunians[index].get_garasi(), anchor="w").grid(row=7, column=0, sticky="w")
    btn_exit = Button(d_frame, text="Exit", command=top.destroy, anchor="w").grid(row=10, column=1, sticky="w")

def about():
    top = Toplevel()
    top.title("Tentang kami")

    d_frame = LabelFrame(top, padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)

    d_summary = Label(d_frame, text="APLIKASI HUNIANS", anchor="w").grid(row=0, column=0, sticky="n")
    d_summary = Label(d_frame, text="Aplikasi pendataan hunian", anchor="w").grid(row=1, column=0, sticky="n")
    d_summary = Label(d_frame, text="dengan fungsionalitas yang membantu proses bisnis sebuah perusahaan", anchor="w").grid(row=2, column=0, sticky="w")
    d_summary = Label(d_frame, text="Dibuat oleh :", anchor="w").grid(row=3, column=0, sticky="n")
    d_summary = Label(d_frame, text="Muhammad Rifqi(1908083)", anchor="w").grid(row=4, column=0, sticky="n")

def show():
    top = Toplevel()
    top.title("Melihat semua masukkan")

    s_frame = LabelFrame(top, padx=10, pady=10)
    s_frame.pack(padx=10, pady=10)

    for widget in s_frame.winfo_children():
        widget.destroy()

    for index, h in enumerate(hunians):
        idx = Label(s_frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(s_frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(s_frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(s_frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(s_frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    if not hunians:
        kosong = Label(s_frame, text="Belum ada data atau masukkan").grid(row=0, column=3)

    btn_exit = Button(s_frame, text="Exit", command=top.destroy, anchor="w").grid(row=10, column=3, sticky="e")

def isi():
    if not (input_nama.get()):
        response = messagebox.showwarning("Peringatan", "Field text masih ada yang kosong!")
    elif not (input_jml_penghuni.get()):
        response = messagebox.showwarning("Peringatan", "Field text masih ada yang kosong!")
    elif not (input_jml_kamar.get()):
        response = messagebox.showwarning("Peringatan", "Field text masih ada yang kosong!")
    else:
        response = messagebox.showinfo("Berhasil", "Data berhasil disimpan!")
        if tipe.get() == "Rumah":
            hunians.append(Rumah(input_nama.get(), input_jenis_kelamin.get(), input_jml_penghuni.get(), input_jml_kamar.get(), kolam.get(), halaman.get(), garasi.get()))
        if tipe.get() == "Apartemen":
            hunians.append(Apartemen(input_nama.get(), input_jenis_kelamin.get(), input_jml_penghuni.get(), input_jml_kamar.get(), kolam.get(), halaman.get(), garasi.get()))

def popup_exit():
    response = messagebox.askquestion("Peringatan", "Yakin ingin keluar?")
    if response == "yes":
        root.destroy()

def popup_clear():
    response = messagebox.askquestion("Peringatan", "Yakin ingin menghapus semua data?")
    if response == "yes":
        if not hunians:
            response = messagebox.showinfo("Pemberitahuan", "Data masih kosong!")
        else:
            response = messagebox.showinfo("Pemberitahuan", "Semua data telah dihapus!")
            hunians.clear()

#Inisialisasi frame
frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
frame.pack(padx=10, pady=10)

main = LabelFrame(root, padx=10, pady=10, borderwidth=0, highlightthickness=0)
main.pack(padx=10, pady=10)

form = LabelFrame(root, padx=10, text="Form Pengisian Hunian", pady=10)
form.pack(padx=10, pady=10)

#Variabel Tkinter
input_jenis_kelamin = StringVar()
input_jenis_kelamin.set("Laki-laki")
tipe = StringVar()
tipe.set("Apartemen")
kolam = StringVar()
halaman = StringVar()
garasi = StringVar()

#layout main
b_show = Button(main, text="Show Submissions", command=show, width=30).pack()
b_clear = Button(main, text="Clear Submissions", command=popup_clear, width=30).pack()
b_about = Button(main, text="About", command=about, width=30, ).pack()
b_exit = Button(main, text="Exit", command=popup_exit, width=30)
b_exit.pack()

#Inisialisasi label dan input
lbl_nama = Label(form, text="Nama ", anchor="w", width=15)
lbl_jenis_kelamin = Label(form, text="Jenis Kelamin ", anchor="w", width=15)
lbl_jml_penghuni = Label(form, text="Jumlah Penghuni ",anchor="w", width=15)
lbl_jml_kamar = Label(form, text="Jumlah Kamar ", anchor="w", width=15)
lbl_tipe = Label(form, text="Tipe ", anchor="w", width=15)
lbl_fasilitas = Label(form, text="Fasilitas ", anchor="w", width=15)
input_nama = Entry(form)
Radiobutton(form, text="Laki-laki", variable=input_jenis_kelamin, value="Laki-laki", anchor="w", width=15).grid(row=1, column=1)
Radiobutton(form, text="Perempuan", variable=input_jenis_kelamin, value="Perempuan", anchor="w", width=10).grid(row=1, column=2)
input_jml_penghuni = Entry(form)
input_jml_kamar = Entry(form)
input_tipe = OptionMenu(form, tipe, "Apartemen", "Rumah")
input_tipe.config(anchor="w", width=15)
input_kolam = Checkbutton(form, text="Kolam Renang", variable=kolam, onvalue="Kolam Renang", anchor="w", width=15)
input_kolam.deselect()
input_halaman = Checkbutton(form, text="Halaman", variable=halaman, onvalue="Halaman", anchor="w", width=10)
input_halaman.deselect()
input_garasi = Checkbutton(form, text="Garasi", variable=garasi, onvalue="garasi", anchor="w", width=10)
input_garasi.deselect()

#Layout form
lbl_nama.grid(row=0 , column=0)
lbl_jenis_kelamin.grid(row=1, column=0)
lbl_jml_penghuni.grid(row=2 , column=0)
lbl_jml_kamar.grid(row=3 , column=0)
lbl_tipe.grid(row=4 , column=0)
lbl_fasilitas.grid(row=5 , column=0)
input_nama.grid(row=0 , column=1)
input_jml_penghuni.grid(row=2 , column=1)
input_jml_kamar.grid(row=3 , column=1)
input_tipe.grid(row=4, column=1)
input_kolam.grid(row=5, column=1)
input_halaman.grid(row=5, column=2)
input_garasi.grid(row=5, column=3)
lbl_kosong = Label(form, text=" ")
lbl_kosong.grid(row=8, column=0)
b_add = Button(form, text="Add Data", command=isi)
b_add.grid(row=9, column=1)

root.mainloop()
