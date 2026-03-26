# compare_simple.py
import time
import sys

# Import the chatbots
from eliza_custom import get_eliza_response
from LLM_simple import get_llm_response

def compare_responses(user_input):
    """Compare responses from both chatbots"""
    print(f"\n{'='*60}")
    print(f"User: {user_input}")
    print(f"{'='*60}")
    
    # Get ELIZA response
    start = time.time()
    eliza_response = get_eliza_response(user_input)
    eliza_time = (time.time() - start) * 1000
    print(f"\n[ELIZA] ({eliza_time:.0f}ms)")
    print(f"{eliza_response}")
    
    # Get LLM response
    print(f"\n[LLM] (processing...)")
    start = time.time()
    llm_response = get_llm_response(user_input)
    llm_time = (time.time() - start) * 1000
    print(f"[LLM] ({llm_time:.0f}ms)")
    print(f"{llm_response}")
    
    print(f"\n{'='*60}")
    print(f"Comparison Summary:")
    print(f"- ELIZA speed: {eliza_time:.0f}ms")
    print(f"- LLM speed: {llm_time:.0f}ms")
    if llm_time > 0:
        print(f"- LLM is {llm_time/eliza_time:.1f}x slower than ELIZA")

if __name__ == "__main__":
    print("=" * 60)
    print("AI Comparison: ELIZA (1960s) vs Modern LLM (2020s)")
    print("=" * 60)
    
    # Test prompts from assignment
    test_prompts = [
        "Hello",
        "My name is David",
        "I feel stressed",
        "I am tired",
        "Because I have exams",
        "My mother is strict",
        "I need more sleep"
    ]
    
    print("\nRunning predefined test prompts...\n")
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n--- Test {i}/{len(test_prompts)} ---")
        compare_responses(prompt)
        if i < len(test_prompts):
            input("\nPress Enter to continue to next test...")
    
    # Interactive mode
    print("\n\n" + "="*60)
    print("Interactive Mode - Type your own messages")
    print("Type 'quit' to exit")
    print("="*60)
    
    while True:
        user = input("\nYou: ").strip()
        if user.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        compare_responses(user)
