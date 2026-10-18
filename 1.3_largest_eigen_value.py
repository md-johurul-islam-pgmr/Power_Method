while True:
    try:
        m, n = map(int, input("Order of  Square-Matrix A. Comma separated-n,n: ").split(","))
        if n < 0 or m < 0 or m != n:
            raise ValueError("Order is always Positive and must be equal")

        A = []

        for i in range(m):
            row = list(map(int, input(f"Enter {i+1} no Row: ").split(",")))
            A.append(row)

        V = list(map(int, input("Enter Initial-vector V (transposed and comma saperated): ").split(",")))
        if len(V) != n:
            raise ValueError(f"Order of V should be {n}")
        
        break

    except ValueError as error:
        print(f"Invalid Input: {error}. Please try again")


end = False

while end == False:
    AV = []
    EV = []
    for row in A:
        A_prod_V = 0
        for i in range(len(row)):
            A_prod_V += round(row[i]*V[i], 3)
        AV.append(A_prod_V)

    #to identify the element of V contains 1 to make new V's same elelment 1.
    for k in range(len(V)):
        if V[k] == 1:
            devide_by = AV[k]
            if devide_by == 0:
                devide_by = max(AV, key=abs)
            break

    for j in range(len(AV)):
        E_prod_V = round(AV[j]/ devide_by, 3)
        EV.append(E_prod_V)

    print(f"Eigen value: {devide_by}, Corresponding Eigen Vector: {EV}")

    if EV == V:
        end = True
        print(f"Largest eigen value: {devide_by}, Corresponding Eigen Vector: {EV}")
    else:
        V = EV