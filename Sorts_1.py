import random
def selection_sort(listo):

    for k in range(len(listo)):
        mino = listo[k]
        did_swap = False
        for v in range(k, len(listo)):
            if listo[v] < mino:
                mino = listo[v]
                swapindex = v
                did_swap = True
        if did_swap:
            tmp = listo[k]
            listo[k] = mino
            listo[swapindex] = tmp
    return listo

def inserto(listo, new_element):

    longo = len(listo)
    to_the_right = False

    for v in range(longo):
        pointer = longo - 1 - v
        if listo[pointer] < new_element:
            listo = listo[:pointer + 1] + [new_element] + listo[pointer + 1:]
            to_the_right = True
            break
    
    if not to_the_right:
        listo = [new_element] + listo

    return listo

def insertion_sort(listo):

    left_array = [listo[0]]

    for v in range(1, len(listo)):
        left_array = inserto(left_array, listo[v])
    
    return left_array

input_list = list(range(100))
random.shuffle(input_list)
print(input_list)
print()
print(insertion_sort(input_list))


