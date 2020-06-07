example_braille = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'
#                  000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110
example_string = 'The quick brown fox jumps over the lazy dog'

CHUNK_SIZE = 6

def get_chunks(braille_string):
    start, end = 0, 0
    for i in range(int(len(braille_string)/6)):
        end += CHUNK_SIZE
        yield braille_string[start:end]
        start = end

def get_braille_dict(in_string, in_braille):
    braille_dict = {}
    braille_dict.setdefault('capitalize', '000001')
    braille_dict.setdefault(' ', '000000')
    braille_chunks = [_ for _ in get_chunks(example_braille) if _ not in ['000001', '000000']]
    in_string = in_string.lower().replace(' ', '')
    braille_dict.update(dict(zip(list(in_string), braille_chunks)))
    return braille_dict

BRAILLE_DICT = get_braille_dict(example_string, example_braille)
    

def solution(s):
    # Your code here
    output_braille = ''
    for each_char in s:
        if ord('A') <= ord(each_char) <= ord('Z'):
            output_braille += BRAILLE_DICT['capitalize']
            each_char = chr(ord(each_char)+32)
        output_braille += BRAILLE_DICT[each_char]
    return output_braille

print(solution('The quick brown fox jumps over the lazy dog'))
