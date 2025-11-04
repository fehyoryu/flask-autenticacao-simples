# flask-autenticacao-simples


Estudo de API de autenticação com banco de dados


Até o commit atual, foi necessário criar o banco de dados usando o flask shell em um terminal

```cmd
flask shell
>> db.create_all()
>> db.session.commit()
>> exit()
```

com isso, foi criado o database na pasta **instance**

Nesse commit de teste de login, foi usado novamente o flask shell para fazer o cadastro de um usuário no banco de dados SQLite e testar a rota /login

```
user = User(username="admin", password="123456")
db.session.add(user)
db.session.commit()
exit()
```