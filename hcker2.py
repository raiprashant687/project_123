def merge_the_tools(string, k):
    n = len(string)
    new = []
    new2 = []
    new1 = set()
    for i in range(0, len(string), k):
        new.append(string[i:i + k])

    for num in new:
        new1 = set(num)
        new2.append(new1)

    print(new2)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)