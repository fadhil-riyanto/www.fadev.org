# Cgit setup

Ku mau share pengalaman bikin self hosting git server, pakai cgit, biar engga kalah aja sama git.kernel.org dan kernel.dk wkwk

step satu, include dir nya sites-available spt biasa, contoh config nya
https://gist.github.com/fadhil-riyanto/328f2cc0607eb58b713cdeaa473d08ee, lalu config untuk sites-available nya
https://gist.github.com/fadhil-riyanto/c2e26de30c97600e4ee9342aefbd6ece

nb: install fcgiwrap dulu

lalu edit /etc/cgitrc, contoh config: https://gist.github.com/fadhil-riyanto/4033e6ce59a35568c31dbd5e5a1d29bd

harusnya sampai sini, cgit dah bisa diakses, cuman empty repository aja.

ok, lalu kita ke permission2 nya, pertama2 pakai akun root, tldr

```sh
cd /root
mkdir git
cd git
mkdir user1, misal aja mkdir fadhil_riyanto
cd fadhil_riyanto
```


clone git apapun disini, misal 
`git clone https://github.com/fadhil-riyanto/reponame.git --bare` (harus pakai bare)

posisi dir ini di `/root/git/fadhil-riyanto/reponame.git`

ok, balik ke parent dir, posisi di /root/git
lakukan `chown -R fadhil_riyanto fadhil-riyanto`, jika engga nanti error "git submodule update" failed with 'fatal: detected dubious ownership in repository at...' etc...

ok, saatnya push
`git remote add cgit fadhil_riyanto@123.123.111.222:/root/git/fadhil-riyanto/reponame.git`