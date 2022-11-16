import re
import math
import copy

stopwords = set(["s", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"])


def read_reference_text(filename: str) -> list[list[str]]:
    f = open(filename)
    content = f.readlines()
    content = [line.rstrip() for line in content]
    content = [re.split("[ .,;:\’\"\?!]+", l) for l in content]
    for line in content:
        while ("" in line):
            line.remove("")
    content = [[content.lower() for content in content] for content in content]
    content = [list(filter(lambda word: len(word) >= 3, content)) for content in content]
    content = [[i for i in content if i not in stopwords] for content in content]
    content = [i for i in content if i != []]
    f.close()
    return content


content = read_reference_text("ref-sentences.txt")


def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    dicti = {}
    txt_deep_copy = copy.deepcopy(txt)
    for line in txt_deep_copy:
        if w in line:
            # remove the word w in the list
            line.pop(line.index(w))
            # no duplicates
            tempset = set(line)
            # looping for adding the found words in the sentence in our dictionary
            for word in tempset:
                if word in dicti.keys():
                    # adding +1 if the word already exists
                    dicti[word] = dicti[word] + 1
                else:
                    # adding 1 if the word doesn't exist
                    dicti[word] = 1
    return dicti


def product(v1: dict[str, int], v2: dict[str, int]) -> float:
    sp = 0.0
    for word in v1:
        sp += v1[word] * v2.get(word,0)
    return sp


def similarity(s1: str, s2: str) -> float:
    d1 = make_word_vector(s1,read_reference_text("ref-sentences.txt"))
    d2 = make_word_vector(s2,read_reference_text("ref-sentences.txt"))
    return product(d1, d2)/(math.sqrt(product(d1, d1)*product(d2, d2)))


def main():
