#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import asyncio
import os
import socket
import subprocess

from aiohttp import web


def gen_primes():
    """Generate primes generator

    Function which simply create a generator of primes

    """

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
    """Find the prime which is n-prime

    :param request: HTTP request
    :type request: aiohttp.web.Request
    :return: HTTP response containing n-prime
    :rtype: aiohttp.web.Response

    """

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
    """Function which is made factorization on value from request

    :param request: HTTP request
    :type request: aiohttp.web.Request
    :return: HTTP response containing n-prime
    :rtype: aiohttp.web.Response

    """

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
    """Ping specified host n times

    :param request: HTTP request
    :type request: aiohttp.web.Request
    :return: HTTP response containing n-prime
    :rtype: aiohttp.web.Response

    """

    post = await request.post()
    host = post.get('host')
    n = post.get('reps')

    process = await asyncio.create_subprocess_shell(
        "ping -c {0} {1}".format(n, host), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    data, err = await process.communicate()
    if not err:
        return web.Response(text="{0}\n".format(str(data)))
    else:
        return web.Response(text="{0}\n".format(str(err)))
