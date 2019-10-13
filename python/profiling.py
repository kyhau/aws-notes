"""
See https://stackoverflow.com/questions/5375624/a-decorator-that-profiles-a-method-call-and-logs-the-profiling-result/47945389#47945389
"""
import cProfile
import functools


def profileit(func):
    @functools.wraps(func)  # <-- Changes here.
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile" # Name the data file sensibly
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        prof.dump_stats(datafn)
        return retval

    return wrapper


@profileit
def function_you_want_to_profile():
    pass