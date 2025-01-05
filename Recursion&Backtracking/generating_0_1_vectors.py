def gen01(idx, vector):
    if idx >= len(vector):
        print("".join([str(x) for x in vector]))
        return
    for number in range(2):
        vector[idx] = number
        gen01(idx + 1, vector)


number_input = int(input())
vector = [0] * number_input
gen01(0, vector)
