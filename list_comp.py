
if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    array_3d = [[a,b,c] for a in range(0,x+1)for b in range(y+1)for c in range(z+1) if a+b+c != n]
    print(array_3d)
