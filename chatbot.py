import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def chatbot_response(preprocessed_text, user_query):
    # Truncate preprocessed_text if it's too long
    max_length = 800  # Example maximum length, adjust as needed
    if len(preprocessed_text) > max_length:
        preprocessed_text = preprocessed_text[:max_length] + "..."

    prompt = f"""
    You are a helpful assistant. The following is the content of a PDF document:

    {preprocessed_text}

    Based on the above, answer the user's question: "{user_query}"
    """
    
    # Encode the prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate a response
    try:
        outputs = model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract the relevant part of the response
        response_start_index = len(prompt)
        if response_start_index < len(response):
            return response[response_start_index:].strip()
        else:
            return "No response generated."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
with open('./extracted_text.txt', 'r', encoding='utf-8') as file:
    preprocessed_text = file.read()

user_query = "What is the main topic of this document?"
response = chatbot_response(preprocessed_text, user_query)-
print(response)