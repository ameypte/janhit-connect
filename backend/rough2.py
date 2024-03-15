

import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    res = llm.invoke("Explain me ABout AI")
    print(res);
main()