Publishers for sensors data. This scripts send data to a database.

requirements/system installation: 

pip install sqlalchemy
pip install sqlalchemy_utils
pip install mysql-python


fichier de conf de mysql
/etc/mysql/my.cnf


on remplace 
bind-address            = 127.0.0.1

par 
bind-address            = 10.0.160.3


puis restart mysql : 
sudo /etc/init.d/mysql restart


bon ca n'est pas suffisant il faut autoriser la connection distante à regarder plus tard. TODO


# autorisation des privilege pour une ip
dans /etc/mysql/my.cnf commenter la ligne bind-address
GRANT ALL PRIVILEGES ON *.* TO 'root'@'10.0.164.118' IDENTIFIED BY 'PASSWORD' WITH GRANT OPTION;