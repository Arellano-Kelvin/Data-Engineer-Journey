'''
string split and join
'''
def split_and_join(line):
    split_str = line.split()
    new_str ='-'.join(split_str)
    return new_str


'''
Mutations
'''
def mutate_string(string, position, character):
    s= string[:position]+character+string[position+1:]
    return s
