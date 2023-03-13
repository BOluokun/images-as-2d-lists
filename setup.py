import sys
import os
import subprocess

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


if __name__ == '__main__':
    env = os.environ.copy()
    env['PYTHONPATH'] = os.pathsep.join(sys.path)
    try:
        p = subprocess.run(["python3","-m", "pip", "install", "-r", "requirements.txt"], env=env, check=True, capture_output=True)
        print(p.stdout)
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        print(str(e.stdout))

