import random


def get_defficulty():
    print("\n" + "=" * 40)
    print("welcome ")
    print("=" * 40)
    print("chooce the level:")
    print("1) easy (1_50 - 10 time)")
    print("2) middle (1_100 - 7 time)")
    print("3) hard (1_200 - 5 time)")

    while True:
        choice = input("chooce between 1-3: ")
        if choice == "1":
            return 1, 50, 10, "easy"
        elif choice == "2":
            return 1, 100, 10, "middle"
        elif choice == "3":
            return 1, 200, 10, "hard"
        else:
            print("invalid,please choose from 1-3")

def get_guess(low, high):
    while True:
        try:
            guess = int(input("enter your guess:"))
            if guess < low or guess > high:
                print(f"your guess should be between {low} and {high}")
                continue
            return guess
        except ValueError:
            print("please enter a number")

def play_game():
    low , high , max_attmpts,level_name= get_defficulty()
    secret=random.randint(low , high)
    attempts = 0
    print(f"\n choose a number between {low} and {high} ")
    print(f"level:{level_name}| your ettmpts:{max_attmpts}\n")
    while attempts < max_attmpts:
        remaining = max_attmpts - attempts
        print(f"remains:{remaining}")
        guess = get_guess(low , high)
        attempts += 1
        if guess == secret:
            print(f"your guess was correct")
            return True
        elif guess < secret:
            print(f"your guess was low")
        elif guess > secret:
            print(f"your guess was high")
    print(f"you lost corrct number is :{secret}")
    return False

def main():
    wins =0
    total =0
    while True:
        result = play_game()
        total += 1
        if result :
            wins += 1
        print(f"you won {wins} times, you play {total} times")
        again = input("do you want to play again?(y/n) ")
        if again != "y":
            print("bye")
            break
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye")
