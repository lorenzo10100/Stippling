import pstats 
from pstats import SortKey

p = pstats.Stats('stippling_main.prof')
p.sort_stats(SortKey.TIME).print_stats(10)
