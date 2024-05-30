a = "abcdefghijklmnopqrstuvwxyz"
def print_rangoli(size):
    lines=[]
    for row in range(size):
        print_="-".join(a[row:size])
        lines.append(print_[::-1] + print_[1:])
    Width = len(lines[0])
    for row in range(size-1, 0, -1):
        print(lines[row].center(Width, '-'))
    for row in range(size):
        print(lines[row].center(Width, '-'))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
