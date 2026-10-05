import subprocess
import time
import os

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

scenes = [
    'act4_1',
    'act4_2',
    'act4_3',
    'act5_1',
    'act5_2',
    'act5_3',
    'act6_1',
    'act6_2',
    'act6_3',
    'ship_1'
]

os.makedirs('screenshots', exist_ok=True)

for sc in scenes:
    url = f"http://localhost:8080/preview.html?scene={sc}"
    out_file = os.path.abspath(f"screenshots/{sc}.png")
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--window-size=1920,1080",
        f"--screenshot={out_file}",
        url
    ]
    print(f"Capturing {sc}...")
    subprocess.run(cmd, check=True, timeout=15)
    print(f"Captured {out_file} ({os.path.getsize(out_file)} bytes)")
    time.sleep(1)

print("All scenes captured successfully!")
