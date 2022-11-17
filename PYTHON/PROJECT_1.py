
# IMPORT PACKAGES --------------------------------------------------
import re
import math
import copy

# ALL FUNCTIONS REQUIRED ------------------------------------------
def read_reference_text(filename: str, stopwords: list[str]) -> list[list[str]]:
    """
    :param filename: Our Filename or direction if not in the root folder
    :return: a list of list of string with each word split in sentences
    """
    f = open(filename)
    line = f.readlines()
    line = [re.split("[ ,;:\’\"\?!]+", l) for l in line]
    line = [line[:-1] for line in line]
    line = [[line.lower() for line in line] for line in line]
    line = [[i for i in line if i not in stopwords] for line in line]
    line = [list(filter(lambda word: len(word) >=3, line)) for line in line]
    f.close()
    return line


def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    """
    :param w: the word we want to compute vector
    :param txt: the reference text (ref-sentences.txt)
    :return: a dictionary providing all words frequency found in the same context as w (the word)
    """
    dict = {}
    for sentence in txt:
        if w in sentence:
            sentence_1 = copy.copy(sentence)
            sentence_1.pop(sentence_1.index(w))
            temporary = set(sentence_1)
            for word in temporary:
                if word in dict.keys():
                    dict[word] = dict[word] + 1
                else:
                    dict[word] = 1
    return dict


def product(v1: dict[str, int], v2: dict[str, int]) -> float:
    """
    :param v1: The First Word Dictionary
    :param v2: The Second Word Dictionary
    :return: Product of the both Dictionary
    """
    sp = 0.0
    for word in v1:
        sp += v1[word] * v2.get(word,0)
    return sp


def similarity(s1: str, s2: str, reference_text: list[list[str]]) -> float:
    """
    :param s1: The Word 1 as string
    :param s2: The Word 2 as string
    :param reference_text: Use the split Reference Text (List of List of String)
    :return: Similarity between both Words in range 0 and 1 (as float)
    """
    d1 = make_word_vector(s1,reference_text)
    d2 = make_word_vector(s2,reference_text)
    return product(d1, d2)/(math.sqrt(product(d1, d1)*product(d2, d2)))


# MAIN FUNCTION -------------------------------------------------------------

def main(word_list:list[str], stopwords:list[str], reference_text: str):
    """
    :param word_list: The Full List of Words we want to compare similarity
    :return: printing the result for the Full List of Words, only the maximum similarity combination
    """

    reference = read_reference_text(reference_text,stopwords)

    for i in range(len(word_list)):
        max_sim = 0
        for j in range(len(word_list)):
            if j == i:
                continue
            else:
                sim = similarity(word_list[i], word_list[j], reference)
                if sim>max_sim:
                    max_sim=sim
                    j_pos = j
        print(f'{word_list[i]} --> {word_list[j_pos]}, {max_sim}')


# INPUTS -------------------------------------------------------------------

# Stopword Set
stopwords = set(["s", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"])

# First List for the Sample Output
word_list_1 = ["canada", "disaster", "flood", "car", "road", "train", "rail", "germany", "switzerland", "technology", "industry", "conflict"]

# Second List for the To Do Output
word_list_2 = ["spain", "anchovy","france", "internet", "china", "mexico", "fish", "industry", "agriculture", "fishery", "tuna", "transport", "italy", "web", "communication", "labour", "fish", "cod"]

# COMPUTATIONS --------------------------------------------------------------

# Use word_list_1 for Sample output or word_list_2 for To Do output
main(word_list_1, stopwords, "ref-sentences.txt")

