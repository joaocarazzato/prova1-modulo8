import re
import actions

intent_dict = {
        r"[Ss]air": actions.program_exit,
        r"[Cc]omo posso atualizar[ o ]* meu cart[aã]o( de cr[eé]dito| de d[eé]bito)?|([Pp]reciso|[Nn]ecessito) mudar a (minha )?forma de pagamento, (o que fazer|como fazer)|([Qq]uero|[Gg]ostaria de) (atualizar|mudar) minhas informações de pagamento|Método de pagamento desatualizado, como (proceder para|posso) atualizar": actions.payment_issues,
        r"[Oo]nde (posso ver |vejo )o status (atual )?do meu pedido|[Cc]omo (faço|posso fazer) para rastrear (o )?meu pedido|([Qq]uero|[Gg]ostaria de) saber onde est[aá] (o )?meu pedido, como (faço|posso fazer)|([Qq]uero consultar meu)?[Ss]tatus de entrega, como (posso )?consultar": actions.status
        }

def chatbot():
    command = input("Digite sua pergunta: ")
    for key, function in intent_dict.items():
        pattern = re.compile(key)
        point = pattern.findall(command)
        if point:
            print("Ação detectada")
            function()
            return

def main():
    while True:
        chatbot()

if __name__ == "__main__":
    main()