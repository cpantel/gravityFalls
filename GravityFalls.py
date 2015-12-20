from SubstitutionAttack import *



#mensaje="lar zpuhtfty xweupjr ghgzt"
#mensaje="pvrek big qf. jcdqzrf' znvefh obcx: 'c bewrs vvutbfl bt bknx cvay bknx cvay bknx'"
#mensaje="zhofrph wr judylwb idoov. qhaw zhhn: uhwxuq wr exww lvodqg rqzdugv drvklpd!"
#mensaje = "pu. fdhvduldq zloo eh rxw qhaw zhhn. pu. dwedvk zloo vxevwlwxwh."
#mensaje = "fduod, zkb zrqw brx fdoo ph?"
mensaje = "zhofrph wr judylwb idoov"

#mensaje = "pyol ys qh llfdjw: vah dncvfw ztckw xkg wffwwknllmrp? wisagcxj ar wkuisw! dpx wdsukxr: llh ubfo"
#mensaje="lar zpuhtfty xweupjr ghgzt"
#mensaje = "pvrek big qf. jcdqzrf' znvefh obcx: 'c bewrs vvutbfl bt bknx cvay bknx cvay bknx'"        
#mensaje="lar zpuhtfty xweupjr ghgzt - pvrek big qf. jcdqzrf' znvefh obcx: 'c bewrs vvutbfl bt bknx cvay - pyol ys qh llfdjw: vah dncvfw ztckw xkg wffwwknllmrp? wisagcxj ar wkuisw! dpx wdsukxr: llh ubfo"
 

attacker = SubstitutionAttack()
attacker.load(mensaje)
attacker.showMessages()
while not attacker.exit:
    attacker.accept()