import pymongo
from datetime import datetime

def day_atual():
  day_atual = datetime.datetime.now()
  return day_atual

client = pymongo.MongoClient("mongodb+srv://xateja1315:RuCDQA2XygABGgvv@irisbot.h6ev71v.mongodb.net/bot")
db = client.bot
coll_users = db.users
coll_contas = db.contas

def adicionar_conta(email, senha, conta):
  add = coll_contas.insert_one({
    "email": email,
    "senha": senha,
    "conta": f"{conta}-conta"
  })
  
  if add:
    return True
  else:
    return False
  
def adicionar_tela(email, senha, pin, nome, tela):
  add = coll_contas.insert_one({
    "email": email,
    "senha": senha,
    "pin": pin,
    "nome": nome,
    "conta": f"{tela}-tela"
  })
  
  if add:
    return True
  else:
    return False

def verificar_call(id_clicado, id_usuario):
  if id_clicado == id_usuario:
    ...
  else:
    return False

def verificar_admin(chat_id):
  admin = coll_users.find_one({
    'chat_id': chat_id
  })

  if admin["isAdmin"] == True:
    return True
  else:
    return False

def verificar_existe(chat_id):
  email_exists = coll_users.find_one({
    'chat_id': chat_id.id,
  })

  if email_exists == None:
    email_exists = coll_users.insert_one({
      'chat_id': chat_id.id,
      'nome': chat_id.first_name,
      'username': chat_id.username,
      'isAdmin': False,
      'saldo': 0,
      'registro': datetime.today().strftime('%d/%m/%Y')
    })

    return 0
  else:
    return email_exists["saldo"]
