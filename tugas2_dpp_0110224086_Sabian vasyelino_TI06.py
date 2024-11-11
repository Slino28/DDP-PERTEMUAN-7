# Data pegawai
p1 = {"Nama": "Budi", "Jabatan": "Manager", "Agama": "Islam", "Status": "Menikah"}
p2 = {"Nama": "Siti", "Jabatan": "Asisten Manager", "Agama": "Islam", "Status": "Menikah"}
p3 = {"Nama": "I_Gede", "Jabatan": "SuperVisor", "Agama": "Hindu", "Status": "Menikah"}
p4 = {"Nama": "Joko", "Jabatan": "Staff", "Agama": "Islam", "Status": "Belum Menikah"}
p5 = {"Nama": "Alex", "Jabatan": "Staff", "Agama": "Kristen Protestan", "Status": "Belum Menikah"}

ar_pegawai = [p1,p2,p3,p4,p5]

for pegawai in ar_pegawai:
    if pegawai["Jabatan"] == "Manager":
        pegawai ["gaji_pokok"] = 15000000
    elif pegawai["Jabatan"] == "Asisten Manager":
        pegawai ["gaji_pokok"] = 10000000
    elif pegawai["Jabatan"] == "SuperVisor":
        pegawai ["gaji_pokok"] = 7000000
    elif pegawai["Jabatan"] == "Staff":
        pegawai ["gaji_pokok"] = 4000000
    else :
        pegawai["gaji_pokok"] = 0    

    pegawai["tunjab"] = pegawai["gaji_pokok"] * 0.3
    pegawai["bpjs"] = pegawai["gaji_pokok"] * 0.1
    pegawai["tunjangan_keluarga"] = (0,pegawai ["gaji_pokok"] * 0.1)[pegawai["Status"] == "Menikah"]
    pegawai["gaji_kotor"] = pegawai ["gaji_pokok"] + pegawai["tunjab"] + pegawai["tunjangan_keluarga"] + pegawai["bpjs"]
    pegawai["Zakat"] = (0.025 * pegawai ["gaji_kotor"]) if (pegawai["Agama"] == "Islam" and pegawai["gaji_pokok"] >= 7000000) else 0
    pegawai["gaji_bersih"] = pegawai ["gaji_kotor"] - pegawai["Zakat"]

    print (f"Nama \t\t\t: {pegawai["Nama"]}"
           f"\nJabatan \t\t: {pegawai["Jabatan"]}"
           f"\nAgama \t\t\t: {pegawai["Agama"]}"
           f"\nStatus \t\t\t: {pegawai["Status"]}"
           f"\nGaji pokok \t\t: Rp{pegawai["gaji_pokok"]:,}"
           f"\nTunjangan _Jabatan \t: Rp{pegawai["tunjab"]:,}"
           f"\nBPJS \t\t\t: Rp{pegawai['bpjs']:,}"
           f"\nTunjangan_keluarga \t: Rp{pegawai["tunjangan_keluarga"]:,}"
           f"\nGaji_kotor \t\t: Rp{pegawai["gaji_kotor"]:,}"
           f"\nZakat \t\t\t: Rp{pegawai['Zakat']:,}"
           f"\nGaji_bersih \t\t: Rp{pegawai['gaji_bersih']:,}\n")