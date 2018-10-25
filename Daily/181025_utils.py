class Line_Profiler(object):
    """put @profile on ur functions"""
    def __init__(self, follow=None):
        self.follow = follow or []

    def __call__(self, func):
        def profiled_func(*args, **kwargs):
            line_profiler = LineProfiler()
            line_profiler.add_function(func)
            map(lambda x: line_profiler.add_function(x), self.follow)
            line_profiler.enable_by_count()
            result = func(*args, **kwargs)

            line_profiler.disable_by_count()
            line_profiler.print_stats(stripzeros=True)
            return result

        return functools.wraps(func)(profiled_func)


__builtin__.profile = Line_Profiler()
