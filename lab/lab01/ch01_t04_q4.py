def is_right_angle(a: float, b: float, c: float) -> bool:
    result = ""
    if a >0:
            for a in range(1,n+1):
                result+str(a)
             return result
                
      
    


def main():
    try:
        a=float(input("side a:"))
        b=float(input("side b:"))
        c=float(input("side c:"))
    except ValueError:
                   print("error")
        triangle=a**2+B**2
        print(f'The triangle is a right-angle triangle{triangle}')
              
    


if __name__ == "__main__":
    # execute only if run as a script
    main()
