class Partecipazionedto:
    def __init__(self, id_giocatore,anno, nazione, ruolo, gol_segnati):
        self.id_giocatore=id_giocatore
        self.anno=anno
        self.nazione=nazione
        self.ruolo=ruolo
        self.gol_segnati=gol_segnati

    
    def __str__(self):
        return f'{self.id_giocatore}, {self.anno}, {self.nazione},{self.ruolo}, {self.gol_segnati}'
        
    @property
    def id_giocatore(self):
        return self._id_giocatore 
    
    @id_giocatore.setter    
    def id_giocatore(self, id_giocatore):
        self._id_giocatore = id_giocatore
        
    @property
    def anno(self):
        return self._anno 
    
    @anno.setter    
    def anno(self, anno):
        self._anno = anno

    @property
    def nazione(self):
        return self._nazione 
    
    @nazione.setter    
    def nazione(self, nazione):
        self._nazione = nazione

    @property
    def ruolo(self):
        return self._ruolo 
    
    @ruolo.setter    
    def ruolo(self, ruolo):
        self._ruolo = ruolo

    @property
    def gol_segnati(self):
        return self._gol_segnati 
    
    @gol_segnati.setter    
    def gol_segnati(self, gol_segnati):
        self._gol_segnati = gol_segnati
