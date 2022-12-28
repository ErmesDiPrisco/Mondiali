from dao.utility.db import MySql
from dto.squadradto import Squadradto

class Squadra:

    @classmethod
    def getAllTeam(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Squadra")
        data = MySql.getResults()
        squadre=list()
        for squadra in data:
            squadre.append(Squadradto(squadra[0], squadra[1], squadra[2], squadra[3]))

        MySql.closeConnection()

        return squadre

    @classmethod
    def mostConvTeam(cls):
        MySql.openConnection()
        MySql.query("select	Anno, Nazione, count(*) as NumeroConvocazioni from	Partecipazione p	group	by	Anno, Nazione	having	count(*) >=	all	(select	count(*)	from Partecipazione	where Anno = p.Anno	group by Nazione);")
        data = MySql.getResults()
        MySql.closeConnection()
        return data