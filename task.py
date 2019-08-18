import sys, subprocess

'''
    --- Custom Task Runner Utilities ---
'''
class Task:
    def __init__(self,name,script):
        self.name = name
        self.script = script

class TaskRunner:
    def __init__(self):
        self.tasks = []

    def AddTask(self,name,script):
        if type(name) == list:
            for alt in name:
                self.tasks.append(Task(alt,script))
        else:
            self.tasks.append(Task(name,script))

    def RunTask(self,name):
        for task in self.tasks:
            if task.name == name:
                for path in self.__execute(task.script):
                    print(path, end="")
        else:
            raise Exception('The script \'' + name + '\' could not be found.')

    def __execute(self,cmd):
        popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        for stdout_line in iter(popen.stdout.readline, ""):
            yield stdout_line 
        popen.stdout.close()
        return_code = popen.wait()
        if return_code:
            raise subprocess.CalledProcessError(return_code, cmd)

'''
    --- Prunus Task Runner Implementation ---
'''
if __name__ == '__main__':
    taskRunner = TaskRunner()
    taskRunner.AddTask('greet','echo hello')
    taskRunner.AddTask(['dev','development', 'debug'],'export FLASK_APP=app.py && export FLASK_ENV=development && flask run')
    taskRunner.AddTask(['pro','production'],'gunicorn --bind 0.0.0.0:80 wsgi:app')

    taskRunner.RunTask(sys.argv[1])


