# learning/04_broken.py
import json, time
from pathlib import Path

p = Path("out.json")
for i in range(10_000):
    with open(p, "w") as f:       # ← truncates every iteration
        json.dump({"i": i}, f)
    time.sleep(0.001)