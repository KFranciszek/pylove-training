def odwazniki(a,b):
    ab = a * b
    aa = a
    bb = b
    while bb != 0 :
        cc = bb
        bb = aa % bb
        aa = cc
    ab = ab / aa
    return (int(ab/a),int(ab/b))


print(odwazniki(2, 8))
# 4, 1
print(odwazniki(4, 6))
# 3, 2
print(odwazniki(6, 4))