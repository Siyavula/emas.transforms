import functools
import cPickle

import os
DIRNAME = os.path.dirname(__file__)
KEYFUNC = None

class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func

   def __call__(self, *args):
      key = KEYFUNC(self, *args)
      with open(os.path.join(DIRNAME, 'cache.pickle'), 'rb') as fp:
         cache = cPickle.load(fp)
      try:
         result = cache[key]
         return result
      except KeyError:
         value = self.func(*args)
         cache[key] = value
         with open(os.path.join(DIRNAME, 'cache.pickle'), 'wb') as fp:
            cPickle.dump(cache, fp)
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__
   def __get__(self, obj, objtype):
      """Support instance methods."""
      return functools.partial(self.__call__, obj)

def cache(keyFunc):
   global KEYFUNC
   KEYFUNC = keyFunc
   return memoized
