def merge_the_tools(string, k):
    n = len(string)

    new = []
    new2 = []
    for i in range(0, len(string), k):
        new.append(string[i:i + k])

    for num in new:
        new1 = ''
        for i in range(len(num)):

            if num[i] not in new1:
                new1 = new1 + num[i]
            if num[i] in new1:
                pass
        new2.append(new1)


    for num in new2:
        print(num)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)