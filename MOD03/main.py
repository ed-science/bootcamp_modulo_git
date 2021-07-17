#%%
# imports
import requests
import json
#%%

url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
ret = requests.get(url)

# %%
if ret:
    print(ret)
else:
    print('Falhou')
# %%
dolar = json.loads(ret.text)['USDBRL']

# %%
print(f"20 dolares hoje custam {float(dolar['bid']) * 20} reais")
# %%

def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    # url = 'https://economia.awesomeapi.com.br/json/last/{}'.format(moeda=moeda)
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]} reais")



# %%
cotacao(20, 'USD-BRL')
# %%
cotacao(20, 'JPY-BRL')
# %%
try:
    cotacao(20, 'ed')
except Exception as e: 
    print(e)
else:
    print('ok')

# %%
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]} reais")        


# %%
    lst_money = [
        "USD-BRL"    
    ]

# %%

def error_check(func):
    def inner_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print(f"{func.__name__} falhou")
    return inner_func

@error_check
def multi_moeda(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor} {moeda[-3:]} reais")         


# %%
multi_moeda(20, "USD-BRL")
multi_moeda(20, "EUR-BRL")
multi_moeda(20, "BTC-BRL")
multi_moeda(20, "RPL-BRL")
multi_moeda(20, "JPY-BRL")

# %%
import backoff
import random

def test_func(*args, **kwargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kwargs: {kwargs if kwargs else 'sem kwargs'}
    """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexao foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexao foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de conexao foi excedido')
    else:
        return "OK!"


# %%
test_func()
# %%
test_func(42)
# %%
test_func(42, 51, nome='edson')
# %%
import backoff
import random

@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError, TimeoutError), 
                                    max_tries=10)
def test_func(*args, **kwargs):
    rnd = random.random()
    print(f"""
            RND: {rnd}
            args: {args if args else 'sem args'}
            kwargs: {kwargs if kwargs else 'sem kwargs'}
    """)
    if rnd < .2:
        raise ConnectionAbortedError('Conexao foi finalizada')
    elif rnd < .4:
        raise ConnectionRefusedError('Conexao foi recusada')
    elif rnd < .6:
        raise TimeoutError('Tempo de conexao foi excedido')
    else:
        return "OK!"


# %%
test_func()
# %%
test_func(44)

# %%
import logging

# %%
log = logging.getLogger()
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

# %%

@backoff.on_exception(backoff.expo,(ConnectionAbortedError, ConnectionRefusedError, TimeoutError), 
                                    max_tries=10)
def test_func(*args, **kwargs):
    rnd = random.random()
    log.debug(f"RND: {rnd}")
    log.info (f"args: {args if args else 'sem args'}")
    log.info (f"kwargs: {kwargs if kwargs else 'sem kwargs'}")

    if rnd < .2:
        log.error('Conexao foi finalizada')
        raise ConnectionAbortedError('Conexao foi finalizada')
    elif rnd < .4:
        log.error('Conexao foi recusada')
        raise ConnectionRefusedError('Conexao foi recusada')
    elif rnd < .6:
        log.error('Tempo de conexao foi excedido')
        raise TimeoutError('Tempo de conexao foi excedido')
    else:
        return "OK!"

# %%
test_func()
# %%
