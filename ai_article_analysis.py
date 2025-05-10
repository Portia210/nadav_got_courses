import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def analyze_article(article, add_to_prompt=None):
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    
   
    # Create the prompt for OpenAI
    prompt = f"""you are going to get a an ariticle name and body, act according to the prompt:\nprompt: {add_to_prompt}\n{article}"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Always Return the Response in english in markdown format. Be Pragmatic."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        
        # Get the response content
        response_content = response.choices[0].message.content.strip()
        

        if response_content.startswith("```"):
            response_content = response_content.replace("```", "", 1)
        if response_content.endswith("```"):
            response_content = response_content.rsplit("```", 1)[0]
        
        # Strip any remaining whitespace
        response_content = response_content.strip()
        
        # Check if the response is empty
        if not response_content:
            print("Error: Empty response from OpenAI API")
            return None

        return response_content

    except Exception as e:
        print(f"Error with the proccessing: {str(e)}")
        return None
