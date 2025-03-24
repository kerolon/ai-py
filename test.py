from llama_cpp import Llama

model_path = "C:\\ai-models\\phi-4-q4.gguf"
llm = Llama(model_path=model_path)

system_messages = [
    {"role": "system", "content": "すべての応答は日本語で答えてください。"}
]


def chat():
    # ユーザー入力の受付
        user_input = input("\nあなた: ")

        messages = [
            system_messages,
            {"role": "user", "content": user_input}
        ]

        # 応答の生成
        print("\nAI: ", end="", flush=True)
        output = llm.create_chat_completion(messages, max_tokens=50, temperature=0.7, stream=True)

        for chunk in output:
            delta = chunk["choices"][0].get("delta", {})
            content = delta.get("content")
            if content:
                print(content, end="", flush=True)
        print("")
if __name__ == "__main__":
    print("Q&Aを開始します")
    chat()