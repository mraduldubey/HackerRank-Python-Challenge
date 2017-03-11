def mutate_string(string, position, character):
    lstr=list(string)
    lstr[position]=character
    return ''.join(lstr)