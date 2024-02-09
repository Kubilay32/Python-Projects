def pattern_search(P, I):
#theta == 0 or 180    
    for i in range(len(I) - len(P) + 1):
        for j in range(len(I[0]) - len(P[0]) + 1):
            if P[0] == I[i][j: j + len(P[0])]:
                a = 1
                b = i + 1
                for __ in range(len(P) - 1):
                    if P[a] == I[b][j: j + len(P[0])]:
                        a += 1
                        b += 1
                if a == len(P):
                    return i, j, 0

            elif P[-1][::-1] == I[i][j: j + len(P[0])]:
                c = -2
                d = i + 1
                for _ in range(len(P) - 1):
                    if P[c][::-1] == I[d][j: j + len(P[0])]:
                        c -= 1
                        d += 1
                if c == -1 - len(P):
                    return i, j, 180

    def pattern_270(P):
        global x
        x = []
        _270_pattern = ""
        if len(P) % 2 == 0:
            for _a in range(-1, -len(P[0]) - 1, -1):
                for _b in range(1, len(P), 2):
                    _270_pattern = _270_pattern + P[_b - 1][_a] + P[_b][_a]
                    if len(P) == len(_270_pattern):
                        x.append(_270_pattern)
                        _270_pattern = ""

        elif len(P) % 2 == 1:
            for _A in range(-1, -len(P[0]) - 1, -1):
                for _B in range(0, len(P)):
                    _270_pattern = _270_pattern + P[_B][_A]
                    if len(P) == len(_270_pattern):
                        x.append(_270_pattern)
                        _270_pattern = ""
        return x
        
    def pattern_90(P):
        global y
        y = []
        _90_pattern = ""
        if len(P) % 2 == 0:
            for _c in range(0, len(P[0])):
                for _d in range(1, len(P), 2):
                    _90_pattern = P[_d][_c] + P[_d - 1][_c] +_90_pattern
                    if len(P) == len(_90_pattern):
                        y.append(_90_pattern)
                        _90_pattern = ""
        elif len(P) % 2 == 1:
            for _C in range(0, len(P[0])):
                for _D in range(0, len(P)):
                    _90_pattern = P[_D][_C] + _90_pattern
                    if len(P) == len(_90_pattern):
                        y.append(_90_pattern)
                        _90_pattern = ""
        return y


#theta == 90 or 270
    for k in range(len(I) - len(P[0]) + 1):
        for l in range(len(I[0]) - len(P) + 1):
            if pattern_270(P)[0] == I[k][l: l + len(P)]:
                e = 1
                f = k + 1
                for ___ in range(len(P[0]) - 1):
                    if pattern_270(P)[e] == I[f][l: l + len(P)]:
                        e += 1
                        f += 1
                if e == len(P[0]):
                    return k, l, 270

            elif pattern_90(P)[0] == I[k][l: l + len(P)]:
                h = 1
                j = k + 1
                for ____ in range(len(P[0]) - 1):
                    if pattern_90(P)[h] == I[j][l: l + len(P)]:
                        h += 1
                        j += 1
                if h == len(P[0]):
                    return k, l, 90
    else: return False
