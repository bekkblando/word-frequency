def word_frequency(text):
    re.sub(r'[^A-Za-z]\s', "", text).lower()
    
