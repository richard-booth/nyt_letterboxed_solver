from collections import defaultdict
#letters input
top = ['h','t','u']
left = ['i','s','w']
right = ['b','r','o']
bottom = ['q','d','e']
admissible_letters = top + left + right + bottom

def build_dict():
    words = []
    with open('mit_10k.txt') as dict_file:
        for word in dict_file:
            word = word.strip()
            if len(word) >=3:
                for i in range(len(word)):
                    if word[i] in admissible_letters:
                        continue
                    else:
                        break
                else:
                    words.append(word)
    return words

def get_admissible_words(words):
    admissible_words = []
    words_by_letter = defaultdict(list)
    for word in words:
        current_letters = top + left + right + bottom
        for i in range(len(word)):
            if word[i] not in current_letters:
                break
            else:
                if word[i] in top:
                    current_letters = left + right + bottom
                elif word[i] in left:
                    current_letters = top + right + bottom
                elif word[i] in right:
                    current_letters = top + left + bottom
                else:
                    current_letters = top + left + right
        else:
            admissible_words.append(word)
            words_by_letter[word[0]].append(word)
    return admissible_words, words_by_letter

words = build_dict()

admissible_words, words_by_letter = get_admissible_words(words)

def get_sequences(admissible_words):
    pairs = []
    triples=[]
    for first in admissible_words:
        last_letter = first[-1]
        for second in words_by_letter[last_letter]:
            pairs.append([first, second])
    for pair in pairs:
        last_letter = pair[1][-1]
        for third in words_by_letter[last_letter]:
            triples.append(pair+[third])
    return pairs, triples
        

pairs, triples = get_sequences(admissible_words)

print('pairs:', len(pairs))
print('triples:', len(triples))

def max_pair(pairs):
    max_rank = 0
    max_pair = pairs[0]
    for pair in pairs:
        pair_str = "".join(pair)
        rank = len(set(pair_str))
        if rank > max_rank:
            max_rank = rank
            max_pair = pair
    return max_rank, max_pair
def max_triple(triples):
    max_rank = 0
    max_tri = triples[0]
    for tri in triples:
        tri_str = "".join(tri)
        rank = len(set(tri_str))
        if rank > max_rank:
            max_rank = rank
            max_tri = tri
    return max_rank, max_tri

print(max_pair(pairs))
print(max_triple(triples))