import subprocess
import openai

def run_tests():
    result = subprocess.run(["pytest", "-v"], capture_output=True, text=True)
    return result.stdout

def explain_with_ai(test_output):
    # later we’ll add OpenAI key, for now just mock response
    return f"AI Suggestion: Based on output -> {test_output[:200]}..."

if __name__ == "__main__":
    output = run_tests()
    print("==== PYTEST RAW OUTPUT ====")
    print(output)
    ai_response = explain_with_ai(output)
    print("==== AI DEBUGGING TIP ====")
    print(ai_response)
