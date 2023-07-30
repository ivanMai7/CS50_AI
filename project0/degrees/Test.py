def main():
    a = (1,2)
    list = [3,4]
    tmp = list.copy()
    tmp.append(a)
    print(tmp)
    print(list)

if __name__ == "__main__":
    main()