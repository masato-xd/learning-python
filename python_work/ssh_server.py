import paramiko

# hostname='192.168.0.102'
hostname = '113.196.57.39'
username = 'bob'
password = 'fuvu/u1l'

port = 44818
if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    # s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(port=port, hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = s.exec_command('df -TH')
    print stdout.read()
    print stderr.read()
    s.close()
