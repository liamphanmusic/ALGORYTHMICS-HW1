import re

def read_reference_text(filename: str) -> list[list[str]]:
    f = open(filename)
    line = f.readlines()
    line = [re.split("[ ,;:\’\"\?!.']+", l) for l in line]
    line = [line[:-1] for line in line]
    line = [[line.lower() for line in line] for line in line]
    f.close()
    return line


def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    dict = {}
    for sentence in txt:
        if w in sentence:
            sentence.pop(sentence.index(w))
            temporary = set(sentence)
            for word in temporary:
                if word in dict.keys():
                    dict[word] = dict[word] + 1
                else:
                    dict[word] = 1
    return dict

w = ["spain", "anchovy","france", "internet", "china", "mexico", "fish", "industry", "agriculture", "fishery", "tuna", "transport", "italy", "web", "communication", "labour", "fish", "cod"]

txt = read_reference_text("ref-sentences.txt")
dict = make_word_vector(w,txt)
print(dict)








