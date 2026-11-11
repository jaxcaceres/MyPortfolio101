# Simple Rule-Based AI Agent
def simple_agent():
    print("Hello! I'm a simple career assistant agent.")
    print("I can help with: resume tips, Python practice, or general advice.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "quit":
            print("Agent: Good luck with your software engineering journey!")
            break
            
        elif "resume" in user_input:
            print("Agent: Focus on quantifiable impact. Example: 'Reduced resolution time by 30% using standardized workflows.'")
            
        elif "python" in user_input or "code" in user_input:
            print("Agent: Start with small scripts every day. Build a resume generator or a simple calculator first.")
            
        elif "job" in user_input or "interview" in user_input:
            print("Agent: Highlight your finance domain knowledge + technical skills. Many companies value that combination.")
            
        elif "hello" in user_input or "hi" in user_input:
            print("Agent: Hello! How can I help you today?")
            
        else:
            print("Agent: I'm still learning. Try asking about resume, Python, or jobs.")

simple_agent()
