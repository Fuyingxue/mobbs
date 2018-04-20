#bbs

# #####安装软件
sudo apt-get install python3-pip git python3-setuptools supervisor nginx redis-server supervisor mysql

sudo pip3 install flask gunicorn redis gevent python-redis pycrypto pymongo pymysql flask-sqlalchemy

# 在app所在文件配置如下
       bbs.nginx
       bbs.conf
       mongod.conf
       gunicorn.config.py


# #####配置HTTP服务器  nginx反向代理配置(bbs.nginx)
# 删掉默认网站配置
sudo rm /etc/nginx/sites-enabled/default
# 将本文件的bbs.nigx 软连接到特定目录
sudo ln -s /home/mobbs/bbs.nginx /etc/nginx/sites-enabled/mobbs
# 运行
sudo service nginx restart

# #####配置web服务器(gunicorn.config.py)


# #####配置监控程序supervisor(bbs.conf )
# 将本文件的bbs.conf 软连接到特定目录
sudo ln -s /home/mobbs/bbs.conf /etc/supervisor/conf.d/bbs.conf
# 运行
sudo service supervisor restart

# #####配置mongo(mongod.conf)