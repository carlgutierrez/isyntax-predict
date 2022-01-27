def removeNonAscii(text):
    encoded_string = text.encode("ascii", "ignore")
    return encoded_string.decode()


# remove multi-line comments
def removeMLComment(code):
    if code.find('/*') == -1:
        return code

    startIndex = code.find('/*')
    lastIndex = code.find('*/')
    # first line Comment
    if startIndex == 0:
        # recursion until no comment
        return removeMLComment(code[slice(lastIndex+2, len(code))])
    # last line comment
    if lastIndex == -1:
        # recursion until no comment
        return removeMLComment(code[slice(0, startIndex)])

    # In the middle comment
    # to remove middle comment and preserve other line of codes
    commentChunk = code[slice(startIndex+2, len(code))]
    lastIndex = commentChunk.find('*/')
    # recursion until no comment
    return removeMLComment(code[slice(0, startIndex)] + commentChunk[slice(lastIndex+2, len(commentChunk))])

# remove single-line


def removeLineComment(code):
    if code.find('//') == -1:
        return code
    startIndex = code.find('//')

    # In the middle comment
    # to remove middle comment and preserve other line of codes
    commentChunk = code[slice(startIndex+2, len(code))]
    lastIndex = commentChunk.find('\n')
    # recursion until no comment
    return removeLineComment(code[slice(0, startIndex)] + commentChunk[slice(lastIndex+1, len(commentChunk))])


def removeTabNewline(code):
    return code.replace('\t', ' ').replace('\\n', 'thisisauniqueword').replace('\n', ' ').replace('thisisauniqueword', '\\n')


def clean_code(code):
    code = [removeNonAscii(x) for x in code]
    code = [removeMLComment(removeLineComment(x)) for x in code]
    code = [removeTabNewline(x) for x in code]
    code = [x.strip() for x in code]
    code = [x for x in code if x]
    return code
