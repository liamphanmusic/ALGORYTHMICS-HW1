
'''
a function that reads a reference text file that has one sentence per line
and creates a list of sentences where each sentence is a list of lowercase strings (the words)
'''




def read_reference_text(filename: str) -> list[list[str]]:

    a_file = open(filename, "r")
    list_of_lists = [(line.strip()).split() for line in a_file]
    a_file.close()
    print(list_of_lists)

read_reference_text("ref-sentences.txt")


