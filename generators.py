# def gen(name):
#     for ch in name:
#         yield ch
#
#
# g = gen('Max')
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# import uuid
#
#
# def gen_jpg_file():
#     pattern = '{}.jpg'
#     while True:
#         yield pattern.format(uuid.uuid1())
#         print(45)
#
#
# g = gen_jpg_file()
# # print(next(g))
# # print(5+4)
# # print(5+7)
# # print(next(g))

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 'Filish'
#
# g = gen()


def gen1(name):
    for i in name:
        yield i


def gen2(n):
    for i in range(n):
        yield i


tasks = [gen2(8), gen1('Max')]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
