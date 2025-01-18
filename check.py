import itertools

n = 2
field =4
domain = range(field)
input_space = list(itertools.product(domain, repeat=n)) 

''
func = {(0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 0,
        (1, 0): 0, (1, 1): 0, (1, 2): 0, (1, 3): 2,
        (2, 0): 2, (2, 1): 2, (2, 2): 0, (2, 3): 2,
        (3, 0): 0, (3, 1): 2, (3, 2): 0, (3, 3): 0}

def gf(f, x):
    count = {i: 0 for i in domain}
    for y in input_space:
        x_plus_y = tuple((xi + yi) % field for xi, yi in zip(x, y)) 
        result = (f[x_plus_y] - f[y]) % field 
        count[result] += 1
    return max(count, key=count.get)

def is_linear(func):
    for x, y in itertools.product(input_space, repeat=n):
        x_plus_y = tuple((xi + yi) % field for xi, yi in zip(x, y)) 
        if (func[x_plus_y] != (func[x] + func[y]) % field):
            print(f"x = {x}, y = {y}, x + y = {x_plus_y}, f(x + y) = {func[x_plus_y]}, f(x) = {func[x]}, f(y) = {func[y]}")
            return False
    return True

def check_gf_equals_f(f):
    for x in input_space:
        if print_gf(f, x) != f[x]:  # Compare g_f(x) to f(x)
            return False
    return True

def print_gf(f, x):
    print(f"x = {x} " )
    count = {i: 0 for i in domain}  
    for y in input_space:
        print(f"y = {y},", end=' ')
        x_plus_y = tuple((xi + yi) % field for xi, yi in zip(x, y)) 
        print(f"x + y = {x_plus_y},", end=' ')
        result = (f[x_plus_y] - f[y]) % field  
        print(f"f{x_plus_y} - f{y} = {result}", end=' ')
        count[result] += 1
        print(f"count = {count[result]}")
    gf_x = max(count, key=count.get)
    print(f"g_f{x} = {gf_x} = f{x} = {f[x]}")
    return gf_x
print(func)
if check_gf_equals_f(func):
    if not is_linear(func):
        exit(0)  # Exit after finding the first non-linear bent function