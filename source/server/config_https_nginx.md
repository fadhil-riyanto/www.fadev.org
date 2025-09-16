# config HTTPS nginx

Cara config HTTPS di server pakai certbot (NGINX)

- apt install certbot python3-certbot-nginx 
- verify config na pakai nginx -t
- generate cert na pakai certbot --nginx -d namasite.com

ganti namasite.com dengan embel2 di /etc/nginx/sites-enabled/somefile.conf

didalamnya kan ada server_name, nah diganti dgn itu