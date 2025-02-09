
import read_registre as rr
##import alter_registre as ar
##import update_registre as ur
##import delete_registre as dr


results=rr.read_reg()

for itera in results:
    print('\n')
    print('Nom: ' + itera[0])
    print('Adreça: ' + itera[1])
    print('telèfon: ' + itera[2])
    print('email: ' + itera[3])
    print('neixament: ' + itera[4])

##ur.update_reg()

##ar.alter_reg()

##dr.delete_reg()