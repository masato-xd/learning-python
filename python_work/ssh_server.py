import paramiko

# hostname='192.168.0.102'
hostname = '192.168.89.105'
username = 'root'
password = '123456'

# port=22
if __name__ == '__main__':
    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    # s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = s.exec_command('ifconfig;df -TH')
    print stdout.read()
    print stderr.read()
    s.close()