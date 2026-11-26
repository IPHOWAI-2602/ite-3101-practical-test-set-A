def main():
    while True:
        try:
            upper_length=float(input("Enter upper length: "))
            lower_length=float(input("lower upper length: "))
            h=float(input("Enter height:"))
            break
        except ValueError:
            print("error")
            exit(-1)

    area=area = ((upper_length + lower_length) * h) / 2
    print(f'The area of the trapezoid is {area}')
    # Replace pass with your Python code.
    


if __name__ == "__main__":
    # execute only if run as a script
    main()
