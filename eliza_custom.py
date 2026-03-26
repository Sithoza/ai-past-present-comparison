# eliza_custom.py
import re
import random

class ElizaChatbot:
    def __init__(self):
        # Define reflection patterns (you to me, me to you)
        self.reflections = {
            "am": "are",
            "was": "were",
            "i": "you",
            "i'd": "you would",
            "i've": "you have",
            "i'll": "you will",
            "my": "your",
            "are": "am",
            "you've": "I have",
            "you'll": "I will",
            "your": "my",
            "yours": "mine",
            "you": "me",
            "me": "you"
        }
        
        # Define response patterns
        self.responses = [
            (r"hello|hi|hey", [
                "Hello! How are you feeling today?",
                "Hi there! How can I help you?",
                "Hello. Tell me what's on your mind."
            ]),
            
            (r"my name is (.*)", [
                "Nice to meet you, {0}. How are you feeling?",
                "Hello {0}. What brings you here today?",
                "{0} is a nice name. How can I help you?"
            ]),
            
            (r"I feel (.*)", [
                "Why do you feel {0}?",
                "Tell me more about feeling {0}.",
                "What makes you feel {0}?"
            ]),
            
            (r"I am (.*)", [
                "Why are you {0}?",
                "What caused you to be {0}?",
                "How long have you been {0}?"
            ]),
            
            (r"I am tired|I'm tired", [
                "What's making you feel tired?",
                "Have you been sleeping well?",
                "Would you like to talk about what's exhausting you?"
            ]),
            
            (r"because (.*)", [
                "I see. Does that bother you?",
                "Tell me more about that reason.",
                "How does that make you feel?"
            ]),
            
            (r"my mother (.*)|my father (.*)", [
                "Tell me more about your family.",
                "How does that relationship affect you?",
                "Why do you mention your parent?"
            ]),
            
            (r"I need (.*)", [
                "Why do you need {0}?",
                "What would having {0} do for you?",
                "How important is {0} to you?"
            ]),
            
            (r"quit|bye|goodbye", [
                "Goodbye! Take care of yourself.",
                "Thank you for talking. Goodbye!",
                "Farewell! I hope you feel better soon."
            ])
        ]
        
        # Default responses
        self.default_responses = [
            "I see. Please tell me more.",
            "That's interesting. Go on.",
            "Can you elaborate on that?",
            "Why do you say that?",
            "Tell me more about that."
        ]
    
    def reflect(self, text):
        """Replace pronouns to reflect the user's statement back"""
        words = text.lower().split()
        reflected_words = []
        for word in words:
            if word in self.reflections:
                reflected_words.append(self.reflections[word])
            else:
                reflected_words.append(word)
        return " ".join(reflected_words)
    
    def respond(self, user_input):
        """Generate a response based on pattern matching"""
        user_input_lower = user_input.lower().strip()
        
        # Check each pattern
        for pattern, response_list in self.responses:
            match = re.search(pattern, user_input_lower)
            if match:
                # Extract matched groups
                groups = match.groups()
                if groups:
                    # Reflect the matched groups back to the user
                    reflected_groups = [self.reflect(group) for group in groups if group]
                    if reflected_groups:
                        response = random.choice(response_list)
                        response = response.format(*reflected_groups)
                    else:
                        response = random.choice(response_list)
                else:
                    response = random.choice(response_list)
                return response
        
        # Default response if no pattern matches
        return random.choice(self.default_responses)


def get_eliza_response(user_input: str) -> str:
    """Wrapper function for compatibility"""
    if 'eliza_bot' not in get_eliza_response.__dict__:
        get_eliza_response.eliza_bot = ElizaChatbot()
    return get_eliza_response.eliza_bot.respond(user_input)


if __name__ == "__main__":
    print("=" * 50)
    print("ELIZA Chatbot - A Rogerian Psychotherapist")
    print("=" * 50)
    print("Type 'quit' to exit.\n")
    
    bot = ElizaChatbot()
    
    while True:
        user = input("You: ").strip()
        
        if user.lower() in ["quit", "exit", "bye"]:
            print("ELIZA: Goodbye! Take care of yourself.")
            break
        
        response = bot.respond(user)
        print(f"ELIZA: {response}\n")