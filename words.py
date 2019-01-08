from datamuse import datamuse
dm = datamuse.Datamuse()

# takes the results from a 
# dm query and converts to list of words
def apiToList(results, count = 1000):
    syns = []
    for i in range (min(count, len(results))):
        potentialSyn = results[i]['word']
        if (potentialSyn.find(' ') == -1):
            syns.append(potentialSyn)
    return syns

# takes a word and returns all possible words
# (using datamuse) that are related to it
def totalWords(word):
    totalWords = []
    # same meaning
    totalWords += apiToList(dm.words(ml = word))
    # sounds like
    totalWords += apiToList(dm.words(sl = word), 20)
    # spelled like
    totalWords += apiToList(dm.words(sp = word), 20)
    # often used to describe
    totalWords += apiToList(dm.words(rel_jjb = word), 20)
    # triggerd by
    totalWords += apiToList(dm.words(rel_trg = word))
    # rhymes with
    totalWords += apiToList(dm.words(rel_rhy = word), 10)
    # removing duplicates
    totalWords = set(totalWords)
    return totalWords


def wordsInCommon(word1, word2):
    w1Set = totalWords(word1)
    w2Set = totalWords(word2)
    return (list(w1Set.intersection(w2Set)))

