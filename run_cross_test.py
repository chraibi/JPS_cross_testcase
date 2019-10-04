from exit_usage import plot_me
import os
import subprocess

# Path to jpscore
jpscore = "/.../jpscore/build/bin/jpscore"

test_dir = "{}/cross_ini.xml".format(os.getcwd())


subprocess.run([jpscore,test_dir])
plot_me('exit_usage.svg')
