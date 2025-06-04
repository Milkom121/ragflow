# Istruzioni per l'uso di questo documento

- Al termine di ogni task è obbligatorio scrivere ed eseguire dei test funzionali. I test devono passare con successo per poter procedere al task successivo.
- Dopo ogni task, è necessario aggiornare il documento roadmap.md scrivendo un breve report sotto la fase corrispondente del piano di lavoro, descrivendo i risultati dei test e le eventuali problematiche riscontrate. Usa colori ed emoji nel testo per rendere la lettura più chiara possibile
- Lo scopo è mantenere una traccia chiara e aggiornata di tutto il lavoro svolto, facilitando la gestione

---

# Roadmap per Architettura a Due Livelli: Admin Platform + User WebApp

Questa roadmap descrive il piano di sviluppo per una piattaforma RagFlow Admin (gestione utenti, permessi, monitoraggio) e una User WebApp dedicata agli utenti finali (dipendenti), entrambe collegate a un backend unificato.

---

## Milestone 1: Analisi e Design Architetturale

### Fase 1.1: Analisi Requisiti e API

**Obiettivo:** Definire in modo chiaro i requisiti funzionali e tecnici, mappare le API esistenti, identificare gap e opportunità di estensione.

- **Task 1.1.1:** Analisi delle API esistenti (guarda file api_mappatura.md)
  - Sotto-task:
    - Raccogliere documentazione e/o utilizzare strumenti come Swagger/Postman per esplorare le API.
    - Elencare endpoint per autenticazione, gestione utenti, chat, knowledge base, upload documenti.
    - Annotare parametri, metodi, permessi richiesti, payload di request/response.
  - _User Story:_ Come sviluppatore voglio una mappa delle API così da sapere cosa riusare o estendere.
  - Criteri di accettazione: Documento di mappatura API condiviso nel repository.
  - Deliverable: Tabella/diagramma delle API, note su endpoint da estendere/creare.
  - Strumenti: Swagger, Postman, markdown, diagrammi UML.

- **Task 1.1.2:** Definizione modelli dati (utenti, ruoli, permessi, sessioni)
  - Sotto-task:
    - Analizzare i modelli attuali (DB, ORM, serializzatori).
    - Definire attributi minimi per ogni entità (es. User: id, email, ruolo, stato, ecc.).
    - Mappare relazioni tra entità (es. User-Role, User-Permission).
    - Proporre eventuali modifiche/estensioni.
  - _User Story:_ Come admin voglio definire ruoli e permessi per controllare l’accesso alle funzionalità.
  - Criteri di accettazione: Schema dati validato dal team.
  - Deliverable: Diagramma ER, descrizione entità e relazioni.
  - Strumenti: dbdiagram.io, UML, markdown.

- **Task 1.1.3:** Progettazione flusso autenticazione e autorizzazione (JWT/sessioni)
  - Sotto-task:
    - Analizzare il flusso attuale di login/logout/refresh.
    - Definire il ciclo di vita del token/sessione.
    - Specificare i permessi richiesti per ogni endpoint.
    - Proporre best practice per sicurezza (es. scadenza token, refresh, revoca, storage sicuro).
  - _User Story:_ Come utente voglio autenticarmi in modo sicuro per accedere alle mie risorse.
  - Criteri di accettazione: Diagramma di sequenza del flusso auth, checklist sicurezza.
  - Deliverable: Diagramma di sequenza, documento di policy auth.
  - Strumenti: UML sequence diagram, markdown.

- **Task 1.1.4:** Raccolta requisiti User App e Admin Platform
  - Sotto-task:
    - Intervistare stakeholder o raccogliere user story aggiuntive.
    - Definire casi d’uso principali per User App e Admin Platform.
    - Prioritizzare requisiti (must, should, could).
  - _User Story:_ Come stakeholder voglio che le funzionalità chiave siano chiare e prioritarie.
  - Criteri di accettazione: Lista user story e casi d’uso validata.
  - Deliverable: Documento user story/casi d’uso.
  - Strumenti: markdown, Google Docs, Trello/Jira.

**Note operative:**
- Ogni deliverable va salvato in una cartella “/docs/analisi” o simile.
- Checklist di validazione da condividere con il team prima di passare alla milestone 2.

---

### Report Avanzamento Fase 1.1: Analisi Requisiti e API 🚦🟢

- La mappatura delle API è stata completata e documentata in `docs/analisi/api_mappatura.md`.
- ✅ Test funzionali endpoint `/v1/user/login` e `/v1/user/login/channels` creati e superati con successo.
- 🧪 Validazione formale eseguita tramite script manuale Python (`validate_login_endpoints.py`): 
  - L’endpoint `/v1/user/login` risponde correttamente ma l’utente inserito non è registrato (`Email:  is not registered!`).
  - L’endpoint `/v1/user/login/channels` risponde correttamente con `data: []`.
- 🟢 Gli endpoint sono raggiungibili e il backend risponde come atteso. 
- ⚠️ Da registrare un utente valido per testare completamente il login.
- Prossimi passi: avviare la Fase 1.2 (Prototipazione UI) ✨.
- Nessun problema critico bloccante riscontrato, validazione semplificata documentata! 🚀

---


---

### Fase 1.2: Prototipazione UI

**Obiettivo:** Definire e validare le principali interfacce utente della User WebApp, garantendo un frontend moderno, organizzato e intuitivo, secondo quanto specificato nel file [ragflow-user-design.md](./ragflow-user-design.md).

- **Task 1.2.1:** Design completo User App (vedi ragflow-user-design.md)
  - Sotto-task:
    - Definire principi di UX/UI, struttura pagine, componenti chiave, palette colori, tipografia, navigazione, responsive, accessibilità.
    - Produrre wireframe e mockup dettagliati (carta, Figma, Balsamiq, ecc.).
    - Validare il design con almeno uno stakeholder.
    - Documentare tutto in [ragflow-user-design.md](./ragflow-user-design.md).
  - _User Story:_ Come utente voglio un’interfaccia moderna, organizzata e intuitiva per accedere e usare la chat AI e le altre funzionalità.
  - Criteri di accettazione: Design completo, validato e versionato.
  - Deliverable: File ragflow-user-design.md, wireframe (PNG, PDF, Figma link).
  - Strumenti: Figma, Balsamiq, markdown, carta/scanner.

- **Task 1.2.2:** Definizione linee guida UI/UX (con riferimento a ragflow-user-design.md)
  - Sotto-task:
    - Stabilire palette colori, font, spacing, componenti base, pattern di navigazione e feedback utente, come da design.
    - Documentare le scelte in un mini design system e in ragflow-user-design.md.
  - _User Story:_ Come sviluppatore voglio linee guida chiare e centralizzate per garantire coerenza visiva e usabilità.
  - Criteri di accettazione: Mini design system condiviso e integrato nel file di design.
  - Deliverable: Documento linee guida UI/UX in ragflow-user-design.md.
  - Strumenti: Figma, markdown.

**Note operative:**
- Il design completo e tutte le linee guida sono definite e versionate in [ragflow-user-design.md](./ragflow-user-design.md).
- Tutti i wireframe e mockup vanno salvati in “/docs/ui” o simile.
- Validazione con almeno uno stakeholder prima di procedere.

---

## Milestone 2: Refactoring e Estensione Backend

### Fase 2.1: Gestione Utenti, Ruoli e Permessi

**Obiettivo:** Garantire una gestione robusta e sicura di utenti, ruoli e permessi, con API CRUD e middleware di autorizzazione.

- **Task 2.1.1:** Implementare/estendere API per CRUD utenti, ruoli, permessi
  - Sotto-task:
    - Analizzare i modelli dati definiti nella milestone 1.
    - Implementare endpoint RESTful per creazione, lettura, aggiornamento, cancellazione di utenti, ruoli, permessi.
    - Validare input e output (serializzatori/schema).
    - Gestire errori e casi limite (es. ruoli duplicati, permessi non validi).
    - Scrivere test automatici per ogni endpoint.
  - _User Story:_ Come admin voglio creare/modificare/cancellare utenti e assegnare ruoli.
  - Criteri di accettazione: Tutti gli endpoint CRUD funzionano e sono coperti da test.
  - Deliverable: Codice API, test, documentazione endpoint.
  - Strumenti: Flask/FastAPI/Django, Pytest, OpenAPI/Swagger.

- **Task 2.1.2:** Middleware di autorizzazione su ogni endpoint protetto
  - Sotto-task:
    - Definire decoratori/middleware per controllo permessi su ogni route.
    - Mappare permessi richiesti per ogni endpoint.
    - Gestire risposte standard per accessi negati.
    - Testare accessi con diversi ruoli/permessi.
  - _User Story:_ Come backend voglio bloccare accessi non autorizzati per garantire la sicurezza.
  - Criteri di accettazione: Tutti gli endpoint protetti, test superati.
  - Deliverable: Middleware, test, documentazione permessi.
  - Strumenti: Flask/FastAPI middleware, Pytest.

**Note operative:**
- Tutte le modifiche devono essere versionate e documentate.
- Checklist di test da eseguire prima di procedere alla fase successiva.

---

### Fase 2.2: Autenticazione e Sessioni

**Obiettivo:** Implementare un sistema di autenticazione sicuro e gestire il ciclo di vita delle sessioni/token.

- **Task 2.2.1:** Implementare autenticazione sicura (JWT/sessioni)
  - Sotto-task:
    - Scegliere tra JWT, sessioni server-side o soluzione ibrida.
    - Implementare endpoint di login, logout, refresh token.
    - Gestire la scadenza e la revoca dei token/sessioni.
    - Proteggere le credenziali (hashing password, HTTPS, ecc.).
    - Scrivere test di autenticazione e gestione sessioni.
  - _User Story:_ Come utente voglio autenticarmi e mantenere la sessione attiva in modo sicuro.
  - Criteri di accettazione: Login/logout/refresh funzionanti, test superati.
  - Deliverable: Codice auth, test, documentazione flusso.
  - Strumenti: PyJWT, Flask-Login, bcrypt, Pytest.

- **Task 2.2.2:** Endpoint per login, logout, refresh token
  - Sotto-task:
    - Definire payload e risposte standard.
    - Gestire errori comuni (credenziali errate, token scaduto, ecc.).
    - Aggiornare la documentazione API.
  - _User Story:_ Come utente voglio poter accedere, uscire e mantenere la sessione senza problemi.
  - Criteri di accettazione: Endpoint documentati e testati.
  - Deliverable: Endpoint, test, documentazione.
  - Strumenti: OpenAPI/Swagger, Pytest.

**Note operative:**
- Tutte le password devono essere sempre hashate.
- I token devono avere scadenza e supportare revoca.
- Validare la sicurezza tramite test automatici e, se possibile, penetration test.

---

### Fase 2.3: API per User App

**Obiettivo:** Esporre tutte le API necessarie alla User WebApp per interagire con la piattaforma (chat, knowledge base, upload documenti, ecc.).

- **Task 2.3.1:** Esporre endpoint per chat, knowledge base, upload documenti, ecc.
  - Sotto-task:
    - Analizzare i requisiti raccolti nella milestone 1.
    - Implementare endpoint RESTful per chat AI, knowledge base, upload/download documenti.
    - Applicare autorizzazione e validazione su ogni endpoint.
    - Scrivere test automatici per ogni funzionalità.
    - Aggiornare la documentazione API.
  - _User Story:_ Come utente voglio interagire con la chat AI e caricare documenti tramite la User App.
  - Criteri di accettazione: Tutti gli endpoint funzionano, sono protetti e documentati.
  - Deliverable: Codice API, test, documentazione.
  - Strumenti: Flask/FastAPI, Pytest, OpenAPI/Swagger.

**Note operative:**
- Tutte le API devono essere versionate e documentate.
- Validare la copertura dei test e la sicurezza degli endpoint.

---

## Milestone 3: Sviluppo User WebApp

### Fase 3.1: Setup Progetto e Autenticazione

**Obiettivo:** Creare la base del progetto frontend, integrare l’autenticazione e la gestione sicura delle sessioni.

- **Task 3.1.1:** Inizializzare progetto frontend (React/TS o stack scelto)
  - Sotto-task:
    - Scegliere stack tecnologico (React/TS, Next.js, Vite, ecc.).
    - Creare repository e struttura cartelle (src, components, pages, services, ecc.).
    - Configurare strumenti di sviluppo (linter, formatter, test runner, ecc.).
    - Documentare setup e convenzioni di progetto.
  - _User Story:_ Come sviluppatore voglio uno scaffold pronto per la User App.
  - Criteri di accettazione: Progetto avviabile, struttura chiara, README aggiornato.
  - Deliverable: Codice base, README, configurazioni.
  - Strumenti: create-react-app, Vite, ESLint, Prettier, Jest.

- **Task 3.1.2:** Implementare schermate di login/registrazione e gestione token
  - Sotto-task:
    - Creare form di login e registrazione con validazione.
    - Gestire chiamate API per autenticazione e registrazione.
    - Salvare token/sessione in modo sicuro (es. HttpOnly cookie, localStorage con best practice).
    - Gestire errori di autenticazione e feedback utente.
    - Scrivere test di integrazione per i flussi auth.
  - _User Story:_ Come utente voglio autenticarmi e accedere alle funzionalità protette.
  - Criteri di accettazione: Login/registrazione funzionanti, test superati.
  - Deliverable: Componenti login/registrazione, gestione token, test.
  - Strumenti: React, Axios/Fetch, React Testing Library.

**Note operative:**
- Tutte le dipendenze e le configurazioni vanno documentate.
- Validare i flussi auth con backend mock o reale.

---

### Fase 3.2: Funzionalità Principali

**Obiettivo:** Implementare le funzionalità core della User App: chat AI, knowledge base, gestione profilo.

- **Task 3.2.1:** Implementare chat AI e interazione knowledge base
  - Sotto-task:
    - Creare componenti UI per chat e knowledge base.
    - Gestire chiamate API per invio/ricezione messaggi e ricerca documenti.
    - Visualizzare risposte AI, citazioni, riferimenti.
    - Gestire errori e loading state.
    - Scrivere test di integrazione.
  - _User Story:_ Come utente voglio chattare con l’AI e consultare la knowledge base.
  - Criteri di accettazione: Chat e knowledge base funzionanti, test superati.
  - Deliverable: Componenti chat/KB, test.
  - Strumenti: React, WebSocket/Axios, React Testing Library.

- **Task 3.2.2:** Gestione profilo utente e logout
  - Sotto-task:
    - Creare pagina profilo con visualizzazione e modifica dati utente.
    - Implementare logout sicuro (clear token/sessione).
    - Gestire feedback e notifiche.
    - Scrivere test di integrazione.
  - _User Story:_ Come utente voglio gestire il mio profilo e uscire in sicurezza.
  - Criteri di accettazione: Profilo e logout funzionanti, test superati.
  - Deliverable: Componenti profilo/logout, test.
  - Strumenti: React, Axios, React Testing Library.

**Note operative:**
- Tutte le chiamate API devono includere il token di autenticazione.
- Validare la UX con almeno uno stakeholder.

---

### Fase 3.3: UI/UX e Sicurezza

**Obiettivo:** Garantire un’interfaccia moderna, accessibile e sicura per l’utente finale.

- **Task 3.3.1:** UI responsive e accessibile
  - Sotto-task:
    - Applicare linee guida UI/UX definite nella milestone 1.
    - Testare la UI su diversi dispositivi e browser.
    - Implementare accessibilità (ARIA, contrasto, navigazione tastiera).
    - Scrivere test end-to-end (E2E) per i flussi principali.
  - _User Story:_ Come utente voglio un’interfaccia usabile da qualsiasi dispositivo.
  - Criteri di accettazione: UI responsive, accessibile, test E2E superati.
  - Deliverable: UI responsive, report test E2E.
  - Strumenti: Tailwind/Chakra/AntD, Cypress/Playwright.

- **Task 3.3.2:** Gestione sicura delle credenziali lato client
  - Sotto-task:
    - Salvare token/sessione secondo best practice (evitare XSS/CSRF).
    - Validare la sicurezza tramite audit e test automatici.
    - Documentare le scelte di sicurezza.
  - _User Story:_ Come utente voglio che i miei dati siano protetti anche sul frontend.
  - Criteri di accettazione: Nessuna vulnerabilità nota, audit superato.
  - Deliverable: Report sicurezza, documentazione.
  - Strumenti: ESLint, npm audit, OWASP cheat sheet.

**Note operative:**
- Tutte le scelte di sicurezza e UX vanno documentate.
- Validare la UI con almeno uno stakeholder prima del rilascio.

---

## Milestone 4: Integrazione, Test e Sicurezza

### Fase 4.1: Integrazione End-to-End

**Obiettivo:** Validare l’integrazione tra User App, Admin Platform e backend, garantendo la coerenza e la sicurezza dei flussi.

- **Task 4.1.1:** Collegare User App al backend tramite API protette
  - Sotto-task:
    - Configurare endpoint e variabili ambiente per ambiente di test/staging.
    - Validare autenticazione e autorizzazione su tutte le chiamate API.
    - Testare i flussi principali (login, chat, knowledge base, profilo, logout).
    - Gestire errori di integrazione e casi limite.
    - Documentare i flussi end-to-end.
  - _User Story:_ Come utente voglio che tutte le mie azioni siano processate in sicurezza dal backend.
  - Criteri di accettazione: Tutti i flussi funzionano end-to-end, documentazione aggiornata.
  - Deliverable: Report di integrazione, checklist flussi.
  - Strumenti: Postman, Cypress, Docker Compose, markdown.

- **Task 4.1.2:** Test funzionali multi-utente e simulazione carico
  - Sotto-task:
    - Creare script per simulare accesso e interazione di più utenti contemporanei.
    - Eseguire test di carico su API e frontend.
    - Analizzare performance, tempi di risposta, errori.
    - Ottimizzare configurazioni e risorse se necessario.
    - Documentare risultati e azioni correttive.
  - _User Story:_ Come admin voglio essere sicuro che il sistema regga più utenti contemporanei.
  - Criteri di accettazione: Test di carico superati, performance accettabili.
  - Deliverable: Script test, report performance.
  - Strumenti: Locust, JMeter, Cypress, Docker Compose.

**Note operative:**
- Tutti i test devono essere ripetibili e versionati.
- Validare i risultati con almeno uno stakeholder.

---

### Fase 4.2: Sicurezza e Logging

**Obiettivo:** Garantire la sicurezza, la tracciabilità e la resilienza del sistema in produzione.

- **Task 4.2.1:** Rate limiting, logging accessi, audit trail
  - Sotto-task:
    - Implementare rate limiting su API critiche.
    - Configurare logging accessi e azioni sensibili (login, modifica permessi, upload documenti).
    - Abilitare audit trail per operazioni amministrative.
    - Testare la persistenza e la consultabilità dei log.
    - Documentare policy di logging e audit.
  - _User Story:_ Come admin voglio monitorare accessi e prevenire abusi.
  - Criteri di accettazione: Logging e audit attivi, log consultabili.
  - Deliverable: Configurazioni logging, report audit.
  - Strumenti: Python logging, ELK stack, Sentry, markdown.

- **Task 4.2.2:** Test di sicurezza (sandbox, permessi, sessioni)
  - Sotto-task:
    - Eseguire test automatici e manuali su sandbox, permessi, gestione sessioni.
    - Simulare attacchi comuni (XSS, CSRF, privilege escalation, brute force).
    - Validare la sicurezza di token, sessioni, upload documenti.
    - Correggere eventuali vulnerabilità rilevate.
    - Documentare risultati e azioni correttive.
  - _User Story:_ Come sviluppatore voglio garantire che non ci siano vulnerabilità note.
  - Criteri di accettazione: Nessuna vulnerabilità critica, report sicurezza.
  - Deliverable: Script test sicurezza, report finale.
  - Strumenti: OWASP ZAP, pytest, npm audit, markdown.

**Note operative:**
- Tutti i log e i report di sicurezza vanno archiviati in modo sicuro.
- Validare la sicurezza con almeno uno stakeholder prima del rilascio.

---

## Milestone 5: Deployment, Documentazione e Supporto

### Fase 5.1: Deployment

**Obiettivo:** Garantire un deployment affidabile, ripetibile e documentato per Admin Platform e User WebApp.

- **Task 5.1.1:** Script di deploy separati per Admin e User App
  - Sotto-task:
    - Scrivere script di build e deploy per Admin Platform (Docker, bash, batch, ecc.).
    - Scrivere script di build e deploy per User WebApp (Docker, npm, ecc.).
    - Testare i deployment su ambienti di staging e produzione.
    - Automatizzare rollback e aggiornamenti.
    - Documentare le procedure di deploy.
  - _User Story:_ Come devops voglio poter installare e aggiornare le app in modo indipendente.
  - Criteri di accettazione: Script funzionanti, testati e documentati.
  - Deliverable: Script deploy, guida deploy.
  - Strumenti: Docker Compose, bash, npm, CI/CD (GitHub Actions, GitLab CI).

- **Task 5.1.2:** Configurazione ambiente (variabili, chiavi, endpoint)
  - Sotto-task:
    - Definire file di configurazione per ogni ambiente (dev, staging, prod).
    - Gestire variabili sensibili (API key, secret, endpoint) in modo sicuro.
    - Documentare le configurazioni richieste e le best practice.
    - Validare la configurazione tramite checklist.
  - _User Story:_ Come devops voglio gestire facilmente le configurazioni per ogni ambiente.
  - Criteri di accettazione: Configurazioni chiare, sicure e documentate.
  - Deliverable: File config, guida configurazione.
  - Strumenti: .env, YAML, Docker secrets, markdown.

**Note operative:**
- Tutti gli script e le configurazioni vanno versionati e testati.
- Validare i deployment con almeno uno stakeholder.

---

### Fase 5.2: Documentazione e Supporto

**Obiettivo:** Fornire documentazione completa e supporto efficace per utenti, admin e cliente finale.

- **Task 5.2.1:** Aggiornare la documentazione tecnica e utente
  - Sotto-task:
    - Scrivere/aggiornare guide tecniche per installazione, configurazione, troubleshooting.
    - Scrivere manuali utente per Admin Platform e User WebApp.
    - Creare FAQ e guide rapide.
    - Versionare e pubblicare la documentazione (es. su GitHub Wiki, ReadTheDocs).
  - _User Story:_ Come utente/admin voglio guide chiare per usare e gestire il sistema.
  - Criteri di accettazione: Documentazione aggiornata, accessibile e validata.
  - Deliverable: Manuali, guide, FAQ.
  - Strumenti: markdown, GitHub Wiki, ReadTheDocs.

- **Task 5.2.2:** Supporto al cliente per installazione e configurazione
  - Sotto-task:
    - Preparare checklist di installazione e configurazione.
    - Fornire supporto remoto (call, ticket, email) durante la messa in opera.
    - Raccogliere feedback e migliorare la documentazione.
    - Documentare eventuali problemi e soluzioni.
  - _User Story:_ Come cliente voglio ricevere assistenza per l’installazione e la messa in opera.
  - Criteri di accettazione: Cliente autonomo nell’uso, feedback positivo.
  - Deliverable: Checklist, report supporto, miglioramenti doc.
  - Strumenti: markdown, ticketing, call, email.

**Note operative:**
- Tutta la documentazione va versionata e aggiornata a ogni release.
- Validare la chiarezza e la completezza con almeno uno stakeholder.

---

# Note Generali

- Ogni task deve essere completato con test funzionali che ne confermino il corretto funzionamento.
- Dopo ogni task, aggiornare questo documento con un breve report sullo stato di avanzamento e eventuali problemi riscontrati.
- Lo scopo è mantenere una traccia chiara e aggiornata di tutto il lavoro svolto, facilitando la gestione del progetto e la comunicazione con il cliente.

---
