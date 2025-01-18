import itertools

n = 2
field =4
domain = range(field)

def generate_functions():
    input_space = list(itertools.product(domain, repeat=n))  
    possible_outputs = itertools.product(domain, repeat=len(input_space))  
    functions = []
    for outputs in possible_outputs:
        func = {input_space[i]: outputs[i] for i in range(len(input_space))}
        functions.append(func)
        yield func

def gf(f, x):
    input_space = list(itertools.product(domain, repeat=n))  
    count = {i: 0 for i in domain}  
    for y in input_space:
        x_plus_y = tuple((xi + yi) % field for xi, yi in zip(x, y))  
        result = (f[x_plus_y] - f[y]) % field  
        count[result] += 1
    return max(count, key=count.get)

# Check if the function is linear
def is_linear(func):
    input_space = list(itertools.product(domain, repeat=n)) 
    for x, y in itertools.product(input_space, repeat=n):
        x_plus_y = tuple((xi + yi) % field for xi, yi in zip(x, y))  
        if (func[x_plus_y] != (func[x] + func[y]) % field): 
            return False
    return True


def check_gf_equals_f(f):
    input_space = list(itertools.product(domain, repeat=n))  
    for x in input_space:
        if gf(f, x) != f[x]:  
            return False

    return True




def print_gf(f, x):
    print(f"x = {x} " )
    input_space = list(itertools.product(domain, repeat=n))  
    count = {i: 0 for i in domain}  
    for y in input_space:
        print(f"y = {y},", end=' ')
        x_plus_y = tuple((xi + yi) % field for xi, yi in zip(x, y)) 
        print(f"x + y = {x_plus_y},", end=' ')
        result = (f[x_plus_y] - f[y]) % field  
        print(f"f{x_plus_y} - f{y} = {result}", end=' ')
        count[result] += 1
        print(f"count = {count[result]}")
    return max(count, key=count.get)

for idx, func in enumerate(generate_functions(), start=1):
    if check_gf_equals_f(func):
        if not is_linear(func):
            print(f"Non-linear function found: {func}")
            input_space = list(itertools.product(domain, repeat=n))  
            for x in input_space:
                print_gf(func, x)
            exit(0)  



