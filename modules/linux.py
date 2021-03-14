import subprocess

def run(cmd):
    completed = subprocess.run([cmd], shell=True)
    return completed

def output(task):
    print(task.stdout)