
# Get public SSH key to remote connect

To connect to a remote server in which I can launch big processes we follow two steps:
- I generate my public and private keys
- I give the public key to my supervisor and he adds it into `.ssh/authorized_keys`

And now I can SSH!

To do this I run

`ssh-keygen -t rsa`

and follow the default instructions without password.

