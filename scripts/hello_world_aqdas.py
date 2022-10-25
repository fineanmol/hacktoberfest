from string import ascii_letters as l, whitespace as w, punctuation as p
l += w[0]+p[0]
for i in (33, 4, 11, 11, 14, 52, 48, 14, 17, 11, 3, 53):
    print(l[i], end='')
