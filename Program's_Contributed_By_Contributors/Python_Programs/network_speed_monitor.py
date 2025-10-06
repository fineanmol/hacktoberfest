import speedtest
import csv
from datetime import datetime
import time

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000   # Convert to Mbps
    upload_speed = st.upload() / 1_000_000       # Convert to Mbps
    ping = st.results.ping
    return download_speed, upload_speed, ping

def log_speed(download, upload, ping):
    filename = "network_speed_log.csv"
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create file with headers if not exist
    try:
        with open(filename, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])
    except FileExistsError:
        pass

    # Append new entry
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([time_now, f"{download:.2f}", f"{upload:.2f}", f"{ping:.2f}"])

def main():
    print("=== 🌐 Network Speed Monitor ===")
    print("Press Ctrl+C to stop.\n")

    while True:
        try:
            download, upload, ping = test_speed()
            print(f"[{datetime.now().strftime('%H:%M:%S')}] "
                  f"Download: {download:.2f} Mbps | Upload: {upload:.2f} Mbps | Ping: {ping:.2f} ms")

            log_speed(download, upload, ping)
            time.sleep(300)  # Run test every 5 minutes

        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == "__main__":
    main()
