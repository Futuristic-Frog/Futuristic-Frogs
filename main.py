from textblob import TextBlob

def sentiment_analysis(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity == 0:
        return "Neutral"
    else:
        return "Negative"

user = input("What text do you want analyzed (or null to stop):");
while (user != ""):
  print(sentiment_analysis(user));
  user = input("What text do you want analyzed: ");
