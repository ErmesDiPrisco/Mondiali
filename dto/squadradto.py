class Squadradto:
    def __init__(self, nazione,anno, allenatore, posizione_inclassifica):
        self.nazione=nazione
        self.anno=anno
        self.allenatore=allenatore
        self.posizione_inclassifica=posizione_inclassifica


    
    def __str__(self):
        return f'{self.nazione}, {self.anno}, {self.allenatore},{self.posizione_inclassifica}'
        
    @property
    def nazione(self):
        return self._nazione 
    
    @nazione.setter    
    def nazione(self, nazione):
        self._nazione = nazione
        
    @property
    def anno(self):
        return self._anno 
    
    @anno.setter    
    def anno(self, anno):
        self._anno = anno

    @property
    def allenatore(self):
        return self._allenatore 
    
    @allenatore.setter    
    def allenatore(self, allenatore):
        self._allenatore = allenatore

    @property
    def posizione_inclassifica(self):
        return self._posizione_inclassifica 
    
    @posizione_inclassifica.setter    
    def posizione_inclassifica(self, posizione_inclassifica):
        self._posizione_inclassifica = posizione_inclassifica