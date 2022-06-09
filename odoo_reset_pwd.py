import datetime
from passlib.context import CryptContext
import psycopg2
from datetime import datetime as date

class PassError(Exception):
    """
    passwords not the same
    """

    def __str__(self):
        return 'not the same typed passwords'

print("===="*30)

print("\n")

adress = str(input("postgres address (type enter if default)"))
port = str(input("postgres password (type enter if default)"))

username = str(input("Username (type enter for 'newadmin'):"))

password = str(input("new password : "))
password2 = str(input("confirm new password :"))

firstname = str(input("firstname :"))
lastname = str(input("lastname :"))


if password == password2 :
    pass
else :
    raise PassError

passwd = CryptContext(['pbkdf2_sha512']).encrypt('password')

try:
    connection = psycopg2.connect(user="openpg",password="openpgpwd",host="127.0.0.1",port="5432",database="odoo")
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO res_users (active, login,password,company_id,partner_id,create_date,signature,share,notification_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    record_to_insert = ('true', username, passwd,1, 1, date.now(),'<span data-o-mail-quote="1">-- <br data-o-mail-quote="1">{} {}</span>'.format(firstname,lastname), 'false', "email")
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()
    count = cursor.rowcount
    print (count, "username and password all set")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert password", error)