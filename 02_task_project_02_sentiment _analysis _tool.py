import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import pickle

# Download NLTK data if not present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Sample labeled data (tweets/reviews)
data = [
    ("I love this product! It's amazing.", "positive"),
    ("This is the best movie I've ever seen.", "positive"),
    ("Great customer service, very helpful.", "positive"),
    ("The food was delicious and fresh.", "positive"),
    ("I had a wonderful experience.", "positive"),
    ("This product is terrible, don't buy it.", "negative"),
    ("Worst movie ever, complete waste of time.", "negative"),
    ("Customer service was rude and unhelpful.", "negative"),
    ("The food was cold and tasteless.", "negative"),
    ("I regret purchasing this item.", "negative"),
    ("The weather is beautiful today.", "positive"),
    ("I'm so happy with my new phone.", "positive"),
    ("This book is fantastic.", "positive"),
    ("The concert was incredible.", "positive"),
    ("I enjoy spending time with friends.", "positive"),
    ("This is awful, I hate it.", "negative"),
    ("The service was disappointing.", "negative"),
    ("I feel sad about this situation.", "negative"),
    ("The product broke after one day.", "negative"),
    ("I'm frustrated with this company.", "negative"),
]

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Join back to string
    return ' '.join(tokens)

def train_model():
    # Prepare data
    texts = [preprocess_text(text) for text, label in data]
    labels = [label for text, label in data]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    # Feature extraction using CountVectorizer
    vectorizer = CountVectorizer(max_features=1000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train classifier (Naive Bayes)
    classifier = MultinomialNB()
    classifier.fit(X_train_vec, y_train)

    # Evaluate
    y_pred = classifier.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, pos_label='positive')

    print(f"Model Evaluation:")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"F1 Score: {f1:.2f}")

    # Save model and vectorizer
    with open('sentiment_model.pkl', 'wb') as f:
        pickle.dump((vectorizer, classifier), f)

    return vectorizer, classifier

def predict_sentiment(text, vectorizer, classifier):
    processed_text = preprocess_text(text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = classifier.predict(vectorized_text)[0]
    return prediction

def main():
    print("Training sentiment analysis model...")
    vectorizer, classifier = train_model()
    print("Model trained and saved.\n")

    print("Sentiment Analysis Tool")
    print("Enter text to analyze sentiment (type 'quit' to exit):")

    while True:
        user_input = input("Text: ").strip()
        if user_input.lower() == 'quit':
            break
        if not user_input:
            continue

        sentiment = predict_sentiment(user_input, vectorizer, classifier)
        print(f"Predicted sentiment: {sentiment}\n")

if __name__ == "__main__":
    main()