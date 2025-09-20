import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
print("Environment loaded")

try:
    params = {"model":"gemini-2.5-flash","temperature":0.9}
    llm = ChatGoogleGenerativeAI(**params)
    template = PromptTemplate.from_template("Do a brief financial analysis of {company} based on its financial results in 3 sentences")
    output_parser = StrOutputParser()

    chain = template|llm|output_parser  # this is LCEL

    while True:
        company = input("Enter the company name(type exit to exit):")
        if company == "exit":
            break
        response = chain.invoke({"company":company})
        print(response)



except Exception as e:
    print(f"Some error occured:{e}")

