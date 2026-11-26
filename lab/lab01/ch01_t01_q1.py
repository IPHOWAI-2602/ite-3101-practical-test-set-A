def main():
    while True:
        try:
            num=int(input("Type an integer:"))
            break
        except ValueError:
            print("error")
    if num * 3 ==0 and num * 5!=0:
        print(f'{num}is divisible by both 3 and 5')
    else:
        print(f'{num}is not divisible by both 3 and 5')

    


if __name__ == "__main__":
    # execute only if run as a script
    main()
