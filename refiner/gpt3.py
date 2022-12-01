import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_correction(text):
    prompt = f"Correct grammar and Suggest at-least three formal writing style for the text:\n\n {text} \n\n\nCorrect grammar:"
    response = openai.Completion.create(
        prompt=prompt,
        engine="text-davinci-003",
            temperature=0.5,
        max_tokens=250,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


'''
Correct grammar and Suggest at-least three formal writing style for the text:

their is so much vegetable to the market.

Correct grammar: There are so many vegetables at the market.

Formal Writing Styles: 
1. A plethora of vegetables can be found at the market.
2. An abundance of vegetables are available at the market. 
3. The market is stocked with a wide variety of vegetables.

'''