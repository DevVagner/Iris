import time, json, os, requests, random, mercadopago, telebot, uuid
from markups import *
import random
from buscando_dados import *
from gerar_pagamento import *
from bson.objectid import ObjectId
import os
import csv

giftcard = uuid.uuid4()

client = pymongo.MongoClient("mongodb+srv://xateja1315:RuCDQA2XygABGgvv@irisbot.h6ev71v.mongodb.net/bot")
db = client.bot
coll_users = db.users
coll_prices = db.prices
coll_contas = db.contas
coll_config = db.config
coll_gifts = db.gifts

tipo_conta = ""
tipo_tela = ""
conta_selecionada = ""
listar = ""
alterar = ""
plataforma_selecionada = ""
saldo = ""
valor = ""
registado = False

with open('config/config.json', 'r') as file:
  config = json.loads(file.read())
  token = config['token']
  user = config['userAdmin']
  idAdmin = config['admin']

def gerar_id():
  return random.randint(0, 50000)


def notificar_recarga(id_ta, valor, user):
    bot.send_message(idAdmin, f"""
    🎁 Recarga Pix realizada

Id da transação: {id_ta}
Valor: R${valor},00
Usuário: @{user}
""", parse_mode="HTML")

def notificar_compra_conta(tipo, valor, user, conta, senha):
    bot.send_message(idAdmin, f"""
    🎁 Conta Comprada

Plataforma: {tipo}
Conta: {conta}:{senha}
Valor: R${valor},00
Usuário: @{user}

""", parse_mode="HTML")


bot = telebot.TeleBot(token)

def notificar_compra_tela(tipo, valor, user, conta, senha, pin, nome):
    bot.send_message(idAdmin, f"""
    🎁 Conta Comprada

Plataforma: {tipo}
Conta: {conta}:{senha}:{pin}:{nome}
Valor: R${valor},00
Usuário: @{user}

""", parse_mode="HTML")


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['photo'])
def photo(message):
  if message.chat.type == "private":
     if verificar_admin(message.from_user.id) == True:
        raw = message.photo[2].file_id
        path = raw+".jpg"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(path,'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, """Enviando mensagem 📥
""")
        cursor.execute("SELECT chat_id FROM usuarios")
        captio = message.caption
        for lista in cursor.fetchall():
            for s3 in lista:
                with open(path, "rb") as s2:
                    if captio == None:
                        captio = ""
                        s=requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={s3}&caption={captio}", files={'photo': s2})
                    else:
                        s=requests.post(f"https://api.telegram.org/bot{token}/sendPhoto?chat_id={s3}&caption={captio}&parse_mode=MARKDOWN", files={'photo': s2})
 
@bot.callback_query_handler(func=lambda call: call.data == "admin")
def admin(call):
  if verificar_admin(call.message.chat.id) == True:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
*⚙️ PAINEL ADMINISTRATIVO*

_• Comandos do Admin:_
 
`/send` *- NOTIFICAR USUÁRIOS*
`/gift` *- GERAR GIFT*
`/apagar` *- APAGA UMA OU VÁRIAS CONTAS DO ESTOQUE*
`/info @` *- MOSTRA AS INFORMAÇÕES DO CLIENTE*
""", reply_markup=adminOptions, parse_mode="MARKDOWN")
      

@bot.message_handler(commands=['infor'])
def info(message):
  if verificar_admin(message.from_user.id) == True:
    if message.text == "/infor":
       bot.send_message(message.chat.id, """
         * 👤 Veja as informações
         
Modo de uso:* `/infor id de usuário`
          """, parse_mode="MARKDOWN")
    else:
        chat_id = message.text.split("/infor ")[1]
        verificar_existe(int(chat_id))
        bot.send_message(message.chat.id, f"""
        🔍 *USUÁRIO ENCONTRADO

- ID: {chat_id}
- SALDO: {saldo(int(chat_id))}
- COMPRAS: {compras(int(chat_id))}*
          """, parse_mode="MARKDOWN")
        
        
@bot.message_handler(commands=['send'])
def notificar(message):
  if verificar_admin(message.from_user.id) == True:
    if message.text == "/send":
      bot.send_message(message.chat.id, """
      *📣 Envie uma mensagem para todos os usuários registrados no bot.

Ex:* _/send + a mensagem que deseja enviar_
      """, parse_mode="MARKDOWN")
    else:
      MSG = message.text.split("/send ")[1]
      bot.send_message(message.chat.id, "Enviando mensagem 📥")
      
      findUsers = coll_users.find({})
      for user in findUsers:
        s=requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={user[user['chat_id']]}&text={MSG}&parse_mode=MARKDOWN")


@bot.message_handler(commands=['gift'])
def gerar_gift(message):
  if verificar_admin(message.from_user.id) == True:
    if message.text == "/gift":
      bot.send_message(message.chat.id, """
      *💵 Gere um gift card para o usuário resgatar.*

*Ex:* `/gerar` _+ valor que deseja adicionar_
      """, parse_mode="MARKDOWN")
    else:
      VALOR = int(message.text.split("/gift ")[1])

      gift = ''

      while True:
        for _ in range(4):
          words = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=4))
          gift += words + '_'

        findGift = coll_gifts.find_one({"codigo_gift": gift[:-1]})

        print(findGift)

        if findGift:
          continue
        else:
          break

      coll_gifts.insert_one({"codigo_gift": gift[:-1], "valor": VALOR, "usado": False})
      bot.send_message(message.chat.id, f"""
    ✅ GIFT R${VALOR} GERADO

🎁 `/resgatar {gift[:-1]}`
""", parse_mode="MARKDOWN")
  else:
    bot.send_message(message.chat.id, "*Você não possui autorização!*", parse_mode="MARKDOWN")

@bot.message_handler(commands=['resgatar'])
def resgatar_gitf(message):
      verificar_existe(message.from_user)
      if message.text == "/resgatar":
        bot.send_message(message.chat.id, """
  🏷 *De o comando /resgatar + o gift a ser resgatado.*
  """, parse_mode="MARKDOWN")
          
      else:
          gift_enviado = message.text.split("/resgatar ")[1]
          try:  
              find = coll_gifts.find_one({"codigo_gift": gift_enviado, "usado": False})

              if find:
                findUser = coll_users.find_one({"chat_id": message.chat.id})

                updateUser = coll_users.find_one_and_update(
                  {"chat_id": message.chat.id},
                  {"$set": {"saldo": int(findUser["saldo"]) + int(find["valor"])}}
                )

                if updateUser:
                  find = coll_gifts.find_one_and_delete({"codigo_gift": gift_enviado})

                  findUser = coll_users.find_one({"chat_id": message.chat.id})

                  bot.send_message(message.chat.id, f"""
                    💳 Gift Resgatado

Valor: R${find["valor"]}
Id: {message.from_user.id}
Usuário: {message.from_user.username}

Saldo atual: R${findUser["saldo"]}
  """, parse_mode="HTML")
                else:
                  bot.send_message(message.chat.id,"*NÃO É POSSÍVEL RESGATAR NO MOMENTO.*", parse_mode="MARKDOWN")
                  
              else:
                bot.send_message(message.chat.id,"❗️*GIFT CARD INVÁLIDO OU JÁ RESGATADO.*", parse_mode="MARKDOWN")
          except:
              bot.send_message(message.chat.id,"❗️*ESSE GIFT CARD É ÍNVALIDO, ADICIONE SALDO NO BOT E PEÇA PARA O DONO GERAR UM GIFT PARA VOCÊ.*", parse_mode="MARKDOWN")

@bot.message_handler(commands=['dimn'])
def diminuir_slo(message):
  if verificar_admin(message.from_user.id) == True:
      if message.text == "/dimn":
          bot.send_message(message.chat.id, """
          *➖ Diminuir saldo

Modo de usar:* `/dimn` *id de usuário|quantidade para diminuir*
   """, parse_mode="MARKDOWN")
      else:
          texto = message.text.split("/dimn ")[1]
          chat = texto.split("|")[0]
          s = texto.split("|")[1]
          s2 = saldo(int(chat)) - int(s)
          diminuir_saldo(int(chat), s2)
          bot.send_message(message.chat.id, "Saldo Diminuído!")


@bot.message_handler(commands=['start'])
def start(message):
  global saldo

  saldoUser = verificar_existe(message.from_user)

  if verificar_admin(message.from_user.id):
      bot.send_message(message.chat.id, f"""
  *⭐ Olá {message.from_user.first_name}, seja bem vindo(a) a *melhor store de Contas Premium/Logins.

  ➡️ LEIA COM ATENÇÃO⤵️

  ➡️ Antes de adicionar saldo verifique se o que deseja comprar está disponível! Não fazemos reembolso.

  ➡️ Se a conta que você deseja não estiver disponível entre em contato com o suporte.

  _➤ Informações:_
  *├ ID:* `{message.from_user.id}`
  *└💰 Saldo:* `R${saldoUser}`
          """, reply_markup=inicioAdmin, parse_mode="MARKDOWN")
  else:
      bot.send_message(message.chat.id, f"""
  *⭐ Olá {message.from_user.first_name}, seja bem vindo(a) a *melhor store de Contas Premium/Logins.

  ➡️ LEIA COM ATENÇÃO⤵️

  ➡️ Antes de adicionar saldo verifique se o que deseja comprar está disponível! Não fazemos reembolso.

  ➡️ Se a conta que você deseja não estiver disponível entre em contato com o suporte.

  _➤ Informações:_
  *├ ID:* `{message.from_user.id}`
  *└💰 Saldo:* `R${saldoUser}`
          """, reply_markup=inicio2, parse_mode="MARKDOWN")


@bot.message_handler(commands=['pix'])
def recarga_pix(message):
  if message.text == "/pix":
    bot.send_message(message.chat.id, "*Digite /pix + o valor que deseja.*", parse_mode="MARKDOWN")
  else:
    try:
      tipoPagamento = coll_config.find_one({"atual": {"$in": ["mercadopago", "manual"]}})

      if tipoPagamento["atual"] == "mercadopago":
        pag = coll_config.find_one({"tipo": "mercadopago"})

        if pag:
          VALOR = message.text.split("/pix ")[1]
          id_pix = gerar_pagamento(int(VALOR), pag['token'])[0]

          headers = {"Authorization": f"Bearer {pag['token']}"}
          request = requests.get(f'https://api.mercadopago.com/v1/payments/{id_pix}', headers=headers)
          response = request.json()
          pix = response['point_of_interaction']['transaction_data']['qr_code']
          msg = bot.send_message(message.chat.id, f"""
        *✅ PAGAMENTO GERADO

    ℹ️  ID DO PAGAMENTO:* `{id_pix}`
    *ℹ️  PIX COPIA E COLA:* `{pix}`
    *ℹ️  A COMPRA IRÁ EXPIRAR EM 5 MINUTOS.
    ℹ️  DEPOIS DO PAGAMENTO SEU SALDO SERÁ ADICIONADO AUTOMÁTICAMENTE.*""",
      reply_markup=aguardando, parse_mode="MARKDOWN")
          
          if status(id_pix, pag['token']) == True:
            findUser = coll_users.find_one({"chat_id": message.chat.id})

            updateSaldo = coll_users.find_one_and_update({"chat_id": message.chat.id}, {"$set": {"saldo": int(findUser["saldo"]) + int(VALOR)}})

            if updateSaldo:
              bot.send_message(message.chat.id, "*✅ PAGAMENTO APROVADO!!! SEU SALDO JÁ ESTÁ DISPONÍVEL.*", parse_mode="MARKDOWN")
              notificar_recarga(id_pix, VALOR, message.from_user.username)
          else:
            bot.send_message(message.chat.id, "*O PAGAMENTO FOI EXPIRADO.*", parse_mode="MARKDOWN")
        else:
          bot.send_message(message.chat.id, "*Não foi possível adicionar saldo.*", parse_mode="MARKDOWN")
      elif tipoPagamento["atual"] == "manual":
        pag = coll_config.find_one({"tipo": "manual"})

        VALOR = message.text.split("/pix ")[1]

        msg = bot.send_message(message.chat.id, f"""
      *✅ PAGAMENTO GERADO

  *ℹ️  NOME DA CONTA:* `{pag["nome"]}`
  *ℹ️  PIX:* `{pag["chave"]}`
  *ℹ️  VALOR:* `{VALOR}`

  ℹ️  DEPOIS DO PAGAMENTO, ENVIE O COMPROVANTE PARA @{user}*""", parse_mode="MARKDOWN")
      else:
        bot.send_message(message.chat.id, "*Não foi possível adicionar saldo, nenhuma chave cadastrada pelo administrador.*", parse_mode="MARKDOWN")
    except:
      bot.send_message(message.chat.id, "*Não foi possível adicionar saldo.*", parse_mode="MARKDOWN")
      
@bot.callback_query_handler(func=lambda call: call.data == "net")
def net_call(call):
  bot.answer_callback_query(callback_query_id=call.id , text="Em manutenção.", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "resgatar")
def resgatar(call):
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""
        🏷 *De o comando /resgatar + o gift a ser resgatado.* 
                """, parse_mode="MARKDOWN", reply_markup=i)
      

@bot.callback_query_handler(func=lambda call: call.data.startswith("pre-compra"))
def preCompra(call):
  global plataforma_selecionada

  plataforma = call.data.split("-")[2]

  find_qtd_contas = coll_contas.count_documents({"conta": f"{plataforma}-conta"})
  find_qtd_telas = coll_contas.count_documents({"conta": f"{plataforma}-tela"})

  if find_qtd_telas >= 1 and find_qtd_contas >= 1:
    plataforma_selecionada = plataforma

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""Selecione uma opção:

  *Quantidade de contas disponíveis:*
  {find_qtd_contas} conta(s)
                                              
  *Quantidade de telas disponíveis:*
  {find_qtd_telas} tela(s)
                                                  
  """, reply_markup=compraOpts, parse_mode="MARKDOWN")
  elif find_qtd_contas >= 1:
    plataforma_selecionada = plataforma

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""Selecione uma opção:

  *Quantidade de contas disponíveis:*
  {find_qtd_contas} conta(s)
                                              
  *Quantidade de telas disponíveis:*
  {find_qtd_telas} tela(s)
                                                  
  """, reply_markup=compraOpts2, parse_mode="MARKDOWN")
  elif find_qtd_telas >= 1:
    plataforma_selecionada = plataforma

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""Selecione uma opção:

  *Quantidade de contas disponíveis:*
  {find_qtd_contas} conta(s)
                                              
  *Quantidade de telas disponíveis:*
  {find_qtd_telas} tela(s)
                                                  
  """, reply_markup=compraOpts3, parse_mode="MARKDOWN")
  else:
    bot.send_message(call.message.chat.id, text=f"""⚠️ Não há contas disponíveis""", parse_mode="MARKDOWN")


@bot.callback_query_handler(func=lambda call: call.data == "comprar-conta")
def conta(call):
  global plataforma_selecionada, saldo, valor

  saldoUser = coll_users.find_one({"chat_id": call.message.chat.id})
  valorConta = coll_prices.find_one({"tipo": plataforma_selecionada + "-conta"})

  saldo = saldoUser["saldo"]
  valor = valorConta["valor"]
  plataforma_selecionada = plataforma_selecionada + "-conta"

  if saldoUser and valorConta:
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""Comprar conta:

*Valor:*
💵 R${valorConta["valor"]},00

*Seu saldo:*
💰 R${saldoUser["saldo"]},00""", reply_markup=confirmarCompra, parse_mode="MARKDOWN")
    

@bot.callback_query_handler(func=lambda call: call.data == "comprar-tela")
def tela(call):
  global plataforma_selecionada, saldo, valor

  saldoUser = coll_users.find_one({"chat_id": call.message.chat.id})
  valorTela = coll_prices.find_one({"tipo": plataforma_selecionada + "-tela"})

  saldo = saldoUser["saldo"]
  valor = valorTela["valor"]
  plataforma_selecionada = plataforma_selecionada + "-tela"

  if saldoUser and valorTela:
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""*Comprar tela:*

*Valor:*
💵 R${valorTela["valor"]},00

*Seu saldo:*
💰 R${saldoUser["saldo"]},00""", reply_markup=confirmarCompra, parse_mode="MARKDOWN")
    

@bot.callback_query_handler(func=lambda call: call.data == "confirmar-compra")
def confirmar(call):
  global plataforma_selecionada, saldo, valor

  tipo = plataforma_selecionada.split("-")[1]

  if int(saldo) >= int(valor):
    user = coll_users.find_one({"chat_id": call.message.chat.id})

    if tipo == "conta":
      conta = coll_contas.find_one_and_delete({"conta": plataforma_selecionada})

      if conta:
        notificar_compra_conta(plataforma_selecionada, valor, user["username"], conta["email"], conta["senha"])

        saldoAtualizado = coll_users.find_one_and_update({"chat_id": call.message.chat.id}, {"$set": {"saldo": int(saldo) - int(valor)}})

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""*✅ Compra realizada com sucesso!*

⚠️ REGRAS ⚠️

❌ NÃO MUDAR EMAIL
❌ NÃO MUDAR SENHA

⚠️ CASO DESCUMPRIR UMA DAS REGRAS ACIMA IRÁ PERDER SUPORTE E NÃO TERÁ REEMBOLSO ⚠️

> Prazo para suporte: 24h a 48h

◆ ━━━━❪✪❫━━━━ ◆

📧 Email: {conta["email"]}
🔑 Senha: {conta["senha"]}

*Saldo atualizado:*
💰 R${int(user["saldo"]) - int(valor)},00""", parse_mode="MARKDOWN")
        
    elif tipo == "tela":
      conta = coll_contas.find_one_and_delete({"conta": plataforma_selecionada})

      if conta:
        notificar_compra_tela(plataforma_selecionada, valor, user["username"], conta["email"], conta["senha"], conta["pin"], conta["nome"])

        saldoAtualizado = coll_users.find_one_and_update({"chat_id": call.message.chat.id}, {"$set": {"saldo": int(saldo) - int(valor)}})

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""*✅ Compra realizada com sucesso!*

⚠️ REGRAS ⚠️

❌ NÃO MUDAR EMAIL
❌ NÃO MUDAR SENHA

⚠️ CASO DESCUMPRIR UMA DAS REGRAS ACIMA IRÁ PERDER SUPORTE E NÃO TERÁ REEMBOLSO ⚠️

> Prazo para suporte: 24h a 48h

◆ ━━━━❪✪❫━━━━ ◆

📧 Email: {conta["email"]}
🔑 Senha: {conta["senha"]}
👤 Nome: {conta["nome"]}
🔒 Pin: {conta["pin"]}

*Saldo atualizado:*
💰 R${int(user["saldo"]) - int(valor)},00""", parse_mode="MARKDOWN")
  else:
    bot.send_message(call.message.chat.id, "❌ Saldo insuficiente")
    
  

def alterarValorConta(message):
  global alterar

  valor = message.text

  if int(valor):
    updatePrice = coll_prices.find_one_and_update({"tipo": f"{alterar}-conta"}, {"$set": {"valor": int(valor)}})

    if updatePrice:
      bot.send_message(message.chat.id, "Valor alterado com sucesso!")
      alterar = ''
    else:
      bot.send_message(message.chat.id, "Ocorreu um erro ao alterar o valor!")
  else:
    bot.send_message(message.chat.id, "Valor incorreto.")


def alterarValorTela(message):
  global alterar

  valor = message.text

  if int(valor):
    updatePrice = coll_prices.find_one_and_update({"tipo": f"{alterar}-tela"}, {"$set": {"valor": int(valor)}})

    print(updatePrice)

    if updatePrice:
      bot.send_message(message.chat.id, "Valor alterado com sucesso!")
      alterar = ''
    else:
      bot.send_message(message.chat.id, "Ocorreu um erro ao alterar o valor!")
  else:
    bot.send_message(message.chat.id, "Valor incorreto.")
  
@bot.callback_query_handler(func=lambda call: call.data.startswith("alterar-conta"))
def alterarConta(call):
  global alterar

  conta = call.data.split("-")[2]
  alterar = conta

  msg = bot.send_message(call.message.chat.id , "Insira o valor:")

  bot.register_next_step_handler(msg, alterarValorConta)


@bot.callback_query_handler(func=lambda call: call.data.startswith("alterar-tela"))
def alterarTela(call):
  global alterar

  conta = call.data.split("-")[2]
  alterar = conta

  msg = bot.send_message(call.message.chat.id , "Insira o valor:")

  bot.register_next_step_handler(msg, alterarValorTela)
  

@bot.callback_query_handler(func=lambda call: call.data == "alterar-valores")
def alterar(call):
  if verificar_admin(call.message.chat.id):
    bot.send_message(call.message.chat.id, "Selecione uma opção:", reply_markup=alterarOpts)
  else:
    bot.send_message(call.message.chat.id, "Você não tem permissão para isso.")


@bot.callback_query_handler(func=lambda call: call.data == "estoque")
def listarEstoque(call):
  if verificar_admin(call.message.chat.id):
    bot.send_message(call.message.chat.id , "📄 Listar estoque:", reply_markup=estoqueOpts)
  else:
    bot.send_message(call.message.chat.id, "Não foi possível listar o estoque!")
    
     
@bot.callback_query_handler(func=lambda call: call.data == "tidal")
def tidal(call):
      if int(tidal_quant()) == 0:
          bot.answer_callback_query(callback_query_id=call.id , text="Não possuimos estoque no momento ou não possuimos todas as contas.", show_alert=True)
      else:
          if saldo(call.from_user.id) >= VALOR('tidal'):
              compras_ajustadas = compras(call.from_user.id) + 1
              saldo_ajustado = saldo(call.from_user.id) - VALOR('tidal')
              time.sleep(2)
              bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""
                ✅ *Compra efetuada com sucesso*
    
📧 *E-mail:* `{email('tidal')}`
🔒 *Senha:* `{senha('tidal')}`
📥 *Conta:* Tidal Hifi
📆 *Validade:* 30 Dias
🆘 *Suporte:* 24 Horas apartir da compra
⚙️ *Id da compra:* {gerar_id()}
    
❌_Não responsabilizaremos pela perda da conta ou troca de senha. Até porque não trocamos senha de nenhuma conta._
                """, reply_markup=cc_comp(call.from_user.id),parse_mode="MARKDOWN")
              delete_conta(email('tidal'))
              update(saldo_ajustado, compras_ajustadas, call.from_user.id)
              notificar_compra("Tidal Hifi", VALOR('tidal'), call.from_user.first_name)
          else:
              bot.answer_callback_query(callback_query_id=call.id , text="Você não possui saldo suficiente, recarregue na store.", show_alert=True)

      
@bot.callback_query_handler(func=lambda call: call.data == "comprar")
def comprar(call):
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""*🔎 Escolha uma das opções a seguir:
                        *""", reply_markup=comprar2, parse_mode="MARKDOWN")


@bot.callback_query_handler(func=lambda call: call.data == "back_comprar")
def back_comprar(call):
  saldoUser = verificar_existe(call.message.from_user)

  if verificar_admin(call.message.chat.id):
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""
  *⭐ Olá, seja bem vindo(a) a *melhor store de Contas Premium/Logins.

  ➡️ LEIA COM ATENÇÃO⤵️

  ➡️ Antes de adicionar saldo verifique se o que deseja comprar está disponível! Não fazemos reembolso.

  ➡️ Se a conta que você deseja não estiver disponível entre em contato com o suporte.

  _➤ Informações:_
  *├ ID:* `{call.message.from_user.id}`
  *└💰 Saldo:* `R${saldoUser}`
          """, reply_markup=inicioAdmin, parse_mode="MARKDOWN")
  else:
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""
  *⭐ Olá, seja bem vindo(a) a *melhor store de Contas Premium/Logins.

  ➡️ LEIA COM ATENÇÃO⤵️

  ➡️ Antes de adicionar saldo verifique se o que deseja comprar está disponível! Não fazemos reembolso.

  ➡️ Se a conta que você deseja não estiver disponível entre em contato com o suporte.

  _➤ Informações:_
  *├ ID:* `{call.message.from_user.id}`
  *└💰 Saldo:* `R${saldoUser}`
          """, reply_markup=inicio2, parse_mode="MARKDOWN")
      

@bot.callback_query_handler(func=lambda call: call.data == "contas_premium")
def conta_premium(call):
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""
	*Escolha uma categoria abaixo e verifique a disponibilidade em nosso estoque:*
	 """, parse_mode="MARKDOWN",reply_markup=contasOpts)
                
@bot.callback_query_handler(func=lambda call: call.data == "recarregar")
def recarregar(call):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""
💵 _Adição de Saldo_
    
*• Modo de Usar:*
*Digite o comando* /pix *+ o valor que deseja adicionar*

*Pode ser qualquer valor! Caso aconteça algum erro fale com o dono*""", parse_mode="MARKDOWN",reply_markup=i)

@bot.callback_query_handler(func=lambda call: call.data == "informacion")
def informacion(call):
  user = coll_users.find_one({
    "chat_id": call.from_user.id
  })

  if user:
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=f"""
    📃 *Informações

  Meu perfil ➺
  ✦ ID: {call.from_user.id}
  ✦ USUÁRIO: @{call.from_user.username}

  Carteira ➺
  ✦ SALDO: R${user["saldo"]}
  ✦ RESGISTRADO EM: {user["registro"]}
  *
          """, parse_mode="MARKDOWN", reply_markup=i)
  else:
    bot.send_message(call.from_user.id, "Cadastro não encontrado")


def pagauto(message):
  if verificar_admin(message.chat.id):
    try:
      app = message.text.split(":")[0]
      token = message.text.split(":")[1]

      updateConfig = coll_config.find_one_and_update({"tipo": f"mercadopago"}, {"$set": {"public": app, "token": token}})

      if updateConfig:
        bot.send_message(message.chat.id, "✅ Dados atualizados com sucesso")
      else:
        bot.send_message(message.chat.id, "❌ Não foi possível atualizar os dados")
    except:
      bot.send_message(message.chat.id, "Dados incorretos")


def pagmanual(message):
  if verificar_admin(message.chat.id):
    try:
      nome = message.text.split(":")[0]
      chave = message.text.split(":")[1]

      updateConfig = coll_config.find_one_and_update({"tipo": f"manual"}, {"$set": {"nome": nome, "chave": chave}})

      if updateConfig:
        bot.send_message(message.chat.id, "✅ Dados atualizados com sucesso")
      else:
        bot.send_message(message.chat.id, "❌ Não foi possível atualizar os dados")
    except:
      bot.send_message(message.chat.id, "Dados incorretos")
    

@bot.callback_query_handler(func=lambda call: call.data == "pagamentos")
def pagamentos(call):
  bot.send_message(call.message.chat.id , "Selecione uma opção para configurar o pagamento:", reply_markup=pagamentosOpts)


@bot.callback_query_handler(func=lambda call: call.data == "pag-automatico")
def automatico(call):
  msg = bot.send_message(call.message.chat.id , '''Digite os dados no seguinte formato:
  
MERCADO_PUBLIC:MERCADO_TOKEN

Exemplo:
APP_USR-b150cad6-8ecf:APP_USR-65292187238133...

  ''')

  bot.register_next_step_handler(msg, pagauto)


@bot.callback_query_handler(func=lambda call: call.data == "pag-manual")
def automatico(call):
  msg = bot.send_message(call.message.chat.id , '''Digite os dados no seguinte formato:
  
NOME DA CONTA:CHAVE PIX

  ''')

  bot.register_next_step_handler(msg, pagmanual)


@bot.callback_query_handler(func=lambda call: call.data == "usuarios")
def usuarios(call):
  lista = coll_users.find({})
  total_usuarios = coll_users.count_documents({})

  arquivo = "usuarios.txt"

  with open(arquivo, 'w', encoding='utf-8') as arq:
    arq.write(f"👤 Total de usuários: {total_usuarios}\n \n")

    for item in lista:
      arq.write(f"{item['chat_id']} - @{item['username']} - {item['nome']} - Saldo: R${item['saldo']} \n \n")

  bot.send_document(chat_id=call.message.chat.id, document=open(arquivo, 'rb'))

  os.remove(arquivo)


@bot.callback_query_handler(func=lambda call: call.data.startswith("listar-estoque"))
def baixarEstoque(call):
  if call.data == "baixar-estoque":
    bot.send_message(call.message.chat.id, "Selecione uma opção", reply_markup=baixarEstoque)
  else:
    conta = call.data.split('-')[2]
    tipo = call.data.split('-')[3]

    lista = coll_contas.find({"conta": f"{conta}-{tipo}"})
    total_contas = coll_contas.count_documents({"conta": f"{conta}-{tipo}"})

    arquivo = f"{conta}.txt"

    with open(arquivo, 'w', encoding='utf-8') as arq:
      arq.write(f"🍿 Total de contas cadastradas: {total_contas}\n \n")

      if tipo == "conta":
        for item in lista:
          arq.write(f"id: {item['_id']} - email: {item['email']} - senha: {item['senha']} - plataforma: {conta} \n \n")
      elif tipo == "tela":
        for item in lista:
          arq.write(f"id: {item['_id']} - email: {item['email']} - senha: {item['senha']} - pin: {item['pin']} - nome: {item['nome']} - plataforma: {conta} \n \n")

    bot.send_document(chat_id=call.message.chat.id, document=open(arquivo, 'rb'))

    os.remove(arquivo)


@bot.callback_query_handler(func=lambda call: call.data == "del-manual")
def deletarManual(call):
  delManual = coll_config.find_one_and_update({"tipo": f"manual"}, {"$set": {"nome": "", "chave": ""}})

  if (delManual):
    bot.send_message(call.message.chat.id , '✅ Informações deletadas do pagamento manual.')
  else:
    bot.send_message(call.message.chat.id , '❌ Informações deletadas do pagamento manual.')


@bot.callback_query_handler(func=lambda call: call.data == "del-auto")
def deletarAuto(call):
  delAuto = coll_config.find_one_and_update({"tipo": f"mercadopago"}, {"$set": {"public": "", "token": ""}})

  if (delAuto):
    bot.send_message(call.message.chat.id , '✅ Informações deletadas do pagamento automático.')
  else:
    bot.send_message(call.message.chat.id , '❌ Informações deletadas do pagamento automático.')


@bot.callback_query_handler(func=lambda call: call.data == "definir-pag-auto")
def defAuto(call):
  defPagamento = coll_config.find_one_and_update(
    {"atual": {"$in": ["mercadopago", "manual"]}},
    {"$set": {"atual": "mercadopago"}}
  )

  if (defPagamento):
    bot.send_message(call.message.chat.id , '✅ Pagamento automático definido com sucesso.')
  else:
    bot.send_message(call.message.chat.id , '❌ Erro ao definir o pagamento.')

  
@bot.callback_query_handler(func=lambda call: call.data == "definir-pag-manual")
def defManual(call):
  defPagamento = coll_config.find_one_and_update(
    {"atual": {"$in": ["mercadopago", "manual"]}},
    {"$set": {"atual": "manual"}}
  )

  if (defPagamento):
    bot.send_message(call.message.chat.id , '✅ Pagamento manual definido com sucesso.')
  else:
    bot.send_message(call.message.chat.id , '❌ Erro ao definir o pagamento.')


def add_conta(message):
  global registado

  try:
    repetidas = []

    contas = message.text.split("\n")

    global tipo_conta
    email = ''

    for conta in contas:
      email = conta.split(":")[0]
      senha = conta.split(":")[1]

      if {'email': email, "senha": senha} in repetidas:
        continue
      else:
        if adicionar_conta(email, senha, tipo_conta):
          repetidas.append({'email': email, "senha": senha})
        else:
          bot.send_message(message.chat.id, f"Não foi possível adicionar a conta. {email}")

    if len(repetidas) == 0:
      bot.send_message(message.chat.id, f"❌ Nenhuma conta adicionada no BOT", parse_mode="MARKDOWN")
    else:
      bot.send_message(message.chat.id, f"""🔥 {len(repetidas)} CONTA(S) {tipo_conta.upper()} ADICIONADA(S) AO BOT:
  """, parse_mode="MARKDOWN")
      
    registado = False
  except:
    registado = False
    bot.send_message(message.chat.id, f"❌ Formato inválido", parse_mode="MARKDOWN")
    
def add_tela(message):
  global registado

  try:
    repetidas = []
    telas = message.text.split("\n")
    global tipo_tela
    email = ''

    for tela in telas:
      email = tela.split(":")[0]
      senha = tela.split(":")[1]
      pin = tela.split(":")[2]
      nome = tela.split(":")[3]

      if {'email': email, "senha": senha, "pin": pin, "nome": nome} in repetidas:
        continue
      else:
        if adicionar_tela(email, senha, pin, nome, tipo_tela):
          repetidas.append({'email': email, "senha": senha, "pin": pin, "nome": nome})
        else:
          bot.send_message(message.chat.id, f"Não foi possível adicionar a tela. {email}")

    if len(repetidas) == 0:
      bot.send_message(message.chat.id, f"*❌ Nenhuma tela adicionada no BOT", parse_mode="MARKDOWN")
    else:
      bot.send_message(message.chat.id, f"""🔥 {len(repetidas)} TELA(S) {tipo_tela.upper()} ADICIONADA(S) AO BOT:
  """, parse_mode="MARKDOWN")
      
    registado = False
  except:
    registado = False
    bot.send_message(message.chat.id, f"❌ Formato inválido", parse_mode="MARKDOWN")
            
@bot.callback_query_handler(func=lambda call: call.data == "add-contas")
def addContas(call):
  bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Selecione o que deseja adicionar:", reply_markup=contas)


@bot.callback_query_handler(func=lambda call: call.data == "add-telas")
def addTelas(call):
  bot.send_message(call.message.chat.id , "Selecione o que deseja adicionar:", reply_markup=telas)


@bot.callback_query_handler(func=lambda call: call.data == "indisponivel")
def addTelas(call):
  bot.send_message(call.message.chat.id , "⚠️ Indisponível no momento")


@bot.callback_query_handler(func=lambda call: call.data.startswith("add-conta"))
def addConta(call):
  global tipo_conta, registado

  if registado == False:
    registado = True

    tipo_conta = call.data.split("-")[2]

    msg = bot.send_message(call.message.chat.id , '''Insira a(s) conta(s) no formato:

  Exemplo:

  email:senha
  email:senha
  email:senha

    ''')

    bot.register_next_step_handler(msg, add_conta)
  else:
    bot.send_message(call.message.chat.id, "Você já está registrando uma etapa.")


@bot.callback_query_handler(func=lambda call: call.data.startswith("add-tela"))
def addTela(call):
  global tipo_tela, registado

  if registado == False:
    registado = True

    tipo_tela = call.data.split("-")[2]

    msg = bot.send_message(call.message.chat.id , '''Insira a(s) telas(s) no formato:

  Exemplo:

  email:senha:pin:nome
  email:senha:pin:nome
  email:senha:pin:nome

    ''')

    bot.register_next_step_handler(msg, add_tela)
  else:
    bot.send_message(call.message.chat.id, "Você já está registrando uma etapa.")


@bot.message_handler(commands=['apagar'])
def apagar(message):
  if message.text == "/apagar":
    bot.send_message(message.chat.id, '''Para apagar uma ou várias contas, utilize o exemplo:

Apagar uma conta:
/apagar ID    

Apagar várias:
/apagar ID, ID, ID
''')
  else:
    msg = message.text.split("/apagar ")[1]
    
    apagadas = []
    ids = msg.split(",")

    for idConta in ids:
      deletar = coll_contas.find_one_and_delete({"_id": ObjectId(idConta.strip())})

      if deletar:
        apagadas.append(idConta)
      else:
        bot.send_message(message.chat.id, f"❌ Nenhuma conta/tela com o ID: {idConta}", parse_mode="MARKDOWN")

    if len(apagadas) > 0:
      bot.send_message(message.chat.id, f"""✅ {len(apagadas)} CONTA(S)/TELA(S) APAGADA(S) DO ESTOQUE""", parse_mode="MARKDOWN")

bot.infinity_polling()