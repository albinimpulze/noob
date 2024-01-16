import google.generativeai as genai

def generate(prompt):
    genai.configure(api_key='AIzaSyAXnyrglajaWgDXsHCBFZEF40YZ9ICa74c')
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text


generate("write me a song")