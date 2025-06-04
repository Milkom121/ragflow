# Mappatura API Backend RagFlow

## Autenticazione e Gestione Utenti

### Endpoint Principali (da api/apps/user_app.py)

- **POST /login**
  - Descrizione: Login utente con email e password.
  - Parametri: email, password (criptata).
  - Risposte: 200 OK con dati utente e token, 401 errore autenticazione.
  - Note: Supporta anche login OAuth tramite canali esterni.

- **GET /login/channels**
  - Descrizione: Recupera canali di autenticazione OAuth supportati.

- **GET /login/<channel>**
  - Descrizione: Inizia flusso OAuth per canale specificato.

- **GET /oauth/callback/<channel>**
  - Descrizione: Callback OAuth dinamico per vari canali.

- **GET /logout**
  - Descrizione: Logout utente autenticato.

- **POST /setting**
  - Descrizione: Aggiorna impostazioni utente (nickname, email, password).

- **GET /info**
  - Descrizione: Recupera informazioni profilo utente autenticato.

- **POST /register**
  - Descrizione: Registrazione nuovo utente con nickname, email, password.

- **GET /tenant_info**
  - Descrizione: Recupera informazioni tenant associato all’utente.

- **POST /set_tenant_info**
  - Descrizione: Aggiorna informazioni tenant.

### Note

- Autenticazione gestita con Flask-Login e token UUID.
- Password criptate e decriptate con funzioni custom.
- Supporto OAuth per GitHub, Feishu, altri canali.
- Gestione utenti multi-tenant con ruoli e permessi.

---

## Chat

### Endpoint Principali (da api/apps/sdk/chat.py)

- **POST /chats**
  - Descrizione: Crea una nuova chat.
  - Parametri: dataset_ids, llm, prompt, nome chat, ecc.
  - Note: Validazione embedding model, prompt config, proprietà tenant.

- **PUT /chats/<chat_id>**
  - Descrizione: Aggiorna chat esistente.
  - Parametri: dataset_ids, llm, prompt, nome chat, ecc.
  - Note: Controllo proprietà, validazione duplicati.

- **DELETE /chats**
  - Descrizione: Elimina una o più chat.
  - Parametri: lista di chat id.

- **GET /chats**
  - Descrizione: Lista chat con filtri, paginazione e ordinamento.
  - Parametri: id, nome, pagina, dimensione pagina, ordinamento.

---

## Knowledge Base

### Endpoint Principali (da api/apps/kb_app.py)

- **POST /create**
  - Descrizione: Crea una nuova knowledge base.
  - Parametri: nome knowledge base.

- **POST /update**
  - Descrizione: Aggiorna knowledge base esistente.
  - Parametri: kb_id, nome, descrizione, parser_id.

- **GET /detail**
  - Descrizione: Recupera dettagli knowledge base.
  - Parametri: kb_id.

- **POST /list**
  - Descrizione: Lista knowledge base con filtri e paginazione.
  - Parametri: owner_ids, keywords, pagina, dimensione pagina.

- **POST /rm**
  - Descrizione: Rimuove knowledge base.
  - Parametri: kb_id.

- **GET /<kb_id>/tags**
  - Descrizione: Lista tag associati a knowledge base.

- **GET /tags**
  - Descrizione: Lista tag da più knowledge base.
  - Parametri: kb_ids.

- **POST /<kb_id>/rm_tags**
  - Descrizione: Rimuove tag da knowledge base.
  - Parametri: lista tag.

- **POST /<kb_id>/rename_tag**
  - Descrizione: Rinomina tag in knowledge base.
  - Parametri: from_tag, to_tag.

- **GET /<kb_id>/knowledge_graph**
  - Descrizione: Recupera grafo di conoscenza associato.

- **DELETE /<kb_id>/knowledge_graph**
  - Descrizione: Elimina grafo di conoscenza associato.

---

## Documenti

### Endpoint Principali (da api/apps/document_app.py)

- **POST /upload**
  - Descrizione: Upload file per knowledge base.
  - Parametri: kb_id, file.

- **POST /web_crawl**
  - Descrizione: Scarica e converte pagina web in PDF per knowledge base.
  - Parametri: kb_id, nome, url.

- **POST /create**
  - Descrizione: Crea documento virtuale.
  - Parametri: kb_id, nome documento.

- **POST /list**
  - Descrizione: Lista documenti knowledge base.
  - Parametri: kb_id, keywords, pagina, dimensione pagina, filtri.

- **POST /infos**
  - Descrizione: Recupera info dettagliate documenti.
  - Parametri: lista doc_ids.

- **GET /thumbnails**
  - Descrizione: Recupera miniature documenti.
  - Parametri: lista doc_ids.

- **POST /change_status**
  - Descrizione: Cambia stato documento.
  - Parametri: doc_id, status.

- **POST /rm**
  - Descrizione: Rimuove documenti.
  - Parametri: lista doc_id.

- **POST /run**
  - Descrizione: Avvia/ferma parsing documenti.
  - Parametri: lista doc_ids, run.

- **POST /rename**
  - Descrizione: Rinomina documento.
  - Parametri: doc_id, nome.

- **GET /get/<doc_id>**
  - Descrizione: Recupera contenuto documento.

- **POST /change_parser**
  - Descrizione: Cambia parser documento.
  - Parametri: doc_id, parser_id.

- **GET /image/<image_id>**
  - Descrizione: Recupera immagine associata documento.

- **POST /upload_and_parse**
  - Descrizione: Upload e parsing file per conversazione.
  - Parametri: conversation_id, file.

- **POST /parse**
  - Descrizione: Parsing file o URL.

- **POST /set_meta**
  - Descrizione: Imposta metadati JSON su documento.
  - Parametri: doc_id, meta.

---

## Dialoghi

### Endpoint Principali (da api/apps/dialog_app.py)

- **POST /set**
  - Descrizione: Crea o aggiorna dialogo.
  - Parametri: dialog_id (opzionale), nome, descrizione, LLM, knowledge base, prompt, ecc.

- **GET /get**
  - Descrizione: Recupera dettagli dialogo.
  - Parametri: dialog_id.

- **GET /list**
  - Descrizione: Lista dialoghi utente.

- **POST /rm**
  - Descrizione: Rimuove dialoghi.
  - Parametri: lista dialog_ids.

---

## Conversazioni

### Endpoint Principali (da api/apps/conversation_app.py)

- **POST /set**
  - Descrizione: Crea o aggiorna conversazione.
  - Parametri: conversation_id (opzionale), dialog_id, nome, messaggi, ecc.

- **GET /get**
  - Descrizione: Recupera dettagli conversazione.
  - Parametri: conversation_id.

- **GET /getsse/<dialog_id>**
  - Descrizione: Recupera dati per Server-Sent Events.

- **POST /rm**
  - Descrizione: Rimuove conversazioni.
  - Parametri: lista conversation_ids.

- **GET /list**
  - Descrizione: Lista conversazioni di un dialogo.
  - Parametri: dialog_id.

- **POST /completion**
  - Descrizione: Genera risposte AI in streaming o singole.
  - Parametri: conversation_id, messaggi.

- **POST /tts**
  - Descrizione: Genera audio da testo (Text-to-Speech).
  - Parametri: testo.

- **POST /delete_msg**
  - Descrizione: Elimina messaggio da conversazione.
  - Parametri: conversation_id, message_id.

- **POST /thumbup**
  - Descrizione: Gestisce feedback positivo/negativo su messaggi AI.
  - Parametri: conversation_id, message_id, feedback.

- **POST /ask**
  - Descrizione: Genera risposte a domande specifiche con streaming.
  - Parametri: domanda, kb_ids.

- **POST /mindmap**
  - Descrizione: Genera mappe mentali da domande.
  - Parametri: domanda, kb_ids.

- **POST /related_questions**
  - Descrizione: Genera domande correlate per migliorare la ricerca.
  - Parametri: domanda.

---

Questo documento sarà aggiornato progressivamente durante l’analisi e lo sviluppo.
