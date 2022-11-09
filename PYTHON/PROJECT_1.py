import re

def read_reference_text(filename: str) -> list[list[str]]:
    f = open(filename)
    line = f.readlines()
    line = [re.split("[ ,;:\’\"\?!.]+", l) for l in line]
    line = [line[:-1] for line in line]
    line = [[line.lower() for line in line] for line in line]
    f.close()
    return line


def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:


w = ["spain", "anchovy","france", "internet", "china", "mexico", "fish", "industry", "agriculture", "fishery", "tuna", "transport", "italy", "web", "communication", "labour", "fish", "cod"]
txt = read_reference_text("ref-sentences.txt")

print(make_word_vector(w,txt))

