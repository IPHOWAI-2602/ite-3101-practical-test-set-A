def main():
    while true:
        try:
            upper_length=float(input("Enter upper length: "))
            lower_length=float(input("lower upper length: "))
            h=float(input("Enter height:"))
            break
        except ValueError:
            print("error")

            area=upper_length+lower_length*h
            print(f'{}')
    # Replace pass with your Python code.
    


if __name__ == "__main__":
    # execute only if run as a script
    main()
