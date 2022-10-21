import _pickle as cPickle
with open(r"mytrace.pickle", "rb") as input_file:
    e = cPickle.load(input_file)
x = e