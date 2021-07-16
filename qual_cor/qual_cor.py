import cv2
import numpy as np
import pandas as pd
import argparse

comando = argparse.ArgumentParser()
comando.add_argument('-i', '--image', required=True, help="Caminho da Imagem")
args = vars(comando.parse_args())
CaminhoImagem = args['image']

imagem = cv2.imread(CaminhoImagem)

click = False
verm = verd = azul = xpos = ypos = 0

index=["color","cor_nome","hexadecimal","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def NomedaCor(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cornome = csv.loc[i,"cor_nome"]
    return cornome

def desenha(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global azul,verd,verm,xpos,ypos, click
        click = True
        xpos = x
        ypos = y
        azul,verd,verm = imagem[y,x]
        azul = int(azul)
        verd = int(verd)
        verm = int(verm)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',desenha)

while(1):

    cv2.imshow("image",imagem)
    if (click):
   
        cv2.rectangle(imagem,(20,20), (750,60), (azul,verd,verm), -1)

        cor = NomedaCor(verm,verd,azul) + ' R='+ str(verm) +  ' G='+ str(verd) +  ' B='+ str(azul)
        
        cv2.putText(imagem, cor,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(verm+verd+azul>=600):
            cv2.putText(imagem, cor,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        click=False
 
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()
