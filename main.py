from random import shuffle

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def sort_coin(coins):
    for i in range(len(coins)-1):
        min_index = i
        for j in range(i+1, len(coins)):
            if coins[j] < coins[min_index]:
                min_index = j
        swap(coins, i, min_index)
        swap(coins, i+1, min_index+1 if min_index+1<len(coins) else min_index-1)

def main():
    coins = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    shuffle(coins)

    sort_coin(coins)
    print(coins)
    for i in range(1, len(coins)):
        assert coins[i-1] <= coins[i]

if __name__ == '__main__':
    main()