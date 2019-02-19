MAT = [
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1]
]

def compute_determinant (m):
    if len(m[0]) > 2:
        det = 0
        for cell in m[0]:
            i = 0
            sub_m = []
            for j in range(1, len(m)):
                sub_m.append(m[i][:(j)] + m[i][(j+1):])
            det += (-1 if cell % 2 == 1 else 1) * cell * compute_determinant(sub_m)
            i += 1
        return det
    if len(m[0]) == 2:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    else:
        return m[0][0]

print(compute_determinant(MAT))