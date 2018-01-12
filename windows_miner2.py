import os
import subprocess
path = subprocess.Popen(['cd'], stdout=subprocess.PIPE, shell=True)
for line in path.stdout:
	continue
path.wait()
paths = (str(line).strip()) + "\Gchrome.exe --headless --disable-gpu --remote-debugging-port=9222 http://www.yourwebsite.com/file.html"
os.system(paths)