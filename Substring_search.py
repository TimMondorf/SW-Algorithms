text = (8 * 'timmondo') + 'timmondorf' + (8 * 'timmondo')
pattern = 'timmondorf'
print(text.index(pattern))
print(text.index(pattern) + len(pattern))

def Brute(text, pattern):
    long_text = len(text)
    long_pat = len(pattern)
    pattern_found = False
    i = 0
    while i < long_text - long_pat:
        slico = text[i: i + long_pat]
        for j in range(long_pat):
            if not slico[j] == pattern[j]:
                break
        if slico == pattern:
            pattern_found = True
            break
        i += 1
    if pattern_found:
        print('Brute found pattern from index ' + str(i) + ' to index ' + str(i + len(slico)) )
        print(slico)
    else:
        print('Brute did not find pattern')

Brute(text, pattern)

def KMP(text, pattern):
    long_text = len(text)
    long_pat = len(pattern)
    slico = ''
    pattern_found = False
    i = 0
    while i < long_text - long_pat:
        slico += text[i]
        if not slico == pattern[:len(slico) ]:
            slico = ''
        if slico == pattern:
            pattern_found = True
            break
        i += 1
    if pattern_found:
        print( 'KMP found pattern from index ' + str(i - len(slico)) + ' to index ' + str(i) ) 
        print(slico)
    else:
        print('KMP did not find pattern')

KMP(text, pattern)

def Rabin_Karp(text, pattern):
    hash_value = hash(pattern)
    long_text = len(text)
    long_pat = len(pattern)
    i = 0
    pattern_found = False
    while i < long_text - long_pat:
        slico = text[i:i + long_pat]
        if hash(slico) == hash_value:
            pattern_found = True
            break
        i += 1
    if pattern_found:
        print('Rabin-Karp found pattern from index ' + str(i) + ' to index ' + str(i + len(slico)) )
        print(slico)
    else:
        print('Rabin-Karp did not find pattern')

Rabin_Karp(text, pattern)