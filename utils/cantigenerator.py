from db import db
from models.canto import CantoModel


#Aggiungo canti di prova nel DB
def add_canti_to_db():
    canto = CantoModel('Canto I', 'Inferno', 'Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura, che la dritta via era smarrita...')
    canto.save_to_db()
    canto = CantoModel('Canto II', 'Inferno', 'Lo giorno se n\'andava, e l\'aere bruno toglieva li animai che sono in terra da le fatiche loro; e io sol uno...')
    canto.save_to_db()
    canto = CantoModel('Canto III', 'Inferno', 'Per me si va nella città dolante, \n per me si va ne l\' etterno dolore, \n per me si va tra la perduta gente...')
    canto.save_to_db()


    canto = CantoModel('Canto I', 'Purgatorio', 'Per correre miglior acque alza le vele\n ormai la navicella del mio ingegno, \n che lascia deitro a sé mar sì crudele;')
    canto.save_to_db()
    canto = CantoModel('Canto II', 'Purgatorio', 'Già era ‘l sole a l’orizzonte giunto \n lo cui meridian cerchio coverchia \nIerusalèm col suo più alto punto; ')
    canto.save_to_db()
    canto = CantoModel('Canto III', 'Purgatorio', 'Avvegna che la subitana fuga \n dispergesse color per la campagna, \n rivolti al monte ove ragion ne fruga,')
    canto.save_to_db()



    canto = CantoModel('Canto I', 'Paradiso', 'La gloria di colui che tutto move  \n per l’universo penetra, e risplende \n in una parte più e meno altrove. ')
    canto.save_to_db()
    canto = CantoModel('Canto II', 'Paradiso', 'O voi che siete in piccioletta barca, \ndesiderosi d’ascoltar, seguiti \ndietro al mio legno che cantando varca,    ')
    canto.save_to_db()
    canto = CantoModel('Canto III', 'Paradiso', 'Quel sol che pria d’amor mi scaldò ‘l petto, \ndi bella verità m’avea scoverto, \nprovando e riprovando, il dolce aspetto;')
    canto.save_to_db()

