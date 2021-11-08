import pysftp

myHostname = "Ubuntu"
myUsername = "samat"
myPassword = "samat"

localFilePath = '/home/samat'
remoteFilePath = '/home/samat'
with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print("Connection succesfully stablished ... ")

    # Switch to a remote directory
    sftp.cwd('/home/samat/')

    # Obtain structure of the remote directory '/var/www/vhosts'
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:
        print(attr.filename, attr)
    
    sftp.put(localFilePath, remoteFilePath)
    
# connection closed automatically at the end of the with-block