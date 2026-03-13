import asyncio
import aiohttp

# Write a Python script that sends 20 concurrent prompts to an inference API.

URL = "http://localhost:8000/v1/chat/completions"

async def send_prompt(session, prompt):
         payload = { "model: "llama", "prompt": prompt, "max_tokens": 30 }

         async with session.post(URL, json=payload) as resp:
              data = await resp.json()
              return data["choices"][0]["text"]

async def main()
    prompts = [f "Explain concept {i}" for i in range(20)]

    async with aiohttp.ClientSession() as sessions:
         tasks = [send_prompt(session, p) for p in prompts]
         results = await asyncio.gather(*tasks)

     for r in results:  
         print(r)

asyncio.run(main())

# The script concurrently fires 20 LLM requests using a single async session,
# gathers all results without blocking, and prints them 
# turning what would be 20 sequential waits into one parallel wait."
