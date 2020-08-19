#!/usr/bin/env bash
# Set up web server for deployment of web_static
apt-get -y update
apt-get install nginx
ufw allow 'Nginx HTTP'
ufw enable
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
    <head>
        <title>Andres Interactive</title>
    </head>
    <body>
        <h1>Holberton School is cool!</h1>
    </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-available/default
service nginx restart
