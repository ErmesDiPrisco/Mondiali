from dao.utility.db import MySql
from dto.partecipazionedto import Partecipazionedto

class Partecipazione:

    @classmethod
    def getAllApplyes(cls):
        MySql.openConnection()
        MySql.query("SELECT * FROM Partecipazione")
        data = MySql.getResults()
        partecipanti=list()
        for partecipante in data:
            partecipanti.append(Partecipazionedto(partecipante[0], partecipante[1], partecipante[2], partecipante[3], partecipante[4]))

        MySql.closeConnection()

        return partecipanti