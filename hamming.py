if __name__=="__main__":
    array=[None]*8
    for i in range(0,8):
        string=int(input("Enter 0 or 1:"))
        while string>1 or string<0:
            string=int(input("Please enter 0 or 1:"))
        array[i]=string
        print(array[i])    
    print(array)

    array2=[None]*12
    array2[2]=array[0]
    array2[4]=array[1]
    array2[5]=array[2]
    array2[6]=array[3]
    array2[8]=array[4]
    array2[9]=array[5]
    array2[10]=array[6]
    array2[11]=array[7]
            
    print(array2)

    print("Checking For Parity 1")
    result=array2[2]+array2[4]+array2[6]+array2[8]+array2[10]

    if result%2==0:
        array2[0]=0
    else:
        array2[0]=1

    print(array2)

    print("Checking For Parity 2")
    result=array2[2]+array2[5]+array2[6]+array2[9]+array2[10]
    
    if result%2==0:
        array2[1]=0
    else:
        array2[1]=1
        
    print(array2)

    print("Checking For Parity 3")
    result=array2[4]+array2[5]+array2[6]+array2[11]

    if result%2==0:
        array2[3]=0
    else:
        array2[3]=1
        
    print(array2)

    print("Checking For Parity 4")
    result=array2[8]+array2[9]++array2[10]+array2[11]

    if result%2==0:
        array2[7]=0
    else:
        array2[7]=1

    array3=[None]*12     
    print("Encoded data is:",array2)
