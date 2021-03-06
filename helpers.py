#!/usr/bin/python3
import os
import subprocess

# HOTSOS GLOBALS
DATA_ROOT = os.environ.get('DATA_ROOT', '/')


def get_ip_addr():
    if DATA_ROOT == '/':
        ip_addr_show = subprocess.check_output(['ip', '-d', 'address'])
        return ip_addr_show.decode('UTF-8').splitlines()

    path = os.path.join(DATA_ROOT,
                        "sos_commands/networking/ip_-d_address")
    if os.path.exists(path):
        return open(path, 'r').readlines()


def get_ps():
    if DATA_ROOT == '/':
        ps = subprocess.check_output(['ps'])
        return ps.decode('UTF-8').splitlines()

    path = os.path.join(DATA_ROOT,
                        "ps")
    if os.path.exists(path):
        return open(path, 'r').readlines()


def get_numactl():
    if DATA_ROOT == '/':
        numactl = subprocess.check_output(['numactl', '--hardware'])
        return numactl.decode('UTF-8').splitlines()

    path = os.path.join(DATA_ROOT,
                        "sos_commands/numa/numactl_--hardware")
    if os.path.exists(path):
        return open(path, 'r').readlines()