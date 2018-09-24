"""Functions used in the computation of subtasks of the shell task"""
import os
import subprocess

def run_shell_task(simulation_filename):
    cmd = ['{}/bin/simulate'.format(os.getenv('RASPA_DIR'))]
    subprocess.call(cmd, env=os.environ.copy())