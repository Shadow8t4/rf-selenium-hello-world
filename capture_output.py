from contextlib import redirect_stdout
import io
from robot import run
from subprocess import Popen, PIPE, call
from threading import Thread
import sys
from os import fork, remove
from pygtail import Pygtail


def run_test(test, variable, file_io):
    with redirect_stdout(file_io):
        run(test, variable=variable, stdout=file_io)
        print('EOF')
    file_io.close()


def meta_run_test(test, variable):
    print('TEst')
    jobs = [run_test, print_stdout_stream]
    file_io = open('output', 'w+')
    j0 = Thread(target=jobs[1])
    j0.start()
    j1 = Thread(target=jobs[0], args=[test], kwargs={
                'variable': variable, 'file_io': file_io})
    j1.start()


def print_stdout_stream():
    remove('output.offset')
    eof = False
    while(not eof):
        for line in Pygtail('output'):
            if('EOF' in line):
                eof = True
                break
            call(f'echo "{line.strip()}"'.split())


def main():
    variable = ['BROWSER:Headless Firefox']
    test = 'test.robot'

    meta_run_test(test, variable)

    return ''


if(__name__ == '__main__'):
    print(main())
