class Controller(object):
    def __init__:
        pass

    def find_n_prime(self, n):
        def gen_primes():
            d = {}
            q = 2
            while True:
                if q not in d:
                    yield q
                    d[q*q] = [q]
                else:
                    for p in d[q]:
                        d.setdefault(p+q, []).append(p)
                    del d[q]
                q += 1
        i = 1
        primes = gen_primes()
        for p in primes:
            if i == n:
                return p
            else:
                i += 1

    def factorization(self, value):
        pass

    def ping_server(self, server, value):
        pass
