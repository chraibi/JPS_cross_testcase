import os
import subprocess
import datetime
import time
from exit_usage import plot_me
import sys

if len(sys.argv) == 1:
    sys.exit("usage: %s full_path_to_jpscore"%sys.argv[0])

# Path to jpscore
jpscore = sys.argv[1]

test_dir = "{}/cross_ini.xml".format(os.getcwd())


subprocess.run([jpscore, test_dir])
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H%M%S')
figname = '%s.png'%st
print("output: %s"%figname)
plot_me(figname)
