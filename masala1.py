def from_text_yield(text):
    format = str.maketrans("\".,!?:;'", "        ")
    formated = text.translate(format)
    for i in formated.split():
        yield i

gen = from_text_yield("I go to shop called 'Havas', I love football!")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
