def handle_request(req: dict) -> dict:
    if "prompt" not in req:
        return {"status": "error", "error": "missing prompt"}

    prompt = req["prompt"]
    if not isinstance(prompt, str) or not prompt.strip():
        return {"status": "error", "error": "prompt must be a non-empty string"}

    max_tokens = req.get("max_tokens", 50)
    if not isinstance(max_tokens, int) or max_tokens <= 0:
        return {"status": "error", "error": "max_tokens must be a positive integer"}

    return {
        "status": "ok",
        "data": {
            "prompt": prompt,
            "max_tokens": max_tokens,
        },
    }