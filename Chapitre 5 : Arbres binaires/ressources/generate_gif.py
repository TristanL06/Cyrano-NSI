from base64 import b64encode
from PIL import Image, ImageDraw
import requests

def code(s):
    return b64encode(s.encode('ascii')).decode('ascii')

lien = "https://mermaid.ink/img/Z3JhcGggVEQKICAgIEEoKDAwKSkKICAgIEIoKDEwKSkKICAgIEMoKDExKSkKICAgIEQoKDEyKSkKICAgIEUoKDIwKSkKICAgIEYoKDIxKSkKICAgIEcoKDIyKSkKICAgIEgoKDIzKSkKICAgIEkoKDI0KSkKICAgIAogICAgQSAtLS0gQgogICAgQSAtLS0gQwogICAgQSAtLS0gRAogICAgQiAtLS0gRQogICAgQiAtLS0gRgogICAgRCAtLS0gRwogICAgRCAtLS0gSAogICAgRCAtLS0gSQogICAgCiAgY2xhc3NEZWYgb2sgZmlsbDojNWY1?type=png"

arbre = """graph TD
    A((00)) %%1
    B((10)) %%2
    C((12)) %%3
    D((20)) %%4
    E((21)) %%5
    F((22)) %%6
    G((23)) %%7
    
    A --- B
    A --- C
    B --- D
    B --- E
    C --- F
    C --- G
    
  classDef ok fill:#5f5"""

d = {"largeur":[1,2,3,4,5,6,7], "préfix":[1,2,4,5,3,6,7], "infixe":[4,2,5,1,6,3,7], "postfix":[4,5,2,6,7,3,1]}

lien = f"https://mermaid.ink/img/{code(arbre)}?type=png"
with open("current_temoin.png","wb") as file:
    r = requests.get(lien)
    while not r.ok:
        r = requests.get(lien)
    file.write(r.content)

for methode in d:
    print(methode)
    images = [Image.open("current_temoin.png")]
    s = arbre.split('\n')
    for n in d[methode]:
        print(n)
        s[n] = s[n].split(' %%')[0] + ":::ok"
        t = '\n'.join(s)
        lien = f"https://mermaid.ink/img/{code(t)}?type=png"
        with open(f"current{n}.png","wb") as file:
            r = requests.get(lien)
            while not r.ok:
                r = requests.get(lien)
            file.write(r.content)
        images.append(Image.open(f"current{n}.png"))
    #images.append(Image.frombytes("RGBA",(411,233),))
    images[0].save(f'{methode}.gif',
                   save_all = True, append_images = images[1:],
                   optimize = False, duration = len(images)*100,
                   loop=0)
