# systemd config template

root location: `/etc/systemd/system/<YOUR_SERVICE>.service`

template
```
[Unit]
Description=Random service
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
ExecStart=/usr/bin/randomprogram -c /etc/randomprogram/other.toml

[Install]
WantedBy=multi-user.target
```