import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()
print("Environment variables loaded.")

# Check if the Google API key is available
if os.getenv("GOOGLE_API_KEY"):
    print("Google API Key found.")
else:
    print("Google API Key not found. Please check your .env file.")
    exit()

try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    print("Google Gemini (gemini-pro) model initialized.")

    prompt = "Hello! In one sentence explain what is RAG?"

    print("\nInvoking model...")
    response = llm.invoke(prompt)
    print("Model invocation successful.")

    print("\n--- Response from Gemini ---")
    print(response.content)
    print("----------------------------\n")
    print("Your environment is set up and working correctly with Google Gemini!")

except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check your API key, internet connection, and Google Cloud project status.")