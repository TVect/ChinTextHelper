import Levenshtein

word2strokes = {}
with open("./resources/chinese_strokes.txt") as fr:
    for line in fr:
        line_striped = line.strip()
        if line_striped:
            word, strokes = line_striped.split()
            word2strokes[word] = strokes


def word_strokes_similarity(word1, word2):
    # Compute absolute Levenshtein distance of two strings.
    form1 = word2strokes.get(word1, "")
    form2 = word2strokes.get(word2, "")
    return 1 - Levenshtein.distance(form1, form2) / max(len(form1), len(form2))


if __name__ == "__main__":
    print(word_strokes_similarity(word1="徽", word2="微"))
