from dao.utility.db import MySql
from dto.organizzazionedto import Orgdto

class Organizzazione:

    @classmethod
    def getOrganizers(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Organizzazione")
        data = MySql.getResults()
        organizzatori=list()
        for organizzazione in data:
            organizzatori.append(Orgdto(organizzazione[0], organizzazione[1]))

        MySql.closeConnection()

        return organizzatori

    @classmethod
    def notWinningOrganizer(cls):
        MySql.openConnection()
        MySql.query("select	Nazione	 from	Organizzazione o where	Nazione	not	in	(select	Nazione	 from Squadra	where Anno=o.Anno	and	PosizioneInClassifica=1)")
        data = MySql.getResults()
        MySql.closeConnection()
        return data
    