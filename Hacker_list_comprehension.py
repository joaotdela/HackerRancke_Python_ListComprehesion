if __name__ == '__main__':
    x = int(input('X value: '))
    y = int(input('Y value: '))
    z = int(input('Z value: '))
    n = int(input('N value: '))

    allper=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(allper)