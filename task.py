import sys, subprocess

def execute(cmd):
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line 
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)

if sys.argv[1] == 'greet':
    for path in execute('echo hello'):
        print(path, end="")
elif sys.argv[1] == 'dev' or sys.argv[1] == 'development':
    for path in execute('export FLASK_APP=prunus && export FLASK_ENV=development && flask run'):
        print(path, end="")
elif sys.argv[1] == 'pro' or sys.argv[1] == 'production':
    for path in execute('gunicorn --certfile=keys/prunus.crt --keyfile=keys/prunus.key --bind 0.0.0.0:80 wsgi:app'):
        print(path, end="")

