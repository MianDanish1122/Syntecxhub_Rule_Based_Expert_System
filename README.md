# Rule-Based Expert System

A Python implementation of a rule-based expert system with forward chaining inference.

## Features

- **Rule Engine**: If-then rules with conditions and conclusions
- **Facts Base**: Dynamic knowledge base for storing known facts
- **Forward Chaining**: Automatic inference from known facts to conclusions
- **Multi-step Inference**: Rules can chain together for complex reasoning
- **Inference Logging**: Complete reasoning path transparency
- **Interactive Interface**: User-friendly symptom input and diagnosis output

## Usage

Run the expert system:

```bash
python 01_task_rule_based_expert_system.py
```

Enter symptoms when prompted (one per line, empty line to finish):

```
fever
cough
fatigue
```

The system will perform inference and show:
- Initial symptoms
- Final conclusions/diagnosis
- Complete reasoning path

## Example Output

```
Initial symptoms: ['fever', 'cough', 'fatigue', 'chest_pain']

Final diagnosis/conclusions: {'pneumonia_risk', 'flu'}

=== REASONING PATH ===

Step 1: Rule 'Flu Diagnosis' fired
  Conditions met: {'fever', 'cough', 'fatigue'}
  New facts inferred: {'flu'}
  Total facts now: {'fever', 'flu', 'cough', 'chest_pain', 'fatigue'}

Step 2: Rule 'Pneumonia Risk' fired
  Conditions met: {'chest_pain', 'flu'}
  New facts inferred: {'pneumonia_risk'}
  Total facts now: {'fever', 'pneumonia_risk', 'flu', 'cough', 'chest_pain', 'fatigue'}
```

## Architecture

- `Rule` class: Represents individual if-then rules
- `ExpertSystem` class: Manages facts, rules, and inference process
- Forward chaining algorithm: Applies rules iteratively until no new conclusions

---

# Simple Rule-Based Chatbot

A conversational bot using pattern matching to handle intents and provide responses.

## Features

- **Intent Recognition**: Supports greeting, help, small talk, and goodbye intents
- **Pattern Matching**: Uses regex for flexible input matching
- **Knowledge Base**: Answers domain-specific questions about AI, Python, etc.
- **Interactive Console**: Real-time conversation via command line
- **Conversation Logging**: Saves all interactions to `conversation_log.txt`

## Usage

Run the chatbot:

```bash
python 02_task_simple_rule_based_chatbot.py
```

Start chatting! The bot recognizes:
- Greetings: "hello", "hi", "hey"
- Help requests: "help", "what can you do"
- Small talk: "how are you", "tell me a joke"
- Knowledge questions: "what is python", "what is ai"
- Goodbye: "bye", "exit"

## Example Interaction

```
Chatbot: Hello! I'm a simple rule-based chatbot. Type 'exit' to quit.
You: hello
Chatbot: Hi there!
You: what is python
Chatbot: Python is a high-level programming language known for its simplicity and readability.
You: tell me a joke
Chatbot: Why did the computer go to the doctor? Because it had a virus!
You: bye
Chatbot: Goodbye! Have a great day!
```

## Architecture

- `intents` dict: Maps intents to patterns and responses
- `knowledge_base` dict: Q&A pairs for domain knowledge
- Pattern matching with regex for intent detection
- Random response selection for variety
- File logging with timestamps

---

# Sentiment Analysis Tool

A machine learning tool for analyzing sentiment in text using TF-IDF features and Logistic Regression.

## Features

- **Text Preprocessing**: Cleans, tokenizes, and removes stopwords from text
- **Feature Extraction**: Converts text to numeric features using TF-IDF vectorization
- **Model Training**: Trains Logistic Regression classifier on labeled data
- **Evaluation**: Reports accuracy and F1-score on test data
- **Interactive CLI**: Allows real-time sentiment prediction for user input
- **Model Persistence**: Saves trained model for future use

## Usage

Run the sentiment analysis tool:

```bash
python 02_task_project_02_sentiment _analysis _tool.py
```

The tool will:
1. Train the model on sample data
2. Display evaluation metrics
3. Enter interactive mode for sentiment analysis

Enter text when prompted, or type 'quit' to exit.

## Example Output

```
Training sentiment analysis model...
Model Evaluation:
Accuracy: 0.80
F1 Score: 0.67
Model trained and saved.

Sentiment Analysis Tool
Enter text to analyze sentiment (type 'quit' to exit):
Text: I love this product!
Predicted sentiment: positive

Text: This is terrible.
Predicted sentiment: negative
```

## Architecture

- Sample dataset of positive/negative reviews
- NLTK for text preprocessing (tokenization, stopwords)
- Scikit-learn for TF-IDF vectorization and Logistic Regression
- Model saved as pickle file for reuse
- Command-line interface for predictions

## Requirements

- Python 3.x
- scikit-learn
- nltk

## License

MIT License

---

# Hand Gesture Recognition Demo

This script uses MediaPipe to detect hand landmarks in real-time from a webcam feed and classifies simple gestures: thumbs up, fist, and open palm. Each gesture is mapped to an action for demonstration purposes.

## Gestures and Actions
- **Thumbs Up**: Increase Volume
- **Fist**: Play/Pause
- **Open Palm**: Decrease Volume
- **Unknown**: No Action

## Requirements
- Python 3.7+
- Webcam
- opencv-python
- mediapipe

## Installation
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script:
```
python 03_task_hand_gesture_recognition.py
```

- A window will open showing the webcam feed with hand landmarks drawn.
- The detected gesture and corresponding action will be displayed on the screen.
- Press 'q' to quit.

## Troubleshooting
- If the webcam doesn't open, ensure it's not in use by another application.
- For better detection, ensure good lighting and keep your hand in view.
- If gestures are not detected accurately, adjust the `min_detection_confidence` parameter in the code.