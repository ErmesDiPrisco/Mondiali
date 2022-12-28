from dao.giocatoridao import Giocatore
from dao.Organizzazionedao import Organizzazione
from dao.partecipazionedao import Partecipazione
from dao.Squadradao import Squadra

giocatore=Giocatore()
organ=Organizzazione()
par=Partecipazione()
team=Squadra()

print(team.mostConvTeam())
print (organ.notWinningOrganizer())
print(giocatore.playerPartecipation())