// LOGIN
const loginForm = document.getElementById('loginForm');
if (loginForm) {
    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        const res = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({username, password})
        });
        const data = await res.json();
        document.getElementById('message').innerText = data.success ? `Benvenuto ${data.nome}` : "Login fallito";
    });
}

// RICETTE
const listaRicette = document.getElementById('listaRicette');
const filtroBtn = document.getElementById('filtraBtn');
if (filtroBtn) {
    filtroBtn.addEventListener('click', async () => {
        const genere = document.getElementById('filtroGenere').value;
        const url = genere ? `http://127.0.0.1:5000/ricette/genere/${genere}` : 'http://127.0.0.1:5000/ricette';
        const res = await fetch(url);
        const ricette = await res.json();
        listaRicette.innerHTML = "";
        ricette.forEach(r => {
            const li = document.createElement('li');
            li.innerHTML = `${r.Titolo} - <button onclick="aggiungiCarrello(${r.ID_Ricetta})">Aggiungi al carrello</button>`;
            listaRicette.appendChild(li);
        });
    });
}

// CARRELLO
async function aggiungiCarrello(id) {
    await fetch('http://127.0.0.1:5000/carrello/add', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ricetta_id: id, persone: 1})
    });
    alert("Aggiunto al carrello!");
}

// VISUALIZZA CARRELLO
const carrelloList = document.getElementById('carrelloList');
const checkoutBtn = document.getElementById('checkoutBtn');
if (carrelloList) {
    async function caricaCarrello() {
        const res = await fetch('http://127.0.0.1:5000/carrello');
        const carrello = await res.json();
        carrelloList.innerHTML = "";
        carrello.forEach(item => {
            const li = document.createElement('li');
            li.innerText = `Ricetta ID: ${item.ricetta_id} - Persone: ${item.persone}`;
            carrelloList.appendChild(li);
        });
    }
    caricaCarrello();
}

// CHECKOUT
if (checkoutBtn) {
    checkoutBtn.addEventListener('click', async () => {
        const res = await fetch('http://127.0.0.1:5000/checkout', {method: 'POST'});
        const data = await res.json();
        document.getElementById('checkoutMessage').innerText = data.success ? `Ordine ID: ${data.ordine_id}` : "Errore checkout";
        if (data.success) window.location.href = "checkout.html";
    });
}
