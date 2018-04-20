#bbs
sudo apt-get install python3-pip git python3-setuptools supervisor nginx redis-server supervisor mysql

sudo pip3 install flask  gunicorn redis gevent python-redis pycrypto pymongo flask-sqlalchemy pymysql 


sudo ln -s /home/mobbs/bbs.conf /etc/supervisor/conf.d/bbs.conf
sudo service supervisor restart

nginx 反向代理配置
# 删掉默认网站配置
sudo rm /etc/nginx/sites-enabled/default
# 增加自己的网站
sudo ln -s /home/mobbs/bbs.nginx /etc/nginx/sites-enabled/mobbs
sudo service nginx restart

sudo service supervisor restart