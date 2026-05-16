import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

questions = [
    "What is AI",
    "What is Python",
    "What is machine learning",
    "Who developed Python",
    "What is C",
    "Is C a language"
]

answers = [
    "AI means Artificial Intelligence",
    "Python is a programming language",
    "Machine learning is a part of AI",
    "Python was developed by Guido van Rossum",
    "C is a programming language",
    "Yes, C is a programming language"
]

def chatbot():
    while True:
        user = input("You: ")

        if user.lower() == "exit":
            print("Bot: Goodbye!")
            break

        all_text = questions + [user]

        vectorizer = CountVectorizer().fit_transform(all_text)

        similarity = cosine_similarity(vectorizer[-1], vectorizer[:-1])

        score = similarity.max()

        index = similarity.argmax()

        if score < 0.3:
            print("Bot: Sorry, I don't understand.")
        else:
            print("Bot:", answers[index])

chatbot()