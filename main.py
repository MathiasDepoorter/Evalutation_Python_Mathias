###### exercice 01
def makeDico_E8 (nomFichier , sep):
  dicoDNS = {}
  file = open(nomFichier,"r")
  lines = file.readlines()
  for line in lines:
    a = line.split(sep)
    dicoDNS[a[0]]=a[1]
  print("Creation d'un dictionnaire a partir du fichier '{}' avec '{}' entrees".format(nomFichier,len(dicoDNS)))
  return dicoDNS  

###### exercice 02
def verifUrl_K1 (url):
  partie = url.split('.')
  if len(partie) == 2:
    if len(partie[1]) < 4:
      return True
    else:
      print('url mal formee')
      return False
  else:
    print('url mal formee')
    return False
    
###### exercice 03
def getTLD_S4(url):
  if verifUrl_K1 (url) == False:
    print("TLD mal formee")
    return False
  else:
    partie = url.split('.')
    return partie[1]

###### exercice 04 
def VerifTLD_D8 (tldOk,tld): 
  if tld in tldOk:
    return True
  else: 
    return False

###### exercice 05
def ipVerifFormat_Q6(adresseIp):
  adresseIp.replace('\n','')
  partie = adresseIp.split('.')
  if len(partie) == 4:
    if int(partie[0]) > -1:
      if int(partie[0]) < 256:
        if int(partie[1]) > -1:
          if int(partie[1]) < 256:
            if int(partie[2]) > -1:
              if int(partie[2]) < 256:
                if int(partie[3]) > -1:
                  if int(partie[3]) < 256:
                    return True
  return False

###### exercice 06
def makeTLD_G8 (dico):
  liste = []         
  for key, value in dico.items():
    result = getTLD_S4(key) 
    if result not in liste:
      liste.append(result)
  
  print("Creation d'une liste de TLD comprenant {} entrees ".format(len(liste)))
  return liste

###### exercice 07
class serveurDns_F2:
  def __init__(self, resolDns):
    self.resolDns = resolDns

  ###### exercice 08
  def resolDNS_W4(self, url):
    if verifUrl_K1(url):
      if url in self.resolDns:
        return self.resolDns[url]
    print('erreur de format de l’url')
    return False

  ###### exercice 09
  def resolInverse_Z5(self, adresseIp):
    if ipVerifFormat_Q6(adresseIp):
      for key, value in self.resolDns.items():
        value = value.replace('\n','')
        if value == adresseIp:
          return key
    print("adresse IP inconnue")
    return False

  ###### exercice 10
  def addAsso_V6(self, url, adresseIp):
    if ipVerifFormat_Q6(adresseIp) == False:
      return 'malformedAddress'

    if verifUrl_K1(url) == False:
      return 'malformedUrl'
    
    if self.resolInverse_Z5(adresseIp) != False:
      return 'existingIP'

    if self.resolDNS_W4(url) != False:
      return 'existingURL'

    self.resolDns[url] = adresseIp
    print(self.resolDns[url])
    return True


print("exercice 01 #######################")
resolDns = makeDico_E8 ('dns.txt' , ',')
print(resolDns)

print("exercice 02 #######################")
result = verifUrl_K1 ('toto.fr')
print("test de 'toto.fr' : resultat = {}".format(result))
result = verifUrl_K1 ('to.to.fr')
print("test de 'to.to.fr' : resultat = {}".format(result))
result = verifUrl_K1 ('toto.frog')
print("test de 'toto.frog' : resultat = {}".format(result))

print("exercice 03 #######################")
result = getTLD_S4 ('toto.fr')
print("test de 'toto.fr' : resultat = {}".format(result))

###### exercice 04
print("exercice 04 #######################")
result = VerifTLD_D8 (['fr','com','net'],'fr')
print("la liste passee en argument et contenant les TLD est '['fr', 'com', 'net']' test de 'fr' : resultat = {}".format(result))
###### exercice 05
print("exercice 05 #######################")
result = ipVerifFormat_Q6("1.1.1.1")
print("test de '1.1.1.1' : resultat = {}".format(result))
###### exercice 06
print("exercice 06 #######################")
tldOk = makeTLD_G8 (resolDns)
print(tldOk)
###### exercice 07
print("exercice 07 #######################")
s = serveurDns_F2 (resolDns)

###### exercice 08
print("exercice 08 #######################")
print(s.resolDNS_W4 ('google.fr'))

###### exercice 09
print("exercice 09 #######################")
print(s.resolInverse_Z5 ('65.55.206.154'))

###### exercice 10
print("exercice 10 #######################")
print(s.addAsso_V6('developpez.net', '87.98.128.200'))
print(s.addAsso_V6('coding.nzl', '87.98.128.200'))
print(s.addAsso_V6('developpez.net', '271.98.128.200'))
print(s.addAsso_V6('developpez.net', '87.98.1280.200'))