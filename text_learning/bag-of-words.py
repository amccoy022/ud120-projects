from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
email1 = "Hi Katie the self driving car will be late Best Sebastian"
email2 = "Hi Sebastian the machine learning class will be great great great Best Katie"
email3 = "Hi Katie the machine learning class will be most excellent"
email_list = [email1, email2, email3]
bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
print(bag_of_words)
#return what feature number great this is in bag of words
print (vectorizer.vocabulary_.get("great"))