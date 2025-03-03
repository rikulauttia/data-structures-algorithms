import re

def evaluate(data):
    def replacer(match):
        expr = match.group(0)
        if expr.startswith("add("):
            x, y = map(int, expr[4:-1].split(","))
            return str(x + y)
        elif expr.startswith("mul("):
            x, y = map(int, expr[4:-1].split(","))
            return str(x * y)
        return expr
    
    return re.sub(r'add\(\d+,\d+\)|mul\(\d+,\d+\)', replacer, data)

if __name__ == "__main__":
    print(evaluate("add(1,2)")) # 3
    print(evaluate("aybabtu")) # aybabtu
    print(evaluate("mul(6,7),mul(7,191)")) # 42,1337
    print(evaluate("abadd(123,456)mulxmul(3,13)")) # ab579mulx39
    print(evaluate("mul()mul(13)mul(0,1)")) # mul()mul(13)mul(0,1)

    data = "mul(6,7)"*10**5
    result = evaluate(data)
    print(len(result)) # 200000
    print(result[:20]) # 42424242424242424242