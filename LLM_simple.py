# LLM_simple.py
import warnings
warnings.filterwarnings("ignore")

# Try to import transformers
try:
    from transformers import pipeline
    HAS_TRANSFORMERS = True
except ImportError:
    HAS_TRANSFORMERS = False
    print("Transformers not installed. Install with: pip install transformers")

class SimpleLLM:
    def __init__(self):
        self.pipeline = None
        if HAS_TRANSFORMERS:
            try:
                print("Loading model (this may take a minute on first run)...")
                self.pipeline = pipeline(
                    "text-generation",
                    model="Qwen/Qwen2.5-1.5B-Instruct",
                    device_map="auto"
                )
                print("Model loaded successfully!")
            except Exception as e:
                print(f"Error loading model: {e}")
                self.pipeline = None
        else:
            print("Please install transformers: pip install transformers torch")
    
    def get_response(self, user_input):
        if not self.pipeline:
            return "[LLM not available. Please install required packages]"
        
        try:
            prompt = f"User: {user_input}\nAssistant:"
            response = self.pipeline(
                prompt,
                max_new_tokens=100,
                do_sample=True,
                temperature=0.7
            )
            output = response[0]["generated_text"].split("Assistant:")[-1]
            return output.strip()
        except Exception as e:
            return f"[Error: {e}]"


def get_llm_response(user_input: str) -> str:
    if 'llm' not in get_llm_response.__dict__:
        get_llm_response.llm = SimpleLLM()
    return get_llm_response.llm.get_response(user_input)


if __name__ == "__main__":
    print("=" * 50)
    print("Modern LLM Chatbot")
    print("=" * 50)
    print("Type 'quit' to exit.\n")
    
    bot = SimpleLLM()
    
    while True:
        user = input("You: ").strip()
        if user.lower() in ["quit", "exit", "bye"]:
            print("LLM: Goodbye!")
            break
        print("LLM: ", end="")
        response = bot.get_response(user)
        print(f"{response}\n")