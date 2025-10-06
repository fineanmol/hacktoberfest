import speedtest
import json
import csv
import os
from datetime import datetime

# Automatically use the folder where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result = {
        "timestamp": timestamp,
        "download_mbps": round(download, 2),
        "upload_mbps": round(upload, 2),
        "ping_ms": round(ping, 2)
    }

    return result

def log_to_csv(data):
    csv_path = os.path.join(BASE_DIR, "speed_log.csv")
    file_exists = os.path.exists(csv_path)

    with open(csv_path, 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def log_to_json(data):
    json_path = os.path.join(BASE_DIR, "speed_log.json")
    with open(json_path, "a") as jf:
        jf.write(json.dumps(data) + "\n")

def main():
    print("Running network speed test... please wait.")
    result = test_speed()
    print(f"\n📶 Download: {result['download_mbps']} Mbps")
    print(f"🚀 Upload: {result['upload_mbps']} Mbps")
    print(f"⚡ Ping: {result['ping_ms']} ms\n")

    log_to_csv(result)
    log_to_json(result)

    print(f"✅ Results saved in:\n   {os.path.join(BASE_DIR, 'speed_log.csv')}\n   {os.path.join(BASE_DIR, 'speed_log.json')}")

if __name__ == "__main__":
    main()
