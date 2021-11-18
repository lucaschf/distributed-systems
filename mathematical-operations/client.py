from rpc import MathematicalOperations

RPC_SERVER = "10.0.1.15"
RPC_PORT = 12000

mop = MathematicalOperations(RPC_SERVER, RPC_PORT)

s = mop.sum(1, 2)
f = mop.factorial(5)
p = mop.product(5, 4)

print(s)
print(f)
print(p)
