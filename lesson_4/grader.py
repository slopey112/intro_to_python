from sys import argv

def get_lines(filename):
    with open(filename, 'r') as f:
        lines = f.readlines() 
    return lines

def main():
    a = get_lines(argv[1] + '.sol')
    b = get_lines(argv[1] + '.out')
    right = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            right += 1
    print('You got {} right out of {}!!!'.format(right, len(a)))

if __name__ == '__main__':
    main()
