from dao.utility.db import MySql
from dto.giocatoridto import Giocatoridto

class Giocatore:

    @classmethod
    def getPlayers(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Giocatore")
        data = MySql.getResults()
        giocatori=list()
        for giocatore in data:
            giocatori.append(Giocatoridto(giocatore[0], giocatore[1]))

        MySql.closeConnection()

        return giocatori
    
    @classmethod
    def playerPartecipation(cls):
        MySql.openConnection()
        MySql.query("select	Nome from Giocatore	g where	3 = (select	count(*) from	Partecipazione	where	IDGiocatore	=	G.ID)	or	1 < (select	count(distinct	Nazione) from	Partecipazione	where	IDGiocatore	= g.ID)")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    
    