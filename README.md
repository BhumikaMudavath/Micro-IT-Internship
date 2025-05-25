# Micro-IT-Internship
## Sentiment Analysis Tool
### Overview
This project is a web-based Sentiment Analysis Tool built using Flask, VADER Sentiment Analysis, Bootstrap, and Chart.js. It analyzes user input text to detect sentiment (Positive, Negative, Neutral) and emotion (Happy, Excited, Sad, Disappointed, Angry, Frustrated, Surprised, Confused, Neutral). The tool displays the results with a corresponding animated GIF of a cartoon girl expressing the detected emotion.
### Features
**Sentiment Detection:** Classifies text as Positive, Negative, or Neutral using VADER's compound score and keyword-based overrides.<br>
__Emotion Detection:__ Identifies emotions like Happy, Sad, Angry, etc., using sentiment and keyword-based rules.<br>
__Visual Feedback:__ Displays a bar chart of sentiment scores (Positive, Negative, Neutral) using Chart.js.<br>
__Animated GIFs:__ Shows a cartoon girl GIF that matches the detected emotion.<br>
__Responsive UI:__ Styled with Bootstrap and custom CSS for a user-friendly interface.<br>
### Project Structure
Sentiment-Analysis-Tool/<br>
├── app.py<br>
├── templates/<br>
│   └── index.html<br>
├── static/<br>
│   ├── cartoon-girl-happy.gif<br>
│   ├── cartoon-girl-sad.gif<br>
│   ├── cartoon-girl-angry.gif<br>
│   ├── cartoon-girl-surprised.gif<br>
│   ├── cartoon-girl-confused.gif<br>
│   ├── cartoon-girl-neutral.gif<br>
│   └── background.jpg<br>
├── requirements.txt<br>
└── README.md<br>
### Deployment
Access the app here](https://sentimental-analysis-tool-w9pj.onrender.com).
