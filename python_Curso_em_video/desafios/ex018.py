import math

angu = float (input('Digite um angulo '))
seno = math.sin(math.radians(angu))
print ('O angulo de {} tem o SENO de {:.2f}'.format(angu, seno))
coss = math.cos(math.radians(angu))
print ('O angulo de {} tem o COSSENO de {:.2f}'.format(angu , coss))
tanga = math.tan(math.radians(angu))
print ('O angulo de {} tem o TANGENTE de {:.2f}'.format(angu, tanga))