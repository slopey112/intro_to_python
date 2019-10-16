from sys import argv

def get_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines() 
    return lines

def main():
    a = get_lines(argv[1] + '.sol')
    b = get_lines(argv[1] + '.out')
    for i in range(len(a)):
        if a[i] != b[i]:
            print('Wrong')
            return
    print('correct!!!!!!!')

if __name__ == '__main__':
    main()
