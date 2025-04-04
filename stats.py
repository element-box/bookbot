
def get_word_count(text: str) -> None:
    num_words = 0
    num_words = text.split()
    print(f"Found {len(num_words)} total words")

def get_char_count(text: str) -> dict:
    char_count: dict = {}
    text = text.lower()
    for t in range(len(text)):
        if text[t] not in char_count:
            char_count[text[t]] = 1
        else:
            char_count[text[t]] += 1
    return char_count

def sort_on(dict):
    return dict["count"]

def get_stats(char_count: dict):
    char_list: list[dict] = []
    for x in char_count:
        count = char_count[x]
        char_list.append({"letter" :x, "count": count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list