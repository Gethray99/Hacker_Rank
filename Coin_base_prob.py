
def get_way(n, coins):
    global num_methods
    for i in range(len(coins)):
        print(f"iterration {i}, current coin: {coins[i]}, remaining amount: {n}")
        if n%coins[i] == 0:
            print("inside if")
            num_methods += 1    
            number = int((n/coins[i]))
            remain = int(coins[i]*(number-1))
            if remain > 0:
                get_way(remain, coins[i+1:])
        else:
            print("inside else")
            remain2 = int(n%coins[i])
            if remain2 > 0:
                get_way(remain2, coins[i+1:])
    return num_methods


if __name__ == "__main__":
    change = int(input("Enter the amount of change: "))
    user_inputs = input("Enter the number of inputs followed by the inputs themselves, separated by spaces: \n")
    inputs = list(map(int, user_inputs.split()))
    print("Original inputs:", inputs)
    inputs.sort(reverse=True)
    print("Sorted inputs in descending order:", inputs)
    num_methods = 0
    total_ways = get_way(change, inputs)
    print(f"Total ways to make change for {change} with coins {inputs}: {total_ways}")
    
