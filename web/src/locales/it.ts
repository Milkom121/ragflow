export default {
  translation: {
    common: {
      italian: 'Italiano',
      delete: 'Elimina',
      deleteModalTitle: 'Sei sicuro di voler eliminare questo elemento?',
      ok: 'Sì',
      cancel: 'No',
      total: 'Totale',
      rename: 'Rinomina',
      name: 'Nome',
      save: 'Salva',
      namePlaceholder: 'Inserisci il nome',
      next: 'Avanti',
      create: 'Crea',
      edit: 'Modifica',
      upload: 'Carica',
      english: 'Inglese',
      portugueseBr: 'Portoghese (Brasile)',
      chinese: 'Cinese semplificato',
      traditionalChinese: 'Cinese tradizionale',
      language: 'Lingua',
      languageMessage: 'Inserisci la tua lingua!',
      languagePlaceholder: 'seleziona la tua lingua',
      copy: 'Copia',
      copied: 'Copiato',
      comingSoon: 'Prossimamente',
      download: 'Scarica',
      close: 'Chiudi',
      preview: 'Anteprima',
      move: 'Sposta',
      warn: 'Attenzione',
      action: 'Azione',
      s: 'S',
      pleaseSelect: 'Seleziona',
      pleaseInput: 'Inserisci',
      submit: 'Invia',
      embedIntoSite: 'Incorpora nella pagina web',
      previousPage: 'Precedente',
      nextPage: 'Successivo',
      add: 'Aggiungi',
    },
    login: {
      login: 'Accedi',
      signUp: 'Registrati',
      loginDescription: 'Siamo felici di rivederti!',
      registerDescription: 'Benvenuto a bordo!',
      emailLabel: 'Email',
      emailPlaceholder: 'Inserisci email',
      passwordLabel: 'Password',
      passwordPlaceholder: 'Inserisci password',
      rememberMe: 'Ricordami',
      signInTip: 'Non hai un account?',
      signUpTip: 'Hai già un account?',
      nicknameLabel: 'Nickname',
      nicknamePlaceholder: 'Inserisci nickname',
      register: 'Crea un account',
      continue: 'Continua',
      title: 'Inizia a costruire i tuoi assistenti smart.',
      description:
        'Registrati gratis per esplorare la tecnologia RAG. Crea knowledge base e AI per la tua azienda.',
      review: 'da oltre 500 recensioni',
    },
    header: {
      knowledgeBase: 'Knowledge Base',
      chat: 'Chat',
      register: 'Registrati',
      signin: 'Accedi',
      home: 'Home',
      setting: 'Impostazioni utente',
      logout: 'Esci',
      fileManager: 'Gestione File',
      flow: 'Agente',
      search: 'Cerca',
      welcome: 'Benvenuto su',
    },
    knowledgeList: {
      welcome: 'Bentornato',
      description: 'Quali knowledge base vuoi usare oggi?',
      createKnowledgeBase: 'Crea knowledge base',
      name: 'Nome',
      namePlaceholder: 'Inserisci nome!',
      doc: 'Documenti',
      searchKnowledgePlaceholder: 'Cerca',
      noMoreData: `Questo è tutto. Nient'altro.`,
    },
    knowledgeDetails: {
      dataset: 'Dataset',
      testing: 'Test di retrieval',
      files: 'File',
      configuration: 'Configurazione',
      knowledgeGraph: 'Knowledge graph',
      name: 'Nome',
      namePlaceholder: 'Inserisci nome!',
      doc: 'Documenti',
      datasetDescription:
        '😉 Attendi che i tuoi file siano stati analizzati prima di iniziare una chat AI.',
      addFile: 'Aggiungi file',
      searchFiles: 'Cerca nei file',
      localFiles: 'File locali',
      emptyFiles: 'Crea file vuoto',
      webCrawl: 'Web Crawl',
      chunkNumber: 'Numero chunk',
      uploadDate: 'Data upload',
      chunkMethod: 'Metodo chunking',
      enabled: 'Abilita',
      disabled: 'Disabilita',
      action: 'Azione',
      parsingStatus: 'Stato parsing',
      parsingStatusTip:
        'Il tempo di parsing dipende da vari fattori. Abilitare funzioni come Knowledge Graph, RAPTOR, Estrazione Automatica di Domande o Parole Chiave aumenterà il tempo di elaborazione.',
      processBeginAt: 'Inizio',
      processDuration: 'Durata',
      progressMsg: 'Progresso',
      testingDescription:
        'Esegui un test di retrieval per verificare se RAGFlow recupera il contenuto desiderato. Se hai modificato le impostazioni, ricorda di applicarle anche nelle impostazioni dell’assistente.',
      similarityThreshold: 'Soglia di similarità',
      similarityThresholdTip:
        'Imposta la soglia di similarità tra la query e i chunk. I chunk con punteggio inferiore saranno esclusi.',
      vectorSimilarityWeight: 'Peso similarità keyword',
      vectorSimilarityWeightTip:
        'Imposta il peso della similarità keyword nel punteggio combinato.',
      testText: 'Testo di prova',
      testTextPlaceholder: 'Inserisci la tua domanda!',
      testingLabel: 'Test',
      similarity: 'Similarità ibrida',
      termSimilarity: 'Similarità termini',
      vectorSimilarity: 'Similarità vettoriale',
      hits: 'Risultati',
      view: 'Visualizza',
      filesSelected: 'File selezionati',
      upload: 'Carica',
      run: 'Analizza',
      runningStatus0: 'IN ATTESA',
      runningStatus1: 'IN ANALISI',
      runningStatus2: 'CANCELLATO',
      runningStatus3: 'SUCCESSO',
      runningStatus4: 'ERRORE',
      pageRanges: 'Intervallo pagine',
      pageRangesTip:
        'Solo le pagine in questo intervallo saranno elaborate.',
      fromPlaceholder: 'da',
      fromMessage: 'Numero pagina iniziale mancante',
      toPlaceholder: 'a',
      toMessage: 'Numero pagina finale mancante (escluso)',
      layoutRecognize: 'Parser PDF',
      layoutRecognizeTip:
        'Usa un modello visuale per analizzare il layout PDF.',
      taskPageSize: 'Dimensione task',
      taskPageSizeMessage: 'Inserisci la dimensione del task!',
      taskPageSizeTip: `Imposta la dimensione dei chunk per l’analisi parallela.`,
      addPage: 'Aggiungi pagina',
      greaterThan: 'Il valore deve essere maggiore di "a"!',
      greaterThanPrevious:
        'Il valore deve essere maggiore del precedente!',
      selectFiles: 'Seleziona file',
      changeSpecificCategory: 'Cambia categoria specifica',
      uploadTitle: 'Trascina qui il file per caricarlo',
      uploadDescription:
        'Supporta upload singolo o multiplo. Limite totale 1GB per installazioni locali, 10MB per la demo online.',
      chunk: 'Chunk',
      bulk: 'Bulk',
      cancel: 'Annulla',
      rerankModel: 'Modello rerank',
      rerankPlaceholder: 'Seleziona',
      rerankTip: `Opzionale. Se vuoto, verrà usata la similarità keyword e vettoriale.`,
      topK: 'Top-K',
      topKTip: `Numero di chunk da inviare al modello rerank.`,
      delimiter: `Delimitatore`,
      delimiterTip:
        'Un delimitatore può essere uno o più caratteri speciali.',
      html4excel: 'Excel in HTML',
      html4excelTip: `Usa con chunking "Generale".`,
      autoKeywords: 'Auto-keyword',
      autoKeywordsTip: `Estrai automaticamente N keyword per ogni chunk.`,
      autoQuestions: 'Auto-question',
      autoQuestionsTip: `Estrai automaticamente N domande per ogni chunk.`,
      redo: 'Vuoi cancellare i {{chunkNum}} chunk esistenti?',
      setMetaData: 'Imposta Meta Dati',
      pleaseInputJson: 'Inserisci JSON',
      documentMetaTips: `<p>I meta dati sono in formato JSON (non ricercabili). Verranno aggiunti al prompt per l’LLM se presenti chunk del documento.</p>`,
      metaData: 'Meta dati',
      deleteDocumentConfirmContent:
        'Il documento è associato al knowledge graph. Dopo l’eliminazione, le informazioni correlate saranno eliminate.',
      plainText: 'Naive',
      reRankModelWaring: 'Il modello rerank è molto lento.',
    },
    knowledgeConfiguration: {
      // Traduzione italiana completata
      titleDescription: 'Aggiorna la configurazione della tua knowledge base qui, in particolare il metodo di chunking.',
      name: 'Nome della knowledge base',
      photo: 'Foto della knowledge base',
      description: 'Descrizione',
      language: 'Lingua del documento',
      languageMessage: 'Inserisci la tua lingua!',
      languagePlaceholder: 'Inserisci la tua lingua!',
      permissions: 'Permessi',
      embeddingModel: 'Modello di embedding',
      chunkTokenNumber: 'Dimensione consigliata del chunk',
      chunkTokenNumberMessage: 'Il numero di token per chunk è obbligatorio',
      embeddingModelTip: 'Il modello di embedding predefinito per la knowledge base. Non può essere modificato una volta che la knowledge base ha chunk. Per cambiare modello, devi eliminare tutti i chunk esistenti.',
      permissionsTip: "Se impostato su 'Team', tutti i membri del team potranno gestire la knowledge base.",
      chunkTokenNumberTip: 'Imposta la soglia di token per creare un chunk. Un segmento con meno token di questa soglia sarà combinato con i segmenti successivi fino a superare la soglia, creando un chunk. Nessun nuovo chunk sarà creato a meno che non si incontri un delimitatore, anche se la soglia è superata.',
      chunkMethod: 'Metodo di chunking',
      chunkMethodTip: 'Visualizza i suggerimenti a destra.',
      upload: 'Carica',
      english: 'Inglese',
      chinese: 'Cinese',
      portugueseBr: 'Portoghese (Brasile)',
      embeddingModelPlaceholder: 'Seleziona un modello di embedding.',
      chunkMethodPlaceholder: 'Seleziona un metodo di chunking.',
      save: 'Salva',
      me: 'Solo io',
      team: 'Team',
      cancel: 'Annulla',
      methodTitle: 'Descrizione del metodo di chunking',
      methodExamples: 'Esempi',
      methodExamplesDescription: 'Gli screenshot seguenti sono forniti per chiarezza.',
      dialogueExamplesTitle: 'visualizza',
      methodEmpty: 'Mostrerà una spiegazione visiva delle categorie della knowledge base',
      book: `<p>I formati di file supportati sono <b>DOCX</b>, <b>PDF</b>, <b>TXT</b>.</p><p>
      Per ogni libro in PDF, imposta gli <i>intervalli di pagina</i> per rimuovere informazioni indesiderate e ridurre il tempo di analisi.</p>`,
      laws: `<p>I formati di file supportati sono <b>DOCX</b>, <b>PDF</b>, <b>TXT</b>.</p><p>
      I documenti legali seguono tipicamente un formato rigoroso. Usiamo la funzione testo per identificare i punti di divisione. 
      </p><p>
      Il chunk ha una granularità coerente con 'ARTICOLO', assicurando che tutto il testo di livello superiore sia incluso nel chunk.
      </p>`,
      manual: `<p>Supportato solo <b>PDF</b>.</p><p>
      Si assume che il manuale abbia una struttura gerarchica delle sezioni, usando i titoli delle sezioni più basse come unità base per il chunking dei documenti. Pertanto, figure e tabelle nella stessa sezione non saranno separate, il che può portare a chunk più grandi.
      </p>`,
      naive: `<p>I formati di file supportati sono <b>MD, MDX, DOCX, XLSX, XLS (Excel 97-2003), PPT, PDF, TXT, JPEG, JPG, PNG, TIF, GIF, CSV, JSON, EML, HTML</b>.</p>
      <p>Questo metodo chunka i file usando un metodo 'naive': </p>
      <p>
      <li>Usa un modello di rilevamento visivo per dividere i testi in segmenti più piccoli.</li>
      <li>Poi combina segmenti adiacenti fino a superare la soglia specificata da 'Numero di token per chunk', a quel punto viene creato un chunk.</li></p>`,
      paper: `<p>Supportato solo <b>PDF</b>.</p><p>
      I documenti saranno divisi per sezione, come <i>abstract, 1.1, 1.2</i>. </p><p>
      Questo approccio permette al LLM di riassumere il documento in modo più efficace e fornire risposte più comprensibili. 
      Tuttavia, aumenta anche il contesto per le conversazioni AI e il costo computazionale per il LLM. Durante una conversazione, considera di ridurre il valore di ‘<b>topN</b>’.</p>`,
      presentation: `<p>I formati di file supportati sono <b>PDF</b>, <b>PPTX</b>.</p><p>
      Ogni pagina nelle slide è trattata come un chunk, con la sua immagine in miniatura salvata.</p><p>
      <i>Questo metodo di chunking è applicato automaticamente a tutti i file PPT caricati, quindi non è necessario specificarlo manualmente.</i></p>`,
      qa: `
      <p>
      Questo metodo di chunking supporta i formati di file <b>XLSX</b> e <b>CSV/TXT</b>.
    </p>
    <li>
      Se un file è in formato <b>XLSX</b> o <b>XLS (Excel 97-2003)</b>, deve contenere due colonne senza intestazioni: una per le domande e l’altra per le risposte, con la colonna delle domande prima di quella delle risposte. Sono accettati più fogli, purché le colonne siano strutturate correttamente.
    </li>
    <li>
      Se un file è in formato <b>CSV/TXT</b>, deve essere codificato in UTF-8 con TAB come delimitatore per separare domande e risposte.
    </li>
    <p>
      <i>
        Le righe di testo che non rispettano queste regole saranno ignorate, e ogni coppia Q&A sarà considerata un chunk distinto.
      </i>
    </p>
      `,
      resume: `<p>I formati di file supportati sono <b>DOCX</b>, <b>PDF</b>, <b>TXT</b>.
      </p><p>
      I curricula di varie forme sono analizzati e organizzati in dati strutturati per facilitare la ricerca di candidati da parte dei recruiter.
      </p>
      `,
      table: `<p>I formati di file supportati sono <b>XLSX</b> e <b>CSV/TXT</b>.</p><p>
      Ecco alcuni prerequisiti e suggerimenti:
      <ul>
    <li>Per i file CSV o TXT, il delimitatore tra le colonne deve essere <em><b>TAB</b></em>.</li>
    <li>La prima riga deve contenere le intestazioni delle colonne.</li>
    <li>Le intestazioni delle colonne devono essere termini significativi per aiutare la comprensione del tuo LLM.
    È buona pratica affiancare sinonimi separati da una barra <i>'/'</i> e enumerare i valori usando parentesi, ad esempio: <i>'Genere/Sesso (maschio, femmina)'</i>.<p>
    Ecco alcuni esempi di intestazioni:<ol>
        <li>fornitore/venditore<b>'TAB'</b>Colore (Giallo, Blu, Marrone)<b>'TAB'</b>Sesso/Genere (maschio, femmina)<b>'TAB'</b>taglia (M, L, XL, XXL)</li>
        </ol>
        </p>
    </li>
    <li>Ogni riga nella tabella sarà trattata come un chunk.</li>
    </ul>`,
      picture: `
    <p>I file immagine sono supportati, con supporto video in arrivo.</p><p>
    Questo metodo utilizza un modello OCR per estrarre testi dalle immagini.
    </p><p>
    Se il testo estratto dal modello OCR è insufficiente, un LLM visivo specificato sarà usato per fornire una descrizione dell’immagine.
    </p>`,
      one: `
    <p>I formati di file supportati sono <b>DOCX, XLSX, XLS (Excel 97-2003), PDF, TXT</b>.
    </p><p>
    Questo metodo tratta ogni documento nella sua interezza come un chunk.
    </p><p>
    Applicabile quando si richiede al LLM di riassumere l’intero documento, purché possa gestire quella quantità di contesto.
    </p>`,
      knowledgeGraph: `<p>I formati di file supportati sono <b>DOCX, EXCEL, PPT, IMMAGINE, PDF, TXT, MD, JSON, EML</b>

<p>Questo approccio chunka i file usando il metodo 'naive'/'Generale'. Divide un documento in segmenti e poi combina segmenti adiacenti fino a superare la soglia di token specificata da 'Numero di token per chunk', a quel punto viene creato un chunk.</p>
<p>I chunk sono poi inviati al LLM per estrarre entità e relazioni per un knowledge graph e una mappa mentale.</p>
<p>Assicurati di impostare i <b>tipi di entità</b>.</p>`,
      tag: `<p>Una knowledge base che usa il metodo di chunking 'Tag' funziona come un set di tag. Altre knowledge base possono usarlo per taggare i propri chunk, e le query a queste knowledge base saranno anch’esse taggate usando questo set di tag.</p>
<p>La knowledge base che usa 'Tag' come metodo di chunking <b>NON</b> sarà coinvolta in un processo Retrieval-Augmented Generation (RAG).</p>
<p>Ogni chunk in questa knowledge base è una coppia descrizione-tag indipendente.</p>
<p>I formati di file supportati includono <b>XLSX</b> e <b>CSV/TXT</b>:</p>
<p>Se un file è in formato <b>XLSX</b>, deve contenere due colonne senza intestazioni: una per le descrizioni e l’altra per i nomi dei tag, con la colonna Descrizione prima della colonna Tag. Sono accettati più fogli, purché le colonne siano strutturate correttamente.</p>
<p>Se un file è in formato <b>CSV/TXT</b>, deve essere codificato in UTF-8 con TAB come delimitatore per separare descrizioni e tag.</p>
<p>In una colonna Tag, <b>la virgola</b> è usata per separare i tag.</p>
<i>Le righe di testo che non rispettano le regole sopra saranno ignorate.</i>
`,
      useRaptor: 'Usa RAPTOR per migliorare il retrieval',
      useRaptorTip:
        'Abilita RAPTOR per task di question-answering multi-hop. Vedi https://ragflow.io/docs/dev/enable_raptor per dettagli.',
      prompt: 'Prompt',
      promptTip:
        'Usa il prompt di sistema per descrivere il compito per il LLM, specificare come deve rispondere e delineare altri requisiti vari. Il prompt di sistema è spesso usato con chiavi (variabili), che servono come vari input di dati per il LLM. Usa una barra / o il pulsante (x) per mostrare le chiavi da usare.',
      promptMessage: 'Il prompt è obbligatorio',
      promptText: `Per favore riassumi i seguenti paragrafi. Fai attenzione ai numeri, non inventare nulla. Paragrafi come segue:
      {cluster_content}
Il contenuto sopra è quello che devi riassumere.`,
      maxToken: 'Token massimo',
      maxTokenTip: 'Il numero massimo di token per chunk di riassunto generato.',
      maxTokenMessage: 'Il token massimo è obbligatorio',
      threshold: 'Soglia',
      thresholdTip:
        'In RAPTOR, i chunk sono raggruppati per similarità semantica. La soglia imposta la similarità minima richiesta per raggruppare i chunk. Una soglia più alta significa meno chunk in ogni cluster, una più bassa significa di più.',
      thresholdMessage: 'La soglia è obbligatoria',
      maxCluster: 'Cluster massimo',
      maxClusterTip: 'Il numero massimo di cluster da creare.',
      maxClusterMessage: 'Il cluster massimo è obbligatorio',
      randomSeed: 'Seed casuale',
      randomSeedMessage: 'Il seed casuale è obbligatorio',
      entityTypes: 'Tipi di entità',
      vietnamese: 'Vietnamita',
      pageRank: 'Page rank',
      pageRankTip: `Puoi assegnare un punteggio PageRank più alto a specifiche knowledge base durante il retrieval. Il punteggio corrispondente viene aggiunto ai punteggi di similarità ibrida dei chunk recuperati da queste knowledge base, aumentando il loro ranking. Vedi https://ragflow.io/docs/dev/set_page_rank per dettagli.`,
      tagName: 'Tag',
      frequency: 'Frequenza',
      searchTags: 'Cerca tag',
      tagCloud: 'Cloud',
      tagTable: 'Tabella',
      tagSet: 'Set di tag',
      tagSetTip: `
     <p> Seleziona una o più knowledge base di tag per auto-taggare i chunk nella tua knowledge base. Vedi https://ragflow.io/docs/dev/use_tag_sets per dettagli.</p>
<p>La query utente sarà anche auto-taggata.</p>
Questa funzione di auto-tagging migliora il retrieval aggiungendo un ulteriore livello di conoscenza specifica del dominio al dataset esistente.
<p>Differenza tra auto-tag e auto-keyword:</p>
<ul>
  <li>Una knowledge base di tag è un set chiuso definito dall’utente, mentre le keyword estratte dal LLM possono essere considerate un set aperto.</li>
  <li>Devi caricare set di tag nei formati specificati prima di eseguire la funzione di auto-tag.</li>
  <li>La funzione auto-keyword dipende dal LLM e consuma un numero significativo di token.</li>
</ul>
      `,
      topnTags: 'Top-N Tags',
      tags: 'Tag',
      addTag: 'Aggiungi tag',
      useGraphRag: 'Estrai knowledge graph',
      useGraphRagTip:
        'Costruisci un knowledge graph sui chunk dei file della knowledge base corrente per migliorare il question-answering multi-hop con logica annidata. Vedi https://ragflow.io/docs/dev/construct_knowledge_graph per dettagli.',
      graphRagMethod: 'Metodo',
      graphRagMethodTip: `Light: (Predefinito) Usa prompt forniti da github.com/HKUDS/LightRAG per estrarre entità e relazioni. Questa opzione consuma meno token, meno memoria e meno risorse computazionali.</br>
        General: Usa prompt forniti da github.com/microsoft/graphrag per estrarre entità e relazioni`,
      resolution: 'Risoluzione entità',
      resolutionTip: `Un interruttore di deduplicazione entità. Quando abilitato, il LLM combinerà entità simili - es. '2025' e 'l’anno 2025', o 'IT' e 'Information Technology' - per costruire un grafo più accurato`,
      community: 'Generazione report comunità',
      communityTip:
        'In un knowledge graph, una comunità è un cluster di entità collegate da relazioni. Puoi far generare al LLM un abstract per ogni comunità, noto come report comunità. Vedi qui per maggiori informazioni: https://www.microsoft.com/en-us/research/blog/graphrag-improving-global-search-via-dynamic-community-selection/',
      theDocumentBeingParsedCannotBeDeleted:
        'Il documento in fase di parsing non può essere eliminato',
    },
    chunk: {},
    chat: {},
    setting: {},
    message: {},
    fileManager: {},
    flow: {},
    llmTools: {},
  },
};
