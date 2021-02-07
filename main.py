import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--x', type=int, default=7,
                    help='First number, default 7')
parser.add_argument('--y', type=int, default=12,
                    help='Second number, default 12')

args = parser.parse_args()

def lcm_df_r(x, y, i=1):
    print(x, y)
    result = x * i / y
    print(result)
    if result == x:
        return x * i
    else:
        return lcm_df_r(x, y, i + 1)

def lcm_df(x, y):
    return lcm_df_r(x, y)

def lcm_bf(x, y):
    found = False
    current_x = x

    while not found:
        print(f'Current Multiple: {current_x} {current_x / y}')
        if current_x / y == x:
            found = True
            break
        current_x = current_x + x

    return current_x

def main():
    x = args.x
    y = args.y

    print(f'Least Common Multiple for {x} and {y}')

    df_result = lcm_df(x, y)
    bf_result = lcm_bf(x, y)

    x_times = df_result / x
    y_times = df_result / y

    print(f'df: {df_result}')
    print(f'bf: {bf_result}')
    print(f'\nLCM is {df_result}')
    print(f'X into {df_result} = {x_times}')
    print(f'Y into {df_result} = {y_times}')

if __name__ == '__main__':
    main()
