import time
import requests

URL = "http://localhost:8000/v1/completions"

latencies = []

for _ in range(10):
    start = time.time()

    requests.post(URL, json={
          "model": "llama".
          "prompt": "Explain attention",
          "max_tokens": 20
     })  
    
     latencies.append(time.time() - start)

print ("Average latency:", sum(latencies)/len(latencies))
