from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    input_text = ''
    sentiment = None
    emotion = None
    confidence = None
    scores = None
    gif_path = None  # Initialize as None, so no GIF is shown on GET request

    if request.method == 'POST':
        input_text = request.form['text'].lower()  # Convert to lowercase for easier keyword matching
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(input_text)

        # Determine sentiment based on compound score and additional rules
        compound = scores['compound']
        pos = scores['pos']
        neg = scores['neg']
        neu = scores['neu']

        # Primary classification based on compound score
        if compound > 0.15:
            sentiment = "Positive"
        elif compound < -0.15:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        # Secondary check: Use pos/neg scores to override
        if any(word in input_text for word in ["okay", "guess", "fine", "average", "alright"]):
            sentiment = "Neutral"
        elif neg > pos and neg > 0.3:
            sentiment = "Negative"
        elif pos > neg and pos > 0.3:
            sentiment = "Positive"

        # Emotion detection using keywords and sentiment
        if sentiment == "Positive":
            emotion = "Happy"
        elif sentiment == "Negative":
            emotion = "Sad"
        else:
            emotion = "Neutral"

        # Refine emotion with keyword-based detection
        if any(word in input_text for word in ["mad", "angry", "ruined", "horrible", "annoyed"]):
            emotion = "Angry"
        elif "frustrated" in input_text or "trying" in input_text:
            emotion = "Frustrated"
        elif any(word in input_text for word in ["thrilled", "amazing", "awesome", "best"]):
            emotion = "Happy"
        elif any(word in input_text for word in ["excited", "can’t wait", "fun"]):
            emotion = "Excited"
        elif any(word in input_text for word in ["upset", "sad", "lost", "awful"]):
            emotion = "Sad"
        elif "disappoint" in input_text:
            emotion = "Disappointed"
        elif any(word in input_text for word in ["can’t believe", "unexpected", "shocked", "surprised", "wow"]):
            emotion = "Surprised"
        elif any(word in input_text for word in ["don’t understand", "confused", "what does", "puzzled"]):
            emotion = "Confused"
        elif any(word in input_text for word in ["okay", "guess", "fine", "average", "alright"]) or (
            sentiment == "Neutral" and not any(
                word in input_text for word in [
                    "thrilled", "amazing", "awesome", "best",  # Happy
                    "excited", "can’t wait", "fun",  # Excited
                    "upset", "sad", "lost", "awful", "disappoint",  # Sad/Disappointed
                    "mad", "angry", "ruined", "horrible", "annoyed", "frustrated", "trying",  # Angry/Frustrated
                    "can’t believe", "unexpected", "shocked", "surprised", "wow",  # Surprised
                    "don’t understand", "confused", "what does", "puzzled"  # Confused
                ]
            )
        ):
            emotion = "Neutral"

        # Confidence (using compound score as a percentage)
        confidence = abs(compound) * 100  # Absolute value for display purposes

        # Map emotion to GIF
        print(f"Emotion before mapping: {emotion}")  # Debug
        gif_mapping = {
            "Happy": "cartoon-girl-happy.gif",
            "Sad": "cartoon-girl-sad.gif",
            "Angry": "cartoon-girl-angry.gif",
            "Surprised": "cartoon-girl-surprised.gif",
            "Confused": "cartoon-girl-confused.gif",
            "Neutral": "cartoon-girl-neutral.gif",
            "Frustrated": "cartoon-girl-angry.gif",
            "Excited": "cartoon-girl-happy.gif",
            "Disappointed": "cartoon-girl-sad.gif"
        }

        # Get the GIF path
        gif_filename = gif_mapping.get(emotion, "cartoon-girl-neutral.gif")  # Default to Neutral if emotion not found
        gif_path = f"static/{gif_filename}"

        # Debug print to log emotion and GIF path
        print(f"Detected Emotion: {emotion}, GIF Path: {gif_path}")

    return render_template('index.html', input_text=input_text, sentiment=sentiment, 
                         emotion=emotion, confidence=confidence, scores=scores, gif_path=gif_path)

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
