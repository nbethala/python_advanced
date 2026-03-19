from handler import handle_request

def run_case(name: str, req: dict) -> None:
    print(f"\n--- {name} ---")
    print("input:", req)
    result = handle_request(req)
    print("output:", result)


run_case("valid request", {"prompt": "Explain KV cache", "max_tokens": 100})
run_case("default max_tokens", {"prompt": "Hello"})
run_case("missing prompt", {"max_tokens" : 20})


run_case("empty prompt", {"prompt": ""})
run_case("wrong type for max_tokens", {"prompt": "Hi", "max_tokens": "abc"})
run_case("prompt is None", {"prompt": None})
run_case("unexpected key", {"text": "Hello"})