class Stream:
        """A lazily computed linked list."""
        class empty:
            def __repr__(self):
                return 'Stream.empty'
        empty = empty()
        def __init__(self, first, compute_rest=lambda: empty):
            assert callable(compute_rest), 'compute_rest must be callable.'
            self.first = first
            self._compute_rest = compute_rest
        @property
        def rest(self):
            """Return the rest of the stream, computing it if necessary."""
            if self._compute_rest is not None:
                self._rest = self._compute_rest()
                self._compute_rest = None
            return self._rest
        def __repr__(self):
            return 'Stream({0}, <...>)'.format(repr(self.first))
            
def memo(f):
	cache = {}
	def memoized(*args):
		if args not in cache:
			cache[args] = f(*args)
		return cache[args]
	return memoized
            
cache = {}   
def prime_stream(first):
    """A stream of prime numbers.
    
    prime_stream(2)
    >>> Stream(2, <...>)
    
    prime_stream(2).rest
    >>> Stream(3, <...>)
    """
    def compute_rest():
        def is_prime(first):
            first += 1
            factors = []
            @memo
            def prime_factors(n):
                i = 2
                nonlocal factors
                while i * i <= n:
                    if n% i:
                        i += 1
                    else:
                        n //= i
                        factors += [i]
                if n > 1:
                    factors += [n]
                return factors
            prime_factors(first)
            if len(factors) != 1:
                return is_prime(first)
            else:
                return prime_stream(first)
        return is_prime(first)
    if first not in cache:
        cache[first] = Stream(first, compute_rest)
    return cache[first]

def first_k(s, k):
	"""Returns the k-th element of a Stream.
	
	first_k(prime_stream(2), 3)
	>>> Stream(5, <...>)
	"""
    while s is not Stream.empty and k > 1:
        s, k = s.rest, k-1
    return s
