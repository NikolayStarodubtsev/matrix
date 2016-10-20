import asyncio
import os
import socket
import subprocess

from aiohttp import web


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


async def find_n_prime(request):
    post = await request.post()

    n = int(post.get('n'))

    i = 1
    primes = gen_primes()
    for p in primes:
        if i == n:
            return web.Response(text="The {0}th prime is {1}\n".format(n, p))
        else:
            i += 1


async def factorization(request):
    post = await request.post()

    n = int(post.get('n'))
    d = 2

    factors = []
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1:
                factors.append(n)
            break
    return web.Response(text="The factors is {0}\n".format(factors))


async def ping_server(request):
    post = await request.post()
    host = post.get('host')
    n = post.get('reps')

    process = await asyncio.create_subprocess_shell(
        "ping -c {0} {1}".format(n, host), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    data, err = await process.communicate()
    if not err:
        return web.Response(text=str(data))
    else:
        return web.Response(text=str(err))
