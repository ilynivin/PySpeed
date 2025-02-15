import speedtest

st = speedtest.Speedtest()
st.get_best_server()

print("Speed Test in Process...\n Usually it requires less than a minute.\n")

ping = st.results.ping
download_bps = st.download()
upload_bps = st.upload()

def main(download_bps, upload_bps, ping):

    print("- - - RESULTS - - -")
    print(f"Your ping is {ping} ms")

    ### DOWNLOAD SECTION

    try:
        # Gbps
        if download_bps > 999999999:
            print(f"Download Speed : {int((download_bps / 1_000_000_000))} Gbps")
        # Mbps
        elif download_bps <= 999999999 and download_bps > 999999:
            print(f"Download Speed : {int((download_bps / 1_000_000))} Mbps")
        # Kbps
        elif download_bps <= 999999 and download_bps > 999:
            print(f"Download Speed : {int((download_bps / 1_000))} Kbps")
        # Bps
        elif download_bps <= 999 and download_bps > 1:
            print(f"Download Speed : {int((download_bps / 1))} Bps")
        else:
            print(f"Something got wrong. Try again")
    except TypeError as e:
            print(f"An error occurred: {e}")

    ### UPLOAD SECTION

    try:
        # Gbps
        if upload_bps > 999999999:
            print(f"Upload Speed : {int((upload_bps // 1_000_000_000))} Gbps")
        # Mbps
        elif upload_bps <= 999999999 and upload_bps > 999999:
            print(f"Upload Speed : {int((upload_bps // 1_000_000))} Mbps")
        # Kbps
        elif upload_bps <= 999999 and upload_bps > 999:
            print(f"Upload Speed : {int((upload_bps // 1_000))} Kbps")
        # Bps
        elif upload_bps <= 999 and upload_bps > 1:
            print(f"Upload Speed : {int((upload_bps // 1))} Bps")
        else:
            print(f"Something got wrong. Try again")
    except TypeError as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main(download_bps, upload_bps, ping)