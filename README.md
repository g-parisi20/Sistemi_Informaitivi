# 🏠 Predizione Prezzo al Metro Quadro - Sindian, Nuova Taipei

Questa applicazione web consente agli utenti di stimare il prezzo al metro quadro di un immobile nella regione di **Sindian**, **Nuova Taipei**, **Taiwan**, utilizzando delle **regressioni lineare multipla** basate sul **Real Estate Valuation Data Set**.

## 📊 Dataset

Il dataset utilizzato è il **Real estate valuation data set** reso disponibile dall’UCI Machine Learning Repository:  
🔗 [UCI Real Estate Dataset](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set)

### Variabili:

- **X1**: Data della transazione (ignorata nei modelli)
- **X2**: Età dell'immobile (anni)
- **X3**: Distanza dalla stazione MRT più vicina (metri)
- **X4**: Numero di minimarket nelle vicinanze
- **X5**: Latitudine
- **X6**: Longitudine
- **Y**: Prezzo al metro quadro dell’immobile

## 🧠 Modelli

Ci sono due modelli lineari basati sui seguenti regressori:

1. **Latitudine e Longitudine** → il modello predice il prezzo basandosi sulla posizione geografica.
   > ⚠️ Qui i valori inseriti devono rientrare nei limiti del dataset.
2. **Età, Distanza MRT, N. Minimarket** → il modello predice in base a caratteristiche strutturali e infrastrutturali.


## 🚀 Eseguire l'app
Comandi per macOS con python3 installato

### 0. Creazione ambiente virtuale
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```

### 1. Clona il repository
```bash
git clone https://github.com/g-parisi20/Sistemi_Informaitivi.git
```
```bash
cd Sistemi_Informaitivi
```

### 2. Installa le dipendenze
```bash
pip install streamlit==1.44.1 pandas==2.2.3 numpy==2.2.5 scikit-learn==1.6.1 ucimlrepo==0.0.7
```

### 3. Avvia la web app
```bash
streamlit run main.py
```

## 🎨 Visualizzazione su Tableau
Link alla mappa interattiva dei prezzi: 🔗 [Visualizzazione dataset](https://public.tableau.com/shared/FDWXPNM7B?:display_count=n&:origin=viz_share_link)
