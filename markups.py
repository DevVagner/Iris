from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from buscando_dados import *
from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton
aguardando = InlineKeyboardMarkup()
aguardando.row_width = 2
aguardando.add(InlineKeyboardButton("🔁 AGUARDANDO PAGAMENTO", callback_data="."))

inicio2 = InlineKeyboardMarkup()
inicio2.row_width = 1
inicio2.add(InlineKeyboardButton('🛒 Comprar', callback_data='comprar'))
inicio2.row_width = 2
inicio2.add(
    InlineKeyboardButton('💰 Recarregar Saldo', callback_data='recarregar'),
    InlineKeyboardButton('👤 Meu perfil', callback_data='informacion'),
    InlineKeyboardButton('🎁 Resgatar Gift', callback_data='resgatar'),
    InlineKeyboardButton('⚙️ Suporte', url='https://t.me/MillionReasons0'),
    InlineKeyboardButton('🛠️ Alugar BOT', url='https://t.me/supremodrop'),
    InlineKeyboardButton('👥 Grupo', url='https://chat.whatsapp.com/FIwmAZhYaYfFEKnCtD0cuo'))

inicioAdmin = InlineKeyboardMarkup()
inicioAdmin.row_width = 1
inicioAdmin.add(InlineKeyboardButton('🛒 Comprar', callback_data='comprar'))
inicioAdmin.row_width = 2
inicioAdmin.add(
    InlineKeyboardButton('💰 Recarregar Saldo', callback_data='recarregar'),
    InlineKeyboardButton('👤 Meu perfil', callback_data='informacion'),
    InlineKeyboardButton('🎁 Resgatar Gift', callback_data='resgatar'),
    InlineKeyboardButton('⚙️ Suporte', url='https://t.me/MillionReasons0'),
    InlineKeyboardButton('🛠️ Alugar BOT', url='https://t.me/supremodrop'),
    InlineKeyboardButton('👥 Grupo', url='https://chat.whatsapp.com/FIwmAZhYaYfFEKnCtD0cuo'))
inicioAdmin.row_width = 1
inicioAdmin.add(InlineKeyboardButton('⭐ Admin', callback_data='admin'))


contas = InlineKeyboardMarkup()
contas.row_width = 2
contas.add(
    InlineKeyboardButton(f'Conta(s) Netflix', callback_data='add-conta-netflix'),
    InlineKeyboardButton(f'Conta(s) Telecine', callback_data='add-conta-telecine'),
    InlineKeyboardButton(f'Conta(s) Paramount', callback_data='add-conta-paramount'),
    InlineKeyboardButton(f'Conta(s) Disney Plus', callback_data='add-conta-disney'),
    InlineKeyboardButton(f'Conta(s) Prime Vídeo', callback_data='add-conta-prime'),
    InlineKeyboardButton(f'Conta(s) Globo Play Sem Canais', callback_data='add-conta-globosemcanais'),
    InlineKeyboardButton(f'Conta(s) Globo Play + Canais', callback_data='add-conta-globocanais'),
    InlineKeyboardButton(f'Conta(s) Star+', callback_data='add-conta-star'),
    InlineKeyboardButton(f'Conta(s) HBO Max', callback_data='add-conta-hbo'),
    InlineKeyboardButton(f'Conta(s) Play Plus', callback_data='add-conta-playplus'),
    InlineKeyboardButton(f'Conta(s) Sony Channel', callback_data='add-conta-sony'),
    InlineKeyboardButton(f'Conta(s) Dezzer', callback_data='add-conta-dezzer'),
    InlineKeyboardButton(f'Conta(s) Dezzer Capturado', callback_data='add-conta-dezzercapturado'),
    InlineKeyboardButton(f'Conta(s) OI Play', callback_data='add-conta-oiplay'),
    InlineKeyboardButton(f'Conta(s) OI Play Capturado', callback_data='add-conta-oiplaycapturado'),
    InlineKeyboardButton(f'Conta(s) Looke', callback_data='add-conta-looke'),
    InlineKeyboardButton(f'Conta(s) My Family', callback_data='add-conta-myfamily'),
    InlineKeyboardButton(f'Conta(s) Discovery Plus', callback_data='add-conta-discovery'),
    InlineKeyboardButton(f'Conta(s) Spotify Individual', callback_data='add-conta-spotifyindividual'),
    InlineKeyboardButton(f'Conta(s) Spotify Família', callback_data='add-conta-spotifyfamilia'),
    InlineKeyboardButton(f'Conta(s) History Play', callback_data='add-conta-history'),
    InlineKeyboardButton(f'Conta(s) Lumine', callback_data='add-conta-lumine'),
    InlineKeyboardButton(f'Conta(s) Tufos', callback_data='add-conta-tufos'),
    InlineKeyboardButton(f'Conta(s) Sexy Hot', callback_data='add-conta-sexyhot'),
    InlineKeyboardButton(f'Conta(s) UFC BY PASS', callback_data='add-conta-ufc'),
    InlineKeyboardButton(f'Conta(s) Viki', callback_data='add-conta-viki'),
    InlineKeyboardButton(f'Conta(s) Youtube Individual', callback_data='add-conta-youtubeindividual'),
    InlineKeyboardButton(f'Conta(s) Youtube Família', callback_data='add-conta-youtubefamilia'),
    InlineKeyboardButton(f'Conta(s) Crunchyroll', callback_data='add-conta-crunchyroll'),
    InlineKeyboardButton(f'Conta(s) Claro TV+', callback_data='add-conta-claro'),
    InlineKeyboardButton(f'Conta(s) Premiere', callback_data='add-conta-premiere'),
    InlineKeyboardButton(f'Conta(s) Canva Pro', callback_data='add-conta-canva'),
    InlineKeyboardButton('🔙 Voltar', callback_data='admin')
    )


telas = InlineKeyboardMarkup()
telas.row_width = 2
telas.add(
    InlineKeyboardButton(f'Tela(s) Netflix', callback_data='add-tela-netflix'),
    InlineKeyboardButton(f'Tela(s) Telecine', callback_data='add-tela-telecine'),
    InlineKeyboardButton(f'Tela(s) Paramount', callback_data='add-tela-paramount'),
    InlineKeyboardButton(f'Tela(s) Disney Plus', callback_data='add-tela-disney'),
    InlineKeyboardButton(f'Tela(s) Prime Vídeo', callback_data='add-tela-prime'),
    InlineKeyboardButton(f'Tela(s) Globo Play Sem Canais', callback_data='add-tela-globosemcanais'),
    InlineKeyboardButton(f'Tela(s) Globo Play + Canais', callback_data='add-tela-globocanais'),
    InlineKeyboardButton(f'Tela(s) Star+', callback_data='add-tela-star'),
    InlineKeyboardButton(f'Tela(s) HBO Max', callback_data='add-tela-hbo'),
    InlineKeyboardButton(f'Tela(s) Play Plus', callback_data='add-tela-playplus'),
    InlineKeyboardButton(f'Tela(s) Sony Channel', callback_data='add-tela-sony'),
    InlineKeyboardButton(f'Tela(s) OI Play', callback_data='add-tela-oiplay'),
    InlineKeyboardButton(f'Tela(s) Looke', callback_data='add-tela-looke'),
    InlineKeyboardButton(f'Tela(s) Discovery Plus', callback_data='add-tela-discovery'),
    InlineKeyboardButton(f'Tela(s) History Play', callback_data='add-tela-history'),
    InlineKeyboardButton(f'Tela(s) Lumine', callback_data='add-tela-lumine'),
    InlineKeyboardButton(f'Tela(s) Viki', callback_data='add-tela-viki'),
    InlineKeyboardButton('🔙 Voltar', callback_data='admin')
    )

contasOpts = InlineKeyboardMarkup()
contasOpts.row_width = 2
contasOpts.add(
    InlineKeyboardButton(f'Netflix', callback_data='pre-compra-netflix'),
    InlineKeyboardButton(f'Paramount', callback_data='pre-compra-paramount'),
    InlineKeyboardButton(f'Telecine', callback_data='pre-compra-telecine'),
    InlineKeyboardButton(f'Disney Plus', callback_data='pre-compra-disney'),
    InlineKeyboardButton(f'Prime Vídeo', callback_data='pre-compra-prime'),
    InlineKeyboardButton(f'Globo Play Sem Canais', callback_data='pre-compra-globoplaysemcanais'),
    InlineKeyboardButton(f'Globo Play + Canais', callback_data='pre-compra-globoplaycanais'),
    InlineKeyboardButton(f'Star Plus', callback_data='pre-compra-star'),
    InlineKeyboardButton(f'Youtube Premium', callback_data='pre-compra-youtube'),
    InlineKeyboardButton(f'Crunchyroll', callback_data='pre-compra-crunchyroll'),
    InlineKeyboardButton(f'HBO Max', callback_data='pre-compra-hbo'),
    InlineKeyboardButton(f'Claro TV+', callback_data='pre-compra-claro'),
    InlineKeyboardButton(f'Premiere', callback_data='pre-compra-premiere'),
    InlineKeyboardButton(f'Play Plus', callback_data='pre-compra-play-plus'),
    InlineKeyboardButton(f'Sony Channel', callback_data='pre-compra-sony'),
    InlineKeyboardButton(f'Dezzer', callback_data='pre-compra-dezzer'),
    InlineKeyboardButton(f'Dezzer Capturado', callback_data='pre-compra-dezzercapturado'),
    InlineKeyboardButton(f'OI Play', callback_data='pre-compra-oiplay'),
    InlineKeyboardButton(f'OI Play Capturado', callback_data='pre-compra-oiplaycapturado'),
    InlineKeyboardButton(f'Looke', callback_data='pre-compra-looke'),
    InlineKeyboardButton(f'My Family', callback_data='pre-compra-myfamily'),
    InlineKeyboardButton(f'Discovery Plus', callback_data='pre-compra-discovery'),
    InlineKeyboardButton(f'Spotify Individual', callback_data='pre-compra-spotifyindividual'),
    InlineKeyboardButton(f'Spotify Família', callback_data='pre-compra-spotifyfamilia'),
    InlineKeyboardButton(f'History Play', callback_data='pre-compra-history'),
    InlineKeyboardButton(f'Lumine', callback_data='pre-compra-lumine'),
    InlineKeyboardButton(f'Tufos', callback_data='pre-compra-tufos'),
    InlineKeyboardButton(f'Sexy Hot', callback_data='pre-compra-sexyhot'),
    InlineKeyboardButton(f'UFC BY PASS', callback_data='pre-compra-ufc'),
    InlineKeyboardButton(f'Viki', callback_data='pre-compra-viki'),
    InlineKeyboardButton('🔙 Voltar', callback_data='back_comprar')
    )

telasOpts = InlineKeyboardMarkup()
telasOpts.row_width = 2
telasOpts.add(
    InlineKeyboardButton(f'Netflix', callback_data='pre-compra-conta-netflix'),
    InlineKeyboardButton(f'Paramount', callback_data='paramount'),
    InlineKeyboardButton(f'Telecine', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'Disney Plus', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'Prime Vídeo', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'Globo Play Sem Canais', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'Globo Play + Canais', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'Star Plus', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'HBO Max', callback_data='pre-compra-conta'),
    InlineKeyboardButton(f'Play Plus', callback_data='playplus'),
    InlineKeyboardButton(f'Sony Channel', callback_data='sony'),
    InlineKeyboardButton(f'Looke', callback_data='Looke'),
    InlineKeyboardButton(f'Discovery Plus', callback_data='discovery'),
    InlineKeyboardButton(f'History Play', callback_data='history Play'),
    InlineKeyboardButton(f'Lumine', callback_data='lumine'),
    InlineKeyboardButton('🔙 Voltar', callback_data='back_comprar')
  )

compraOpts = InlineKeyboardMarkup()
compraOpts.row_width = 2
compraOpts.add(
  InlineKeyboardButton(f'Comprar conta', callback_data='comprar-conta'),
  InlineKeyboardButton(f'Comprar tela', callback_data='comprar-tela'),
  InlineKeyboardButton('🔙 Voltar', callback_data='contas_premium')
)


compraOpts2 = InlineKeyboardMarkup()
compraOpts2.row_width = 2
compraOpts2.add(
  InlineKeyboardButton(f'Comprar conta', callback_data='comprar-conta'),
  InlineKeyboardButton('🔙 Voltar', callback_data='contas_premium')
)


compraOpts3 = InlineKeyboardMarkup()
compraOpts3.row_width = 2
compraOpts3.add(
  InlineKeyboardButton(f'Comprar tela', callback_data='comprar-tela'),
  InlineKeyboardButton('🔙 Voltar', callback_data='contas_premium')
)


confirmarCompra = InlineKeyboardMarkup()
confirmarCompra.row_width = 1
confirmarCompra.add(
  InlineKeyboardButton(f'💠 Confirmar compra', callback_data='confirmar-compra'),
  InlineKeyboardButton('🔙 Voltar', callback_data='contas_premium')
)


alterarOpts = InlineKeyboardMarkup()
alterarOpts.row_width = 2
alterarOpts.add(
    InlineKeyboardButton(f'Contas Netflix', callback_data='alterar-conta-netflix'),
    InlineKeyboardButton(f'Telas Netflix', callback_data='alterar-tela-netflix'),
    InlineKeyboardButton(f'Contas Paramount', callback_data='alterar-conta-paramount'),
    InlineKeyboardButton(f'Telas Paramount', callback_data='alterar-tela-paramount'),
    InlineKeyboardButton(f'Contas Disney+', callback_data='alterar-conta-disney'),
    InlineKeyboardButton(f'Telas Disney+', callback_data='alterar-tela-disney'),
    InlineKeyboardButton(f'Contas Prime', callback_data='alterar-conta-prime'),
    InlineKeyboardButton(f'Telas Prime', callback_data='alterar-tela-prime'),
    InlineKeyboardButton(f'Contas Globo Play Sem Canais', callback_data='alterar-conta-globosemcanais'),
    InlineKeyboardButton(f'Telas Globo Play Sem Canais', callback_data='alterar-tela-globosemcanais'),
    InlineKeyboardButton(f'Contas Globo Play + Canais', callback_data='alterar-conta-globocanais'),
    InlineKeyboardButton(f'Telas Globo Play + Canais', callback_data='alterar-tela-globocanais'),
    InlineKeyboardButton(f'Contas Telecine', callback_data='alterar-conta-telecine'),
    InlineKeyboardButton(f'Telas Telecine', callback_data='alterar-tela-telecine'),
    InlineKeyboardButton(f'Youtube Individual', callback_data='alterar-conta-youtubeindividual'),
    InlineKeyboardButton(f'Youtube Família', callback_data='alterar-conta-youtubefamilia'),
    InlineKeyboardButton(f'Contas Hbo', callback_data='alterar-conta-hbo'),
    InlineKeyboardButton(f'Telas Hbo', callback_data='alterar-tela-hbo'),
    InlineKeyboardButton(f'Contas Play Plus', callback_data='alterar-conta-playplus'),
    InlineKeyboardButton(f'Telas Play Plus', callback_data='alterar-tela-playplus'),
    InlineKeyboardButton(f'Contas Star+', callback_data='alterar-conta-star'),
    InlineKeyboardButton(f'Telas Star+', callback_data='alterar-tela-star'),
    InlineKeyboardButton(f'Contas Sony Channel', callback_data='alterar-conta-sony'),
    InlineKeyboardButton(f'Telas Sony Channel', callback_data='alterar-tela-sony'),
    InlineKeyboardButton(f'Contas Dezzer', callback_data='alterar-conta-dezzer'),
    InlineKeyboardButton(f'Contas Dezzer Capturado', callback_data='alterar-conta-dezzercapturado'),
    InlineKeyboardButton(f'Contas OI Play', callback_data='alterar-conta-oiplay'),
    InlineKeyboardButton(f'Contas OI Play Capturado', callback_data='alterar-conta-oiplaycapturado'),
    InlineKeyboardButton(f'Contas Looke', callback_data='alterar-conta-looke'),
    InlineKeyboardButton(f'Telas Looke', callback_data='alterar-tela-looke'),
    InlineKeyboardButton(f'Contas Discovery Plus', callback_data='alterar-conta-discovery'),
    InlineKeyboardButton(f'Telas Discovery Plus', callback_data='alterar-tela-discovery'),
    InlineKeyboardButton(f'Contas Spotify Individual', callback_data='alterar-conta-spotifyindividual'),
    InlineKeyboardButton(f'Contas Spotify Família', callback_data='alterar-conta-spotifyfamilia'),
    InlineKeyboardButton(f'Contas Lumine', callback_data='alterar-conta-lumine'),
    InlineKeyboardButton(f'Telas Lumine', callback_data='alterar-tela-lumine'),
    InlineKeyboardButton(f'Contas MyFamily', callback_data='alterar-conta-myfamily'),
    InlineKeyboardButton(f'Contas Tufos', callback_data='alterar-conta-tufos'),
    InlineKeyboardButton(f'Contas Sexy Hot', callback_data='alterar-conta-sexyhot'),
    InlineKeyboardButton(f'Contas UFC BY PASS', callback_data='alterar-conta-ufc'),
    InlineKeyboardButton(f'Contas Viki', callback_data='alterar-conta-viki'),
    InlineKeyboardButton(f'Contas Canva Pro', callback_data='alterar-conta-canvapro'),
    InlineKeyboardButton(f'Crunchyroll', callback_data='alterar-conta-crunchyroll'),
    InlineKeyboardButton(f'Claro TV+', callback_data='alterar-conta-claro'),
    InlineKeyboardButton(f'Premiere', callback_data='alterar-conta-premiere'),
    InlineKeyboardButton('🔙 Voltar', callback_data='admin')
    )


adminOptions = InlineKeyboardMarkup()
adminOptions.row_width = 2
adminOptions.add(
    InlineKeyboardButton(f'🍿 Adicionar contas', callback_data='add-contas'),
    InlineKeyboardButton(f'🖥️ Adicionar telas', callback_data='add-telas'),
    InlineKeyboardButton(f'💲 Alterar valores', callback_data='alterar-valores'),
    InlineKeyboardButton(f'💳 Pagamentos', callback_data='pagamentos'),
    InlineKeyboardButton(f'👥 Listar usuários', callback_data='usuarios'),
    InlineKeyboardButton(f'📄 Listar estoques', callback_data='estoque'),
    InlineKeyboardButton('🔙 Voltar', callback_data='back_comprar')
  )


pagamentosOpts = InlineKeyboardMarkup()
pagamentosOpts.row_width = 2
pagamentosOpts.add(
    InlineKeyboardButton(f'Adicionar pagamento automático', callback_data='pag-automatico'),
    InlineKeyboardButton(f'Adicionar pagamento manual', callback_data='pag-manual'),
    InlineKeyboardButton(f'Excluir conta Automático', callback_data='del-auto'),
    InlineKeyboardButton(f'Excluir conta Manual', callback_data='del-manual'),
    InlineKeyboardButton(f'Definir pagamento Automático', callback_data='definir-pag-auto'),
    InlineKeyboardButton(f'Definir pagamento Manual', callback_data='definir-pag-manual'),
    InlineKeyboardButton('🔙 Voltar', callback_data='back_comprar')
  )

estoqueOpts = InlineKeyboardMarkup()
estoqueOpts.row_width = 2
estoqueOpts.add(
    InlineKeyboardButton(f'Contas Netflix', callback_data='listar-estoque-netflix-conta'),
    InlineKeyboardButton(f'Telas Netflix', callback_data='listar-estoque-netflix-tela'),
    InlineKeyboardButton(f'Contas Paramount', callback_data='listar-estoque-paramount-conta'),
    InlineKeyboardButton(f'Telas Paramount', callback_data='listar-estoque-paramount-tela'),
    InlineKeyboardButton(f'Contas Disney+', callback_data='listar-estoque-disney-conta'),
    InlineKeyboardButton(f'Telas Disney+', callback_data='listar-estoque-disney-tela'),
    InlineKeyboardButton(f'Contas Prime', callback_data='listar-estoque-prime-conta'),
    InlineKeyboardButton(f'Telas Prime', callback_data='listar-estoque-prime-tela'),
    InlineKeyboardButton(f'Contas Globo Play Sem Canais', callback_data='listar-estoque-globosemcanais-conta'),
    InlineKeyboardButton(f'Telas Globo Play Sem Canais', callback_data='listar-estoque-globosemcanais-tela'),
    InlineKeyboardButton(f'Contas Globo Play + Canais', callback_data='listar-estoque-globocanais-conta'),
    InlineKeyboardButton(f'Telas Globo Play + Canais', callback_data='listar-estoque-globocanais-tela'),
    InlineKeyboardButton(f'Contas Telecine', callback_data='listar-estoque-telecine-conta'),
    InlineKeyboardButton(f'Telas Telecine', callback_data='listar-estoque-telecine-tela'),
    InlineKeyboardButton(f'Youtube Individual', callback_data='listar-estoque-youtubeindividual-conta'),
    InlineKeyboardButton(f'Youtube Família', callback_data='listar-estoque-youtubefamilia-conta'),
    InlineKeyboardButton(f'Contas Hbo', callback_data='listar-estoque-hbo-conta'),
    InlineKeyboardButton(f'Telas Hbo', callback_data='listar-estoque-hbo-tela'),
    InlineKeyboardButton(f'Contas Play Plus', callback_data='listar-estoque-playplus-conta'),
    InlineKeyboardButton(f'Telas Play Plus', callback_data='listar-estoque-playplus-tela'),
    InlineKeyboardButton(f'Contas Star+', callback_data='listar-estoque-star-conta'),
    InlineKeyboardButton(f'Telas Star+', callback_data='listar-estoque-star-tela'),
    InlineKeyboardButton(f'Contas Sony Channel', callback_data='listar-estoque-sony-conta'),
    InlineKeyboardButton(f'Telas Sony Channel', callback_data='listar-estoque-sony-tela'),
    InlineKeyboardButton(f'Contas Dezzer', callback_data='listar-estoque-dezzer-conta'),
    InlineKeyboardButton(f'Contas Dezzer Capturado', callback_data='listar-estoque-dezzercapturado-tela'),
    InlineKeyboardButton(f'Contas OI Play', callback_data='listar-estoque-oiplay-conta'),
    InlineKeyboardButton(f'Contas OI Play Capturado', callback_data='listar-estoque-oiplaycapturado-tela'),
    InlineKeyboardButton(f'Contas Looke', callback_data='listar-estoque-looke-conta'),
    InlineKeyboardButton(f'Telas Looke', callback_data='listar-estoque-looke-tela'),
    InlineKeyboardButton(f'Contas Discovery Plus', callback_data='listar-estoque-discovery-conta'),
    InlineKeyboardButton(f'Telas Discovery Plus', callback_data='listar-estoque-discovery-tela'),
    InlineKeyboardButton(f'Contas Spotify Individual', callback_data='listar-estoque-spotifyindividual-conta'),
    InlineKeyboardButton(f'Contas Spotify Família', callback_data='listar-estoque-spotifyfamilia-tela'),
    InlineKeyboardButton(f'Contas Lumine', callback_data='listar-estoque-lumine-conta'),
    InlineKeyboardButton(f'Telas Lumine', callback_data='listar-estoque-lumine-tela'),
    InlineKeyboardButton(f'Contas MyFamily', callback_data='listar-estoque-myfamily'),
    InlineKeyboardButton(f'Contas Tufos', callback_data='listar-estoque-tufos-conta'),
    InlineKeyboardButton(f'Contas Sexy Hot', callback_data='listar-estoque-sexyhot-conta'),
    InlineKeyboardButton(f'Contas UFC BY PASS', callback_data='listar-estoque-ufc-conta'),
    InlineKeyboardButton(f'Contas Viki', callback_data='listar-estoque-viki-conta'),
    InlineKeyboardButton(f'Contas Canva Pro', callback_data='listar-estoque-canvapro-conta'),
    InlineKeyboardButton(f'Crunchyroll', callback_data='listar-estoque-crunchyroll-conta'),
    InlineKeyboardButton(f'Claro TV+', callback_data='listar-estoque-claro-conta'),
    InlineKeyboardButton(f'Premiere', callback_data='listar-estoque-premiere-conta'),
    InlineKeyboardButton('🔙 Voltar', callback_data='admin')
    )

i2 = InlineKeyboardMarkup()
i2.row_width = 1
i2.add(
    InlineKeyboardButton('🔙 Voltar', callback_data='comprar'))
        
comprar2 = InlineKeyboardMarkup()
comprar2.row_width = 1
comprar2.add(
    InlineKeyboardButton('🍿 Contas Premium', callback_data='contas_premium'),
    InlineKeyboardButton('📺 IPTV', callback_data='indisponivel'),
    InlineKeyboardButton('🛍️ Lojas', callback_data='indisponivel'),
    InlineKeyboardButton('📱 Internet Ilimitada', callback_data='indisponivel'),
    InlineKeyboardButton('🔙 Voltar', callback_data='back_comprar'))


i = InlineKeyboardMarkup()
i.row_width = 1
i.add(
    InlineKeyboardButton('🔙 Voltar', callback_data='back_comprar'))