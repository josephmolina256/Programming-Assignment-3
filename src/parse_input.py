def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    k = int(lines[0])
    values = {}

    for i in range(1, k+1):
        pair = lines[i].split()
        values[pair[0]] = int(pair[1])
        
    a = lines[-2]
    b = lines[-1]

    return values, a, b

