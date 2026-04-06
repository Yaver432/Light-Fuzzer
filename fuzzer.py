import requests

with open(file = 'word_list.txt',mode= 'r',encoding= 'UTF-8') as words:
    
    palavras = [linha.strip().lower() for linha in words]


Url = str(input("Url: "))

def Fuzz():
    
    Lista_urls = []

    for palavra in palavras:
        Url_nova = str(f"{Url}" + f"{palavra}")

        try:
            r = requests.get(url_nova, timeout=5)
        except requests.RequestException as e:
            print(f"[-] Error requesting {url_nova}: {e}")
            continue

        if r.status_code == 200:
            print("[+]",r.status_code,f"{Url_nova}")
            Lista_urls.append(Url_nova)
        elif r.status_code == 403:
            print("[+]",r.status_code,f"{Url_nova}")
        else:
            pass
    
    question = str(input("Guardar logs? [y/n]: "))
    
    if question == 'y':
        with open('log_urls.txt',mode='w',encoding='UTF-8') as logs_urls:
            logs_urls.write(str(Lista_urls).strip())
    else:
        print("No logs")

Fuzz()