import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

def preprocess_text(text):
    stop_words = set(stopwords.words('german'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return " ".join(filtered_words)

processed_text = preprocess_text('./extracted_text.txt')
print(processed_text[:1000])