import os 
from dotenv import load_dotenv
load_dotenv(dotenv_path="../../env/.env")
open_ai_api_key = os.getenv("OPENAI_API_KEY")

from litellm import completion
from typing import List, Dict

def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content

def main():
    # First Prompt:
    #     Ask the user what function they want to create
    #     Ask the LLM to write a basic Python function based on the user’s description
    #     Store the response for use in subsequent prompts
    #     Parse the response to separate the code from the commentary by the LLM

    function_description = input("Describe a python function that you want to create: \n")
    messages = [
        {"role": "system", "content": "You are an expert software engineer that prefers functional programming."},
        {"role": "user", "content": "Write a python function which does the following:"},
        {"role": "user", "content": function_description}
    ]

    response = generate_response(messages)
    print(response)
    
    # Second Prompt:
    #     Pass the code generated from the first prompt
    #     Ask the LLM to add comprehensive documentation including:
    #         Function description
    #         Parameter descriptions
    #         Return value description
    #         Example usage
    #         Edge cases
    
    input("\n Press enter once you are ready to get documentation \n")
    
    messages.append({"role": "assistant", "content": response})
    messages.append({"role": "user", "content": "Update the function to include documentation. Include all of the following: Function description, Parameter Description, Return value description, Example usage, Edge cases" })

    response = generate_response(messages)
    print(response)

    # Third Prompt:

    #     Pass the documented code generated from the second prompt
    #     Ask the LLM to add test cases using Python’s unittest framework
    #     Tests should cover:
    #         Basic functionality
    #         Edge cases
    #         Error cases
    #         Various input scenarios

    input("\n Press enter once you are ready to get test cases \n")

    messages.append({"role": "assistant", "content": response})
    messages.append({"role": "user", "content": "Add test cases with pythons unit test framework. Include all of the following: basic functionality, edge cases, error cases, various input scenarios" })

    response = generate_response(messages)
    print(response)
    
main()