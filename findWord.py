dataset = "killy_dataset.txt"
word = "hell"

PREFIXES = ('(')
# NOTE: Check `...` before `.`.
SUFFIXES = (')', '?', '!', ',' , '...', '.', ':', '"')

def process_token(token):
    """Splits out prefixes and suffixes from the token."""
    # Split prefixes.
    prefixes = []
    is_clean = False
    while not is_clean:
        is_clean = True
        for prefix in PREFIXES:
            if token.startswith(prefix):
                is_clean = False
                prefixes.append(token[:len(prefix)])
                token = token[len(prefix):]

    # Split suffixes.
    suffixes = []
    is_clean = False
    for suffix in SUFFIXES:
        is_clean = True
        if token.endswith(suffix):
            is_clean = False
            suffixes.append(token[-len(suffix):])
            token = token[:-len(suffix)]
    return prefixes + [token] + suffixes

if __name__ == '__main__':
    g = input("Search for Killy word: ") 
    word = g
    with open(dataset) as file_:
        songs = file_.readlines()
    lines = []
    for song in songs:
        song = song.strip()
        title, author, lyrics = song.split('\t')
        #print(title, "\t\n", lyrics, "\n")
        for line in lyrics.split('\\'):
            line_tokens = line.split(' ')
            tokens = []
            for token in line_tokens:
                tokens.extend(process_token(token))
            for token in tokens:
                if word == token:
                    print(title, "\t", line)
