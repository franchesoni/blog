
# Log in to SSH without password

It's much easier than you think. Just run*

`ssh-copy-id user@remoteserver`

*if you have a public key. You can check if you have one if `id_rsa.pub` is listed when you run `ls ~/.ssh/`. If not, generate one using `ssh-keygen -t rsa`.