import dis
def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a**b) / i
        except Exception:
            result = a + b
        finally:
            return result
dis.dis(magic_calculation)