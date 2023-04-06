# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    input_type = input().rstrip().upper()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        file_name = input()
        with open("tests/" + file_name) as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        print("Invalid input type")
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return pattern, text
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = 10 ** 9 + 7
    x = 263
    n = len(text)
    m = len(pattern)
    patterns = sum(ord(pattern[i]) * x ** i for i in range(m)) % p
    hashes = [0] * (n - m + 1)
    s = text[n - m : n]
    hashes[n - m] = sum(ord(s[i]) * x ** i for i in range(m)) % p
    x_m = pow(x, m, p)

    for i in range(n - m - 1, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - x_m * ord(text[i + m])) % p
    # and return an iterable variable
    return [i for i in range(n - m + 1) if hashes[i] == patterns]
    #return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

