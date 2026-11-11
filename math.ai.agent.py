class CareerAgent:
    def __init__(self):
        self.name = "CareerAgent"
    
    def calculate(self, expression):
        try:
            # Safe evaluation for basic math
            allowed = {"__builtins__": None}
            result = eval(expression, allowed)
            return f"Result: {result}"
        except:
            return "Sorry, I can only do basic math (e.g. 25 * 4 + 10)"
    
    def format_text(self, text, style):
        if style == "upper":
            return text.upper()
        elif style == "title":
            return text.title()
        elif style == "bullet":
            return "\n".join([f"• {line.strip()}" for line in text.split(",")])
        else:
            return text
    
    def respond(self, user_input):
        user_input = user_input.lower().strip()
        
        if user_input.startswith("calc "):
            expr = user_input[5:]
            return self.calculate(expr)
        
        if user_input.startswith("format "):
            parts = user_input.split(" ", 2)
            if len(parts) >= 3:
                return self.format_text(parts[2], parts[1])
        
        if "resume" in user_input:
            return "Tip: Use strong action verbs and numbers. Example: 'Reduced processing time by 30%.'"
        if "python" in user_input:
            return "Practice daily. Build small tools like this agent or a resume generator."
        if "hello" in user_input or "hi" in user_input:
            return f"Hello! I'm {self.name}. Try: calc 15*8, format title hello world, or ask about resume/python."
        
        return "I can help with calculations, text formatting, resume tips, and Python advice. Type 'help' for examples."

agent = CareerAgent()
print("CareerAgent ready. Type 'quit' to exit.\n")

while True:
    msg = input("You: ")
    if msg.lower() == "quit":
        break
    print("Agent:", agent.respond(msg))
    print()
