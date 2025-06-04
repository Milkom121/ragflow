# Design della RagFlow User WebApp

## Principi di Design

- **Modernità:** UI pulita, minimale, ispirata a standard attuali (Material, Ant Design, Tailwind).
- **Intuitività:** Navigazione semplice, feedback chiari, onboarding rapido.
- **Accessibilità:** Contrasto elevato, supporto tastiera, ARIA, responsive.
- **Branding:** Colori e logo personalizzabili per il cliente.

---

## Struttura delle Pagine

1. **Login/Registrazione**
   - Form centrato, validazione in tempo reale, feedback errori.
   - Link a recupero password.
2. **Dashboard**
   - Benvenuto, stato utente, accesso rapido a chat e knowledge base.
3. **Chat AI**
   - Area messaggi, input persistente, invio con Enter/Ctrl+Enter.
   - Messaggi AI con citazioni, riferimenti, evidenziazione fonti.
   - Indicatori di caricamento, errori, retry.
4. **Knowledge Base**
   - Ricerca documenti, filtri, anteprima risultati.
   - Visualizzazione dettagliata con evidenziazione chunk/citazioni.
5. **Profilo Utente**
   - Visualizzazione/modifica dati, cambio password, logout.
6. **Error/Notifiche**
   - Pagina 404, errori di autenticazione, notifiche toast.

---

## Componenti Chiave

- **Navbar/Sidebar:** Navigazione principale, logo, nome utente, link logout.
- **Card/Panel:** Per dashboard, risultati ricerca, dettagli documento.
- **Bottoni:** Primari, secondari, disabilitati, con icone.
- **Modali:** Conferme, dettagli, errori critici.
- **Loader/Spinner:** Per feedback asincroni.
- **Tooltip/Popover:** Aiuti contestuali.

---

## Palette Colori (esempio)

Prevedi da principio l'implementazione della Dark Mode

- Primario: #4e6b99
- Secondario: #f5f5f5
- Success: #4caf50
- Warning: #ff9800
- Danger: #f44336
- Background: #ffffff
- Testo: #222222

---

## Tipografia

- Font principale: Inter, Roboto, Arial, sans-serif
- Titoli: Bold, dimensione crescente (H1-H4)
- Testo: 16px base, 14px secondario

---

## Linee Guida di Navigazione

- Navbar fissa in alto o sidebar a sinistra (responsive).
- Breadcrumb per pagine secondarie.
- Feedback visivo su elementi attivi/focus.
- Navigazione mobile: hamburger menu, swipe per sidebar.

---

## Responsive Design

- Mobile first, breakpoint principali: 480px, 768px, 1024px, 1440px.
- Test su Chrome, Firefox, Safari, Edge.

---

## Accessibilità

- Contrasto minimo WCAG AA.
- Tutti i form e bottoni accessibili da tastiera.
- ARIA label su componenti interattivi.
- Focus visibile.

---

## Esempio di Flusso Utente

1. Login → Dashboard → Chat AI → Visualizza citazioni → Knowledge Base → Profilo → Logout

---

## Note Operative

- Tutte le scelte di design vanno validate con almeno uno stakeholder.
- Il design può essere adattato/brandizzato per il cliente finale.
- Wireframe e mockup dettagliati possono essere allegati in /docs/ui.
