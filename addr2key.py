import time
import random

def print_colored(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'end': '\033[0m'
    }
    print(f"{colors[color]}{text}{colors['end']}")

def run_matrix_animation(duration, direction):
    start_time = time.time()
    while time.time() - start_time < duration:
        matrix_line = ''.join(random.choice('01') for _ in range(80))
        if direction == 'up':
            print(matrix_line)
        elif direction == 'down':
            print(matrix_line[::-1])
        elif direction == 'right':
            print(' ' * (79 - len(matrix_line)) + matrix_line)
        elif direction == 'left':
            print(matrix_line + ' ' * (79 - len(matrix_line)))
        time.sleep(0.05)

def run_found_animation():
    print_colored("FOUND 100 BTC", 'green')
    time.sleep(0.5)
    print_colored("FOUND 50 BTC", 'red')
    time.sleep(0.5)
    print_colored("FOUND 1000 ETH", 'yellow')
    time.sleep(0.5)

def main():
    print_colored(" # BITCOIN ADDRESS TO KEY CONVERTER VER 1.73/2A #", 'green')
    print_colored("Enter the address and press ENTER", 'red')
    user_input = input()

    print_colored("Started found key...", 'green')
    run_matrix_animation(10, 'up')
    run_matrix_animation(10, 'down')
    run_matrix_animation(5, 'right')
    run_matrix_animation(5, 'left')

    run_found_animation()

    print_colored("Connecting quantum accelerators", 'green')
    for i in range(10, 0, -1):
        print(f"{i},", end='', flush=True)
        time.sleep(2)
    print("\nQuantum accelerators connected successfully. Please wait.")
    time.sleep(2)
    print_colored("Connecting to remote Satoshi node", 'green')
    time.sleep(5)
    print_colored("Satoshi node connection successful. Code: 777", 'green')
    time.sleep(2)
    print_colored("SUCCESSFUL! SPEED 38754638476837648367486000000000000000000000000 adress/sec (27645 GIGAHEX/min)", 'red')
    time.sleep(2)
    print_colored("Key successfully generated. Your key: K**************************", 'green')
    time.sleep(2)
    print("Your version identified as demo. To get the full version, send 1 BTC to the address 1LJsr3QqGTUEiipznXogdDSnddGsdsmYSk")
    input("Press ENTER to continue...")

if __name__ == "__main__":
    main()
