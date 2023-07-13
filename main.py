import speedtest

st = speedtest.Speedtest()

print("Speed Test in Process....")
print("Download Speed :" , st.download())
print("Upload Speed :" , st.upload())