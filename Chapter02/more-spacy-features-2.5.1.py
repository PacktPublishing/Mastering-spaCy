#!/usr/bin/env python3

doc = nlp("Hello, hi!")
print(doc[0].lower_)

doc1 = nlp("HELLO, Hello, hello, hEllO")
print(doc[0].is_upper)
print(doc[0].is_lower)
print(doc[1].is_upper)
print(doc[1].is_lower)


doc2 = nlp("Cat and Cat123")
print(doc[0].is_alpha)
print(doc[2].is_alpha)


doc3 = nlp("Hamburg and Göttingen")
print(doc3[0].is_ascii)
print(doc3[2].is_ascii)


doc4 = nlp("Cat Cat123 123")
print(doc4[0].is_digit)
print(doc4[1].is_digit)
print(doc4[2].is_digit)



doc5 = nlp("You, him and Sally")
print(doc5[1])
print(doc5[1].is_punct)


doc6 = nlp(" ")
print(doc6[0])
print(len(doc6[0]))
print(doc6[0].is_space)

doc7 = nlp("I paid 12$ for the t-shirt.")
print(doc7[3])
print(doc7[3].is_currency)


doc8 = nlp("I emailed you at least 100 times")
print(doc8[-2])
print(doc8[-2].like_num)

doc9 = nlp("I emailed you at least hundred times")
print(doc9[-2])
print(doc9[-2].like_num)

doc10 = nlp("My email is duygu@packt.com and you can visit me under https://duygua.github.io any time you want.")
print(doc10[3])
print(doc10[3].like_email)
print(doc10[10])
print(doc10[10].like_url)

doc11 = nlp("Girl called Kathy has a nickname Cat123.")
for token in doc11:
    print(token.text, token.shape_)

