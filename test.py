from llama_cpp import Llama

model_path = "C:\\ai-models\\phi-4-q4.gguf"
llm = Llama(model_path=model_path)

messages = [
    {"role": "system", "content": "すべての応答は日本語で答えてください。"},
    {"role": "user", "content": "AIについて冗談を教えてください。"}
]

output = llm.create_chat_completion(messages, max_tokens=50, temperature=0.7, stream=True)

for chunk in output:
    delta = chunk["choices"][0].get("delta", {})
    content = delta.get("content")
    if content:
        print(content, end="", flush=True)
#    print(chunk)