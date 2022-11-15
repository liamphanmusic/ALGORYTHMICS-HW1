import re
import math

# INPUTS ----------------------------------------------------------

# Your Stopwords
stopwords = set(["s", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"])

# Your Words List
word_list = ["canada", "disaster", "flood", "car", "road", "train", "rail", "germany", "switzerland", "technology", "industry", "conflict"]

# ALL FUNCTIONS REQUIRED ------------------------------------------
def read_reference_text(filename: str) -> list[list[str]]:
    f = open(filename)
    line = f.readlines()
    line = [re.split("[ ,;:\’\"\?!]+", l) for l in line]
    line = [line[:-1] for line in line]
    line = [[line.lower() for line in line] for line in line]
    line = [[i for i in line if i not in stopwords] for line in line]
    line = [list(filter(lambda word: len(word) >=3, line)) for line in line]
    f.close()
    return line

txt = read_reference_text("ref-sentences.txt")

def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    # create dictionary
    dict = {}
    # looping for reaching out each individual sentences and words inside it
    for sentence in txt:
        if w in sentence:
            # remove the word w in the list
            sentence.pop(sentence.index(w))
            # no duplicates
            temporary = set(sentence)
            # looping for adding the found words in the sentence in our dictionary
            for word in temporary:
                if word in dict.keys():
                    # adding +1 if the word already exists
                    dict[word] = dict[word] + 1
                else:
                    # adding 1 if the word doesn't exist
                    dict[word] = 1
    return dict


def product(v1: dict[str, int], v2: dict[str, int]) -> float:
    sp = 0.0
    for word in v1:
        sp += v1[word] * v2.get(word,0)
    return sp


def similarity(s1: str, s2: str) -> float:
    d1 = make_word_vector(s1,txt)
    d2 = make_word_vector(s2,txt)
    return product(d1, d2)/(math.sqrt(product(d1, d1)*product(d2, d2)))


print(similarity("canada","car"))


