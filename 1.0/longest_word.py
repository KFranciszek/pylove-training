def longest(tekst):
    chars = ['.',',',';',':','?','!','"',"'"]
    for chr in chars:
        tekst = tekst.replace(chr, '')
    tekst = tekst.split(' ')
    tekst.sort(key = len, reverse = True)
    counter = 0
    while len(tekst[counter]) == len(tekst[counter + 1]):
        counter += 1
    return tekst[0:(counter+1)]

print(longest('Ala ma kota a kot ma alibabę'))
print(longest('Ala ma kota a kot ma kota'))
print(longest('Vestibulum et ante aliquet, pharetra nulla vitae, dictum risus. Ut vitae nulla ultricies, vulputate dui a, venenatis massa. Aliquam aliquet enim ultricies maximus sollicitudin. Vivamus aliquam ex sit amet sem egestas sodales. Nunc sollicitudin arcu vel tempor imperdiet. In maximus, nulla venenatis luctus ornare, lectus sapien faucibus ipsum, interdum maximus lacus libero eleifend erat. Aliquam ut dui convallis, scelerisque massa sed, condimentum arcu. Suspendisse potenti. Nunc at fringilla diam. Vestibulum at fermentum diam. In nec pulvinar leo, nec sodales metus. Morbi tempus dictum orci eget hendrerit. Sed accumsan luctus mauris vel convallis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed egestas felis ipsum, gravida interdum nunc malesuada eu. Sed rhoncus sapien eu bibendum congue'))