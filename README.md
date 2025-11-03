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