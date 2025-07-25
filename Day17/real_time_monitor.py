import time
def log_stream_monitor(file_path):
    with open(file_path, 'r') as file:
        file.seek(0, 2)  # Go to end of file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue
            if "ERROR" in line or "WARNING" in line:
                yield line.strip()
log_file_path = "server.log"  # Replace with your log file path

try:
    for log in log_stream_monitor(log_file_path):
        print("⚠️ Log Match:", log)
except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")
