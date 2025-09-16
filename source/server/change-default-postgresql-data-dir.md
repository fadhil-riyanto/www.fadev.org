# change default postgresql data dir

- first, you need root account
- identify your service file. by running `systemctl status postgresql`

![image](../_images/26366e59db755f52e6b47a512d0b02f8f0229c69643449cc81876f3eceed3d217e2001232f22e2696250f163e0f0289f7c0e590cd4f9085268a6ff2f.png)

in my case, `/usr/lib/systemd/system/postgresql.service` is the service file

- editing
	- `mkdir /home/postgres`
	- `chown -R postgres:postgres /home/postgres`
	- edit `Environment=PGROOT=/home/postgres` and `ProtectHome=false`
	- run `systemctl daemon-reload && sudo systemctl restart postgresql && sudo systemctl status postgresql`

	