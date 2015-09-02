from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

def main():
    database_name = "test"
    # creation of database if neccessary
    engine = create_engine("mysql://root:root@127.0.0.1/%s" % database_name)
    if not database_exists(engine.url):
        create_database(engine.url)

    connection = engine.connect()
    table_name = "TABLE_NAME_1"
    create_table_sql = "CREATE TABLE %s ( id INT PRIMARY KEY NOT NULL, nom VARCHAR(100), prenom VARCHAR(100), email VARCHAR(255), date_naissance DATE, pays VARCHAR(255), ville VARCHAR(255), code_postal VARCHAR(5), nombre_achat INT)" % table_name
    connection.execute(create_table_sql)


if __name__:
    main()
