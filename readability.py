import pyphen
import string
import time

common_words = ['cosa',	'anno',	'uomo',	'giorno',	'volta',	'casa',	'parte',	'vita',	'tempo',	'donna',	'mano',	'occhio',	'ora',	'signore',	'paese',	'momento',	'modo',	'mondo',	'parola',	'padre',	'punto',	'lavoro',	'stato',	'caso',	'città',	'guerra',	'strada',	'figlio',	'notte',	'voce',	'nome',	'sera',	'acqua',	'amico',	'fatto',	'gente',	'amore',	'storia',	'aria',	'forza',	'testa',	'ragione',	'mare',	'mese',	'capo',	'luce',	'sole',	'famiglia',	'piede',	'persona',	'via',	'signora',	'governo',	'senso',	'opera',	'prodotto',	'festa',	'gioco',	'prova',	'campagna',	'fiore',	'sala',	'misura',	'posizione',	'natura',	'ufficio',	'specie',	'successo',	'zona',	'fuoco',	'soldato',	'vista',	'libertà',	'risultato',	'importanza',	'dubbio',	'ricerca',	'dio',	'figura',	'piazza',	'questione',	'nemico',	'pena',	'motivo',	'esperienza',	'ricordo',	'albero',	'politica',	'processo',	'vino',	'porta',	'sud',	'sogno',	'cane',	'isola',	'movimento',	'mente',	'occasione',	'prezzo',	'causa',	'periodo',	'sviluppo',	'sorella',	'effetto',	'giardino',	'attività',	'volontà',	'volto',	'base',	'carattere',	'coscienza',	'guardia',	'memoria',	'terreno',	'animale',	'direzione',	'eccellenza',	'malattia',	'scienza',	'funzione',	'conseguenza',	'parete',	'dente',	'distanza',	'gusto',	'impressione',	'istituto',	'quadro',	'attenzione',	'autore',	'difficoltà',	'passione',	'commissione',	'dito',	'inizio',	'programma',	'spettacolo',	'titolo',	'comunicazione',	'fenomeno',	'maggio',	'stampa',	'denaro',	'destino',	'dovere',	'ferro',	'punta',	'regno',	'epoca',	'luna',	'provincia',	'voglia',	'differenza',	'controllo',	'grazia',	'passato',	'spazio',	'stella',	'corsa',	'erba',	'massa',	'origine',	'polizia',	'soluzione',	'chilometro',	'madre',	'paura',	'cuore',	'idea',	'fondo',	'esempio',	'ordine',	'posto',	'campo',	'faccia',	'moglie',	'ragazzo',	'bisogno',	'cielo',	'letto',	'fronte',	'conto',	'corpo',	'numero',	'ministro',	'problema',	'chiesa',	'braccio',	'bambino',	'pensiero',	'pace',	'morte',	'fine',	'forma',	'resto',	'popolo',	'società',	'studio',	'legge',	'libro',	'figlia',	'resto',	'luogo',	'condizione',	'professore',	'marito',	'verità',	'segno',	'diritto',	'lettera',	'ragazza',	'scuola',	'camera',	'gruppo',	'lira',	'discorso',	'centro',	'secolo',	'mezzo',	'tipo',	'colpa',	'rispetto',	'scena',	'don',	'oggetto',	'possibilità',	'mamma',	'presenza',	'teatro',	'caffè',	'principio',	'termine',	'lingua',	'pezzo',	'capello',	'regione',	'monte',	'università',	'treno',	'inverno',	'nazione',	'pagina',	'scopo',	'compagno',	'necessità',	'potere',	'musica',	'dottore',	'sentimento',	'nave',	'pietra',	'produzione',	'speranza',	'dolore',	'carne',	'generale',	'proposito',	'elemento',	'stazione',	'materia',	'scala',	'maniera',	'arma',	'autorità',	'gamba',	'patria',	'albergo',	'gioia',	'argomento',	'sguardo',	'relazione',	'classe',	'battaglia',	'viso',	'gesto',	'mattino',	'opinione',	'ponte',	'sorriso',	'frase',	'limite',	'ritorno',	'bosco',	'esame',	'lato',	'operazione',	'pranzo',	'costa',	'prato',	'repubblica',	'valle',	'nord',	'fatica',	'odore',	'articolo',	'costruzione',	'rivoluzione',	'zia',	'confronto',	'potenza',	'sforzo',	'sicurezza',	'ufficiale',	'crisi',	'cucina',	'gatto',	'pietà',	'territorio',	'attimo',	'civiltà',	'contatto',	'errore',	'fretta',	'intenzione',	'cultura',	'giudizio',	'spesa',	'aiuto',	'ambiente',	'animo',	'bestia',	'cortile',	'pelle',	'proposta',	'riva',	'segretario',	'abito',	'chiave',	'corrente',	'operaio',	'corso',	'finestra',	'arte',	'sistema',	'piano',	'bocca',	'anima',	'palazzo',	'passo',	'giornata',	'servizio',	'rapporto',	'milione',	'stanza',	'valore',	'colpo',	'sangue',	'interesse',	'spalla',	'silenzio',	'signorina',	'ombra',	'azione',	'vento',	'mattina',	'colore',	'presidente',	'consiglio',	'principe',	'viaggio',	'genere',	'giornale',	'spirito',	'cavallo',	'muro',	'situazione',	'linea',	'giro',	'automobile',	'atto',	'aspetto',	'età',	'fortuna',	'oro',	'partito',	'macchina',	'carta',	'minuto',	'tratto',	'settimana',	'notizia',	'fratello',	'realtà',	'industria',	'piacere',	'maestro',	'personaggio',	'pomeriggio',	'fianco',	'bambina',	'bellezza',	'domanda',	'pianta',	'pubblico',	'sede',	'affare',	'bene',	'metà',	'papà',	'fiume',	'lotta',	'mercato',	'angolo',	'compagnia',	'espressione',	'labbro',	'villa',	'desiderio',	'serie',	'visita',	'coraggio',	'direttore',	'esercito',	'grado',	'padrone',	'risposta',	'tavola',	'immagine',	'montagna',	'energia',	'fede',	'pane',	'seguito',	'estate',	'film',	'frutto',	'onore',	'pericolo',	'scrittore',	'collina',	'zio',	'difesa',	'metro',	'collo',	'cura',	'disposizione',	'Domenica',	'giovanotto',	'poeta',	'stagione',	'peso',	'tono',	'croce',	'decisione',	'poesia',	'fiducia',	'filo',	'folla',	'qualità',	'roba',	'conoscenza',	'favore',	'popolazione',	'strumento',	'uso',	'vestito',	'commercio',	'fabbrica',	'giugno',	'giustizia',	'avvocato',	'messa',	'orecchio',	'sonno',	'congresso',	'porto',	'calcio',	'fantasia',	'matrimonio',	'medico',	'ospedale',	'pianura',	'tavolo',	'fame',	'latte',	'merito',	'attore',	'ricchezza',	'sacrificio',	'atteggiamento',	'concetto',	'mestiere',	'attesa',	'bagno',	'foglia',	'istante',	'lago',	'questo',	'quello',	'più',	'tutto',	'suo',	'altro',	'mio',	'quale',	'tanto',	'grande',	'poco',	'molto',	'nostro',	'stesso',	'primo',	'loro',	'ogni',	'proprio',	'solo',	'quanto',	'bello',	'qualche',	'nuovo',	'certo',	'vero',	'buono',	'tuo',	'nessuno',	'alcuno',	'italiano',	'ultimo',	'vecchio',	'piccolo',	'troppo',	'tale',	'giovane',	'alto',	'vostro',	'diverso',	'meglio',	'lungo',	'povero',	'maggiore',	'mezzo',	'secondo',	'lontano',	'vicino',	'possibile',	'caro',	'pieno',	'nero',	'particolare',	'bianco',	'forte',	'politico',	'attuale',	'latino',	'impossibile',	'sereno',	'puro',	'normale',	'perfetto',	'piano',	'caratteristico',	'russo',	'continuo',	'stupido',	'estremo',	'grigio',	'reale',	'interessante',	'medesimo',	'religioso',	'ampio',	'biondo',	'ufficiale',	'attento',	'enorme',	'sottile',	'triste',	'minimo',	'privato',	'rapido',	'quarto',	'diretto',	'nobile',	'parecchio',	'pericoloso',	'giallo',	'pazzo',	'sacro',	'comodo',	'elettrico',	'assoluto',	'cristiano',	'antico',	'rosso',	'chiaro',	'unico',	'sicuro',	'importante',	'vario',	'giusto',	'francese',	'vivo',	'generale',	'ricco',	'grosso',	'necessario',	'libero',	'nazionale',	'basso',	'semplice',	'grave',	'pubblico',	'comune',	'freddo',	'economico',	'felice',	'difficile',	'tedesco',	'breve',	'pronto',	'serio',	'presente',	'migliore',	'facile',	'terzo',	'caldo',	'estero',	'largo',	'pricipale',	'verde',	'romano',	'umano',	'inutile',	'moderno',	'numeroso',	'simile',	'fresco',	'militare',	'americano',	'vuoto',	'ciascuno',	'tranquillo',	'contento',	'storico',	'superiore',	'inglese',	'fermo',	'solito',	'buio',	'strano',	'noto',	'prossimo',	'profondo',	'sociale',	'cattivo',	'massimo',	'intero',	'uguale',	'bravo',	'brutto',	'preciso',	'qualsiasi',	'improvviso',	'famoso',	'straniero',	'civile',	'internazionale',	'interno',	'vasto',	'segreto',	'greco',	'naturale',	'sinistro',	'duro',	'stanco',	'azzurro',	'recente',	'notevole',	'cittadino',	'destro',	'europeo',	'zitto',	'medio',	'qualunque',	'straordinario',	'nudo',	'futuro',	'cattolico',	'capace',	'industriale',	'personale',	'centrale',	'tecnico',	'dolce',	'leggero',	'morale',	'utile',	'contrario',	'speciale',	'peggio',	'minore',	'contadino',	'essere',	'avere',	'dire',	'potere',	'volere',	'sapere',	'stare',	'dovere',	'vedere',	'andare',	'venire',	'dare',	'parlare',	'trovare',	'sentire',	'lasciare',	'prendere',	'guardare',	'mettere',	'pensare',	'passare',	'credere',	'portare',	'parere',	'tornare',	'sembrare',	'tenere',	'capire',	'morire',	'chiamare',	'conoscere',	'rimanere',	'chiedere',	'cercare',	'entrare',	'vivere',	'aprire',	'uscire',	'ricordare',	'bisognare',	'cominciare',	'rispondere',	'aspettare',	'riuscire',	'chiudere',	'finire',	'arrivare',	'scrivere',	'diventare',	'restare',	'seguire',	'bastare',	'perdere',	'rendere',	'correre',	'salvare',	'vestire',	'costruire',	'camminare',	'ritrovare',	'durare',	'accendere',	'evitare',	'immaginare',	'ridurre',	'contenere',	'fissare',	'costringere',	'abbandonare',	'attendere',	'preferire',	'scegliere',	'avvertire',	'proporre',	'temere',	'esprimere',	'spingere',	'salutare',	'udire',	'difendere',	'dirigere',	'cantare',	'sorgere',	'assicurare',	'assumere',	'tendere',	'dividere',	'scusare',	'mantenere',	'ritenere',	'concludere',	'saltare',	'stabilire',	'appartenere',	'possedere',	'risultare',	'suonare',	'coprire',	'insegnare',	'affermare',	'rivelare',	'conservare',	'risolvere',	'concedere',	'limitare',	'abitare',	'convincere',	'comprare',	'legare',	'sostenere',	'nascere',	'presentare',	'trattare',	'piacere',	'continuare',	'partire',	'servire',	'giungere',	'fermare',	'apparire',	'amare',	'esistere',	'intendere',	'salire',	'mancare',	'ridere',	'lavorare',	'alzare',	'riconoscere',	'sedere',	'leggere',	'cadere',	'mangiare',	'dormire',	'raggiungere',	'comprendere',	'scendere',	'compiere',	'toccare',	'considerare',	'muovere',	'stringere',	'mandare',	'domandare',	'ascoltare',	'decidere',	'ricevere',	'osservare',	'permettere',	'avvenire',	'spiegare',	'raccogliere',	'ottenere',	'offrire',	'mostrare',	'accompagnare',	'dimenticare',	'pregare',	'raccontare',	'bere',	'ritornare',	'cambiare',	'dimostrare',	'sperare',	'sposare',	'ammettere',	'fuggire',	'liberare',	'riferire',	'svegliare',	'capitare',	'posare',	'impedire',	'gettare',	'vendere',	'distinguere',	'offendere',	'rimettere',	'rompere',	'godere',	'imporre',	'significare',	'desiderare',	'divertire',	'volgere',	'giudicare',	'produrre',	'avvicinare',	'diffondere',	'ordinare',	'invitare',	'discutere',	'sbagliare',	'badare',	'tagliare',	'pubblicare',	'attaccare',	'imparare',	'prevedere',	'scappare',	'spegnere',	'annunciare',	'baciare',	'esporre',	'attraversare',	'fornire',	'segnare',	'superare',	'rivedere',	'allontanare',	'ammazzare',	'accogliere',	'voltare',	'preoccupare',	'provocare',	'riempire',	'partecipare',	'piantare',	'rientrare',	'richiedere',	'nascondere',	'ripetere',	'scoprire',	'preparare',	'scorrere',	'rappresentare',	'riprendere',	'costituire',	'incontrare',	'valere',	'accorgersi',	'provare',	'formare',	'uccidere',	'tirare',	'togliere',	'notare',	'aggiungere',	'succedere',	'pagare',	'tentare',	'accadere',	'creare',	'importare',	'pesare',	'usare',	'accettare',	'indicare',	'buttare',	'battere',	'interessare',	'sorridere',	'condurre',	'disporre',	'unire',	'aiutare',	'piangere',	'girare',	'levare',	'soffrire',	'recare',	'riguardare',	'rivolgere',	'tacere',	'occorrere',	'porre',	'vincere',	'svolgere',	'studiare',	'crescere',	'divenire',	'gridare',	'dichiarare',	'contare',	'giocare',	'assistere',	'aumentare',	'lanciare',	'determinare',	'scherzare',	'elevare',	'promettere',	'scomparire',	'trarre',	'distruggere',	'meritare',	'dedicare',	'iniziare',	'sorprendere',	'trasformare',	'confessare',	'arrestare',	'ringraziare',	'riunire',	'volare',	'fondare',	'guidare',	'ferire',	'opporre',	'procedere',	'smettere',	'consentire',	'innamorare',	'organizzare',	'rifiutare',	'riportare',	'dipendere',	'provvedere',	'trascinare',	'fumare',	'scoppiare',	'sognare',	'appoggiare',	'armare',	'celebrare',	'descrivere',	'resistere',	'bruciare',	'colpire',	'estendere',	'staccare',	'affrontare',	'avanzare',	'comporre',	'escludere',	'figurare',	'insistere',	'il',	'di',	'e',	'a',	'un',	'in',	'che',	'non',	'si',	'da',	'lo',	'per',	'con',	'ma',	'come',	'su',	'mi',	'anche',	'o',	'io',	'se',	'perché',	'li',	'ci',	'ne',	'lei',	'ancora',	'tu',	'lui',	'senza',	'bene',	'cui',	'chi',	'già',	'dopo',	'uno',	'noi',	'dove',	'qui',	'no',	'allora',	'tra',	'vi',	'ora',	'fra',	'prima',	'forse',	'sì',	'sotto',	'voi',	'fino',	'oggi',	'quasi',	'pure',	'egli',	'mentre',	'contro',	'invece',	'esso',	'là',	'però',	'né',	'subito',	'verso',	'ciò',	'ecco',	'loro',	'essa',	'fuori',	'meno',	'adesso',	'niente',	'cioè',	'male',	'nulla',	'ah',	'oh',	'quindi',	'appena',	'insieme',	'dunque',	'dentro',	'durante',	'almeno',	'secondo',	'anzi',	'oramai',	'oltre',	'intorno',	'sopra',	'dietro',	'davanti',	'soltanto',	'infatti',	'qualcosa',	'spesso',	'accordo',	'ieri',	'davvero',	'lì',	'qualcuno',	'avanti',	'assai',	'presto',	'qua',	'domani',	'circa',	'giù',	'soprattutto',	'nemmeno',	'grazie',	'tuttavia',	'appunto',	'neppure',	'eh',	'veramente',	'tardi',	'insomma',	'presso',	'intanto',	'lungo',	'neanche',	'piuttosto',	'stasera',	'perciò',	'naturalmente',	'accanto',	'eppure',	'eccetera',	'finalmente',	'infine',	'poiché',	'comunque',	'dinanzi',	'abbastanza',	'peccato',	'certamente',	'coloro',	'attorno',	'magari',	'oppure',	'inoltre',	'indietro',	'addosso',	'addirittura',	'finché',	'perfino',	'affatto',	'stamattina',	'completamente',	'probabilmente',	'chissà',	'sino',	'ognuno',	'entro']

def syllables(text, language):
  syllable_counter = 0
  hyphenated = []
  pyphen.language_fallback(language)
  dic = pyphen.Pyphen(lang=language)
  for i in text:
    elem = dic.inserted(i)
    if '-' not in elem:
      syllable_counter += 1
    else:
      for j in elem:
        if j == '-':
          syllable_counter += 1
  syllable_counter += 2
  return(syllable_counter)

def preprocess(text):
  sentence_counter = 0
  letter_counter = 0
  word_counter = 0
  
  if "." not in text:
      sentence_counter = 1
  else:
      for i in text:
          if i == ".":
              sentence_counter += 1
              text.remove(i)

  for j in text:
      if j in string.ascii_letters:
          letter_counter += 1

  for k in text:
      if k in string.punctuation or k in string.digits:
          text.remove(k)

  text = "".join(text)
  text = text.split()
  word_counter = len(text)

  return(text, sentence_counter, letter_counter, word_counter)

def main():
  filename = input("File name: ")
  language = input("Language: ")
  print()
  tic = time.process_time()
  with open(filename, 'r') as file: #includere encoding='utf8' dopo 'r' se non dovesse funzionare alla prima
    text = file.read()
  text = list(text)

  newt, s, l, w = preprocess(text)
  sy = syllables(newt, language)

  flesch_formula = 206 - (0.65*sy) - w

  if flesch_formula >= 90:
    print("Formula di Flesch:",flesch_formula,'(molto facile - fino a licenza elementare)')
  elif flesch_formula >= 80 and flesch_formula < 90:
    print("Formula di Flesch:",flesch_formula,'(facile - da licenza elementare a prima media)')
  elif flesch_formula >= 70 and flesch_formula < 80:
    print("Formula di Flesch:",flesch_formula,'(abbastanza facile - seconda media)')
  elif flesch_formula >= 60 and flesch_formula < 70:
    print("Formula di Flesch:",flesch_formula,'(medio - licenza media)')
  elif flesch_formula >= 50 and flesch_formula < 60:
    print("Formula di Flesch:",flesch_formula,'(abbastanza difficile - da licenza media a licenza superiore)')
  elif flesch_formula >= 30 and flesch_formula < 50:
    print("Formula di Flesch:",flesch_formula,'(difficile - università ma non laurea)')
  elif flesch_formula < 30:
    print("Formula di Flesch:",flesch_formula,'(molto difficile - laurea)')

  gulpease_index = 89+(((300*s)-(10*l))/w)

  if gulpease_index < 80 and gulpease_index >= 60:
    print("Indice GULPEASE:",gulpease_index,'difficile per licenza elementare')
  elif gulpease_index < 60 and gulpease_index >= 40:
    print("Indice GULPEASE:",gulpease_index,'difficile per licenza media')
  elif gulpease_index < 40:
    print("Indice GULPEASE:",gulpease_index,'difficile per licenza superiore')
  else:
    print("Indice GULPEASE:",gulpease_index)

  difficult_words = 0
  for i in newt:
    if i not in common_words:
      difficult_words += 1
  dale_chall_formula = 0.1579*((difficult_words/w)*100)+0.0496*(w/s)
  
  print("Formula di Dale-Chall:",dale_chall_formula)
  
  print("Frasi:",s)
  print("Parole:",w)
  print("Sillabe:",sy)
  print("Lettere:",l)

  toc = time.process_time()
  print("Durata processo:",toc-tic)

main()