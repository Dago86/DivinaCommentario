# DivinaCommentario
Backend di una  web app restful: commentario della Divina Commedia
Un db contiene i canti della Divina Commedia, divisi per parte (Inferno, Purgatorio, Paradiso) e nome (Canto I, Canto II, etc). Un utente può loggarsi e commentarli col proprio nome utente, previa registrazione sul servizio.

work in progress

Done:
Modello User: può registrarsi e autenticarsi,  gestione di sicurezza tramite standard JWT

#### Testing
Per utilizzare e testare le chiamate rest del backend si guardi il foglio di Postman caricato nella cartella utils

#### Stack utilizzato
- Python 3.7.3
- Flask 2.0.1
- Flask SqlAlchemy 2.5.1
