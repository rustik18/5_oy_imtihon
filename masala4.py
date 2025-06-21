from multiprocessing import Process

def negative(lst):
    print("Printing negatives..")
    print(list(filter(lambda x: x< 0, lst)))

def positive(lst):
    print("Printing positives")
    print(list(filter(lambda x: x > 0, lst)))

def zero(lst):
    print("Printing zeros")
    print(list(filter(lambda x: x == 0, lst)))

numbers = [1, 5, 34, 0, 43, -43, -64, -2, -6, 0, 3, 0]

if __name__ == '__main__':
    ps = [Process(target=negative, args=(numbers,)), Process(target=positive, args=(numbers,)), Process(target=zero, args=(numbers,))]
    for p in ps:
        p.start()

    for p in ps:
        p.join()
