import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} tomó {end - start} segundos")
        return result
    return wrapper

@time_it
def process_file(file_path):
    with open(file_path) as file:
        for line in file:
            yield line.strip()

@time_it
def generate_stats(file_path):
    stats = {}
    for line in process_file(file_path):
        words = line.split()
        for word in words:
            if word in stats:
                stats[word] += 1
            else:
                stats[word] = 1
    return stats

if __name__ == "__main__":
    stats = generate_stats("archivo_grande.txt")
    print(stats)
