def longest_word(tekst):
    longest = []
    tekst = tekst.replace(',','')
    tekst = tekst.replace('.', '')
    tekst = tekst.replace('?', '')
    tekst = tekst.replace('!', '')
    tekst = tekst.replace('#', '')

    lista = tekst.split()
    lista.sort()
    lista.sort(key=len)
    longest.append(lista[-1])
    while not len(lista[-1]) > len(lista[-2]):
        longest.append(lista[-2])
        lista.pop()
    if len(longest) == 1:
        return longest[0]
    else:
        return longest[::-1]


print(longest_word('ghkj jfhf jshdhdgd b aaaaaaaaaaaaaaaaaaaaaaaaaaaa bnbnbhgfjgn nfjdjdshsb nghgjgkdnd'))
print(longest_word('a b c d eeee ffff g h i j k l aaaa'))
print(longest_word('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed venenatis turpis ac eros consequat '
                   'aliquet. In sollicitudin elementum convallis. Vivamus feugiat mollis vehicula. Ut sodales orci '
                   'quis ornare faucibus. Vivamus efficitur sapien vitae augue interdum ultrices ut non neque. Etiam '
                   'tincidunt orci quam, et posuere ex tempus eu. Etiam bibendum, quam tincidunt lacinia lobortis, '
                   'felis augue hendrerit urna, nec scelerisque neque sem non velit. Nam id facilisis quam. Nulla '
                   'facilisi. Duis non egestas libero, id aliquam augue. Aliquam egestas libero eu ligula sollicitudin '
                   'et quis lectus. Nulla porta dapibus enim vel dapibus. Aenean quis nibh eget dui iaculis vehicula '
                   'pretium odio. Nullam at efficitur eros, sollicitudin varius libero. Proin condimentum felis lectus '
                   'vitae egestas libero consequat ut. In non viverra enim. Vivamus vehicula, lectus sit amet aliquam '
                   'neque est auctor purus, nec dictum velit velit ut felis. Aenean eget eros pellentesque, ultrices '
                   'placerat est. Fusce eu dapibus justo, ac imperdiet tortor. In dapibus volutpat dolor, id facilisis '
                   'mi aliquet eget. In tellus magna, tempor in sem quis, efficitur laoreet erat. Nunc molestie mattis '
                   'cursus. In malesuada ipsum ut facilisis viverra. Class aptent taciti sociosqu ad litora torquent'
                   ' per conubia nostra, per inceptos himenaeos. Vivamus congue feugiat velit, varius turpis imperdiet'
                   ' eget. Fusce fringilla non dui quis placerat. Proin ac mauris venenatis, condimentum elit vel, '
                   'scelerisque ligula. Vestibulum viverra aliquam nisiMorbi interdum neque eleifend eros dignissim, '
                   'a posuere nulla volutpat. In aliquet lorem nec tellus hendrerit, eget sollicitudin diam rutrum. A'
                   'enean et nulla sed purus hendrerit mattis et at enim. Mauris aliquam aliquet ipsum id ullamcorper. '
                   'Proin a justo velit. Nullam ornare finibus tincidunt. Nulla facilisi. Donec et risus in dui '
                   'efficitur varius. Suspendisse vel maximus dolor. Etiam scelerisque metus non rutrum congue. '))
