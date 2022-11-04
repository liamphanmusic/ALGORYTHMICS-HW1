import re

def read_reference_text(filename: str) -> list[list[str]]:
    f = open(filename)
    line = f.readlines()
    line = [re.split("[ ,;:\’\"\?!.]+", l) for l in line]
    line = [line[:-1] for line in line]
    return line
    f.close()

print(read_reference_text("ref-sentences.txt"))

def make_word_vector(w: str, txt: list[list[str]]) -> dict[str, int]:
    






def sim_word_vec(v1: dict[str, int], v2: dict[str, int]) -> float:


