# warc exploration

# NOTE: Must use python 2.7 because other versions don't support the warc module 
import warc
import paramiko 
from collections import OrderedDict

# Connecting to server
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('datasci.library.ucdavis.edu', username='wpschmid', password='WS:2085-t2047')

# storing all warc file names to a list
apath = '/dsl/WARC/warc'
apattern = '"*.warc.gz"'
rawcommand = 'find {path} -name {pattern}'
command = rawcommand.format(path=apath, pattern=apattern)
stdin, stdout, stderr = ssh.exec_command(command)
filelist = stdout.read().splitlines()

# Pulling files from server and storing on local machine. Transfers relevant info in separate .txt files on machine as well
import os

for i in range(0, len(filelist)):
    sftp_client = ssh.open_sftp()
    sftp_client.chdir("/dsl/WARC/warc")
    f = sftp_client.open(filelist[i][15:])
    path = os.path.join(r"C:\Users\William\Desktop\warc_project\raw_warc_files", filelist[i][15:])
    sftp_client.get("/dsl/WARC/warc/" + filelist[i][15:], path) # try to find a way to open file from server instead of storing on machine
    file = warc.open(path)

    # Writing contents of warc to text file
    file_name = "C:\Users\William\Desktop\warc_project\warc_info_files\warc_info_file_" + str(i+1) + ".txt"
    with open(file_name, 'w+') as text_file: 
        for record in file:
            #text_file.write('WARC Header Info: \n')
            #text_file.write('WARC type:'+ record['WARC-Type']+ '\n'+ 'WARC date:'+ record['WARC-Date']+ '\n'+ 'Content Type:'+ record['Content-Type']+ '\n'+ 'Content Length:'+ record['Content-Length'])
            text_file.write('WARC date:'+ record['WARC-Date'] + '\n'+ 'Content Length:'+ record['Content-Length'] + '\n')
            if 'WARC-Target-URI' in record:
                text_file.write('Target URI:'+ record['WARC-Target-URI']+ '\n')
            if 'WARC-Concurrent-To' in record:
                text_file.write('Concurrent-To:'+ record['WARC-Concurrent-To']+ '\n')
            if 'WARC-Refers-To' in record:
                text_file.write('Refers-To:'+ record['WARC-Refers-To']+ '\n')
            if 'via:' in record:
                text_file.write('Via:'+ record['via:']+ '\n')
            #text_file.write('WARC Record Payload:'+ '\n')
            #text_file.write(record.payload.read())
            text_file.write('=-=-' * 25 + '\n')
            
    # Writing only URI's to a .txt file
    sftp_client = ssh.open_sftp()
    sftp_client.chdir("/dsl/WARC/warc")
    f = sftp_client.open(filelist[i][15:])
    path = os.path.join(r"C:\Users\William\Desktop\warc_project\raw_warc_files", filelist[i][15:])
    sftp_client.get("/dsl/WARC/warc/" + filelist[i][15:], path) # try to find a way to open file from server instead of storing on machine
    file = warc.open(path)
    file_name = "C:\Users\William\Desktop\warc_project\warc_uri\uri_list_" + str(i+1) + ".txt"
    with open(file_name, "w+") as text_file:
        for record in file:
            if 'WARC-Target-URI' in record:
                text_file.write(record['WARC-Target-URI']+ '\n')
            
    # Create new .txt file with only unique URL's
    new_file_name = "C:\Users\William\Desktop\warc_project\unique_warc_uri\unique_uri_list_" + str(i+1) + ".txt"
    with open(file_name) as infile, open(new_file_name, 'w+') as outfile:
        outfile.writelines(OrderedDict.fromkeys(infile))