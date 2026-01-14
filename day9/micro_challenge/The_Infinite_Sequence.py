# Goal: Write a while True generator that produces Fiboancci numbers forever.
# Deep dive: This is impossible with a standard list(RAM would fill up). Generators allow
#            INfinite Data streams because they process one item at a time(Lazy Evaluation).

def inf_fibo():
    pre, curr = 0, 1
    while True:
        pre, curr = curr, pre + curr
        yield curr

fibo_gen = inf_fibo()

for _ in range(10):
    print(next(fibo_gen))