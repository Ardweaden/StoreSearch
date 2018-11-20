import sys

sys.path.append("C:/Users/dis/Documents/JanJezersek/EkoSmart/pylemmagen")

from lemmagen.lemmatizer import Lemmatizer

a = Lemmatizer()

sys.stdout.write(a.lemmatize(sys.argv[1]))