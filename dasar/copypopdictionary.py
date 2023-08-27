# copy dictonary
teman_teman = {
    "cup" : "ucup surucup",
    "tong" : "otong surotong",
    "dung" : "dudung surudung",
    "sep" : "asep si kasep",
    "cuy" : "ucuy surucuy"
}

friends = teman_teman.copy()
print(f"teman =\n {teman_teman}")
print(f"friends =\n {friends}")

teman_teman ["cup"] = "ucup si keren"
print(f"teman =\n {teman_teman}")
print(f"friends =\n {friends}")

# pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}")
print(f"data friends = {friends}")

# pop item dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()
print(f"data terakhir = {dataTerakhir}")
print(f"data friends = {friends}")
