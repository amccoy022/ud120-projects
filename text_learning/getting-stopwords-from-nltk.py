#import nltk
#nltk.download('all')


#from nltk.corpus import stopwords
#sw = stopwords.words("english")
#swlen = len(sw)
#print swlen

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stem1 = stemmer.stem("responsiveness")
print stem1
stem2 = stemmer.stem("unresponsive")
print stem2
