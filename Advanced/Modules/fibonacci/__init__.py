def create(length):
    fibonacci=[0,1]
    if length==0:
        fibonacci=[]
    else:
        for i in range(length-2):
            fibonacci.append(fibonacci[-1]+fibonacci[-2])
    return fibonacci


def locate(num,sequence):
    if num in sequence:
        for idx in range(len(sequence)):
            if sequence[idx]==num:
                return f"The number - {num} is at index {idx}"

    else:
        return f"The number - {num} is not in the sequence"
