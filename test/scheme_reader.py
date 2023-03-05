from Pair import Pair

def is_space(char):
    """whether char is a space."""
    return char == ' ' or char == '\n'

def is_parentheses(char):
    """Whether char is a parentheses."""
    return (char == '(') or (char == ')')

def is_symbol(char):
    """Whether a char is a char of symbol."""
    return not (is_space(char) or is_parentheses(char))

def line_split(line):
    """Split line to a list contained all tokens."""
    is_word = False
    bi = 0
    index = 0
    tokens = []
    while index < len(line):
        if is_word:
            if not is_symbol(line[index]):
                tokens.append(line[bi:index])
                is_word = False
                if is_parentheses(line[index]):
                    tokens.append(line[index])
        else:
            if is_symbol(line[index]):
                bi = index
                is_word = True
            elif is_parentheses(line[index]):
                tokens.append(line[index])
    

        # if is_word == False and is_symbol(line[index]):
        #     bi = index
        #     is_word = True
        # elif is_word and (not is_symbol(line[index])):
        #     tokens.append(line[bi:index]) 
        #     is_word = False
            
        # if is_parentheses(line[index]):
        #     tokens.append(line[index])
        index += 1
    return tokens
            
        
