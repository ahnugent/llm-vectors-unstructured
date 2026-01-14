from textblob import TextBlob

phrase = "You can extract topics from phrases using TextBlob"

topics = TextBlob(phrase).noun_phrases

print(topics)

"""
You may find changing the default Noun Phrase Chunker used by TextBlob improves results for your data.
"""