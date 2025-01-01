let userName = "";
let inactivityTimer;

// Exibe a observação de atualização
// document.getElementById("update-info").style.display = "block";

window.onload = function () {
    const storedUserName = localStorage.getItem("userName");
    const isLoggedIn = localStorage.getItem("isLoggedIn");
    const showUserButton = document.getElementById("show-user-btn");

    // Salvar o nome do usuário logado globalmente
    if (storedUserName && isLoggedIn === "true") {
        window.userName = storedUserName; // Nome do usuário logado
    } else {
        window.userName = null;
    }

    if (isLoggedIn === "true") {
        document.getElementById("login-container").style.display = "none";
        document.getElementById("name-container").style.display = "block";
        document.getElementById("user-display").textContent = storedUserName;
        document.getElementById("chat-box").style.display = "block";
        document.getElementById("input-container").style.display = "flex";

        

        if (showUserButton) {
            if (storedUserName === "admin") {
                showUserButton.style.display = "block";
            } else {
                showUserButton.style.display = "none";
            }
        } else {
            console.error("Botão 'show-user-btn' não encontrado no DOM.");
        }
    } else {
        document.getElementById("login-container").style.display = "block";
        document.getElementById("name-container").style.display = "none";
        document.getElementById("chat-box").style.display = "none";
        document.getElementById("input-container").style.display = "none";

        if (showUserButton) {
            showUserButton.style.display = "none";
        }
    }
};

// Mensagens de boas-vindas
const mensagens = [
    'E aí, beleza, em que posso te ajudar?',
    'Fala, como posso ajudar?',
    'Seja bem-vindo! Puxa uma cadeira, pega um café e vamos começar!',
    'Olá! Entre e fique à vontade. Aqui a gente resolve tudo com um sorriso no rosto (ou tenta, pelo menos)!',
    'Seja bem-vindo! Aqui ninguém larga a mão de ninguém, só do teclado (às vezes).',
    'Bem-vindo! Pega o Wi-Fi, não esquece o cafezinho, e bora fingir que sabemos o que estamos fazendo!',
    'Seja bem-vindo! Prometo que aqui ninguém morde... só os bugs às vezes.',
    'Chegou quem tava faltando! A má notícia é que agora não tem mais desculpa pra não entregar tudo no prazo.',
    'Chega mais! O Wi-Fi tá liberado, o cafezinho tá quente, e a bagunça tá organizada... mais ou menos.',
    'Bem-vindo(a)! Aqui o café é forte, as piadas são ruins, e a criatividade é ilimitada... quase sempre.',
    'Hey! Como vai? Vamos espalhar um pouco de magia por aí? Zueira, em que posso ajudar?',
    'Seja bem-vindo(a)! Conexão tem, café tem, agora só falta fingir que o caos é planejado.',
    'Bem-vindo(a)! Aqui o lema é simples: café no sangue, bom humor em falta... às vezes.',
    'E ai, bora botar pra quebrar, deixa comigo, vou fazer parecer que sou um gênio!',
    'Olá! Pode ficar tranquilo,a gente vai fazendo e finge que é tudo no automático.',
    'Parceiro(a)! Vamos botar pra quebrar? O que vai ser hoje?',
    'Fala mostro, aqui é só apertar uns botões e fingir que tudo está sob controle.',
    'Chegou! Relaxa, a gente sabe o que está fazendo... mais ou menos!',
    'E aí, chuchu! Pronto para bater um papo?',
    'E ai! Tô aqui para desenrolar qualquer situação!',
    'Hey, beleza? Estou pronto para te dar uma força, la ele! ',
    'Olá, seu pipoca! Qual vai ser?',
    'Fala, pão na chapa! Como posso facilitar o seu dia?',
    'Olá, ovo frito! Estou à disposição para te auxiliar!'
];

// Função para exibir mensagem de boas-vindas
function exibirMensagemBoasVindas() {
    const mensagemAleatoria = mensagens[Math.floor(Math.random() * mensagens.length)];
    addMessageToChatBox("Bot", mensagemAleatoria);
}

// No login com sucesso, exibe a mensagem de boas-vindas
function handleLogin() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (username === "" || password === "") {
        alert("Por favor, preencha usuário e senha.");
        return;
    }

    fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password, message: "" }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.response === "Login ou senha inválidos.") {
                document.getElementById("login-feedback").style.display = "block";
                document.getElementById("login-feedback").textContent = data.response;
            } else {
                localStorage.setItem("userName", username);
                localStorage.setItem("isLoggedIn", "true");

                document.getElementById("login-container").style.display = "none";
                document.getElementById("name-container").style.display = "block";
                document.getElementById("user-display").textContent = username;
                document.getElementById("chat-box").style.display = "block";
                document.getElementById("input-container").style.display = "flex";
                userName = username;
                startInactivityTimer();

                // Exibe mensagem de boas-vindas
                exibirMensagemBoasVindas();

                // Se for o "admin", exibe o botão "Exibir Usuário"
                if (username === "admin") {
                    document.getElementById("show-user-btn").style.display = "block";
                }
            }
        })
        .catch((error) => {
            console.error("Erro ao realizar login:", error);
            alert("Erro ao realizar login. Tente novamente.");
        });
}

// Adiciona o evento de teclado para realizar login ao pressionar Enter
document.addEventListener("keydown", function (event) {
    if (event.key === "Enter" && document.getElementById("login-container").style.display === "block") {
        event.preventDefault(); // Evita comportamentos padrão, como enviar formulário diretamente
        handleLogin(); // Chama a função de login
    }
});



// Reseta o timer sempre que houver interação do usuário
function resetTimer() {
    startInactivityTimer();
}

// Adiciona os eventos para monitorar atividade do usuário
window.addEventListener("mousemove", resetTimer);
window.addEventListener("keydown", resetTimer);
window.addEventListener("scroll", resetTimer);

// Inicia o timer de inatividade ao carregar a página
startInactivityTimer();

// Envia mensagem
function sendMessage() {
    const message = document.getElementById("message").value.trim();
    if (message === "") return;

    addMessageToChatBox(userName, message);
    document.getElementById("message").value = "";

    fetch("/get_response", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message, userName }),
    })
        .then((response) => response.json())
        .then((data) => {
            const botResponse = linkify(data.response);
            addMessageToChatBox("Bot", botResponse);
        })
        .catch((error) => {
            console.error("Erro:", error);
            addMessageToChatBox("Bot", "Desculpe, houve um erro ao processar sua mensagem.");
        });
}

// Adiciona mensagens ao chat
function addMessageToChatBox(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageElement = document.createElement("div");
    messageElement.classList.add("message");

    const displayName = sender || window.userName || "";

    if (sender === userName) {
        messageElement.classList.add("user-message");
    } else {
        messageElement.classList.add("bot-message");
    }

    messageElement.innerHTML = `<strong>${displayName}:</strong> ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Transforma URLs em links clicáveis
function linkify(text) {
    const urlPattern = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/gi;
    return text.replace(urlPattern, (url) => `<a href="${url}" target="_blank" rel="noopener noreferrer">${url}</a>`);
}

// Inicia o timer de inatividade
function startInactivityTimer() {
    clearTimeout(inactivityTimer); // Limpa qualquer timer anterior
    inactivityTimer = setTimeout(() => {
        if (localStorage.getItem("isLoggedIn") === "true") {
            alert("Você foi desconectado devido à inatividade."); // Exibe o alerta apenas se estiver logado
            logout(true); // Faz o logout indicando que foi por inatividade
        }
    }, 600000); // 600000ms = 10 minutos
}

// Reseta o timer sempre que houver interação do usuário
function resetTimer() {
    startInactivityTimer();
}

// Adiciona os eventos para monitorar atividade do usuário
window.addEventListener("mousemove", resetTimer); // Movimentação do mouse
window.addEventListener("keydown", resetTimer); // Pressionamento de teclas
window.addEventListener("scroll", resetTimer); // Rolar página

// Função de logout
function logout(isInactive = false) {
    localStorage.removeItem("userName"); // Remove dados de login do localStorage
    localStorage.removeItem("isLoggedIn");

    document.getElementById("login-container").style.display = "block"; // Exibe o container de login
    document.getElementById("name-container").style.display = "none"; // Esconde o nome do usuário
    document.getElementById("chat-box").style.display = "none"; // Esconde o chat
    document.getElementById("input-container").style.display = "none"; // Esconde o input de mensagens
    clearTimeout(inactivityTimer); // Cancela o timer de inatividade

    // Se foi desconectado por inatividade, mostra no console (para desenvolvedores)
    if (isInactive) {
        console.log("Usuário desconectado devido à inatividade.");
    }

    // Remove a classe 'show' do menu de configurações, escondendo-o
    const settingsMenu = document.getElementById("settings-menu");
    settingsMenu.classList.remove("show");
}

// Garante que o timer inicie ao carregar a página
startInactivityTimer();


// Adiciona o evento de teclado para enviar mensagem ao pressionar Enter
document.getElementById("message").addEventListener("keydown", function (event) {
    if (event.key === "Enter") {
        event.preventDefault(); // Previne quebra de linha no campo de entrada
        sendMessage(); // Chama a função para enviar a mensagem
    }
});

// Limpa o chat
function clearChat() {
    document.getElementById("chat-box").innerHTML = "";
}

// Alterna visibilidade do menu de configurações
function toggleOptionsBar() {
    const settingsMenu = document.getElementById("settings-menu");
    const userMenu = document.getElementById("user-menu");

    // Fecha a lista de usuários se estiver aberta
    if (userMenu.style.display === "block") {
        userMenu.style.display = "none";
    }

    // Alterna o menu de configurações
    settingsMenu.classList.toggle("show");
}

// Alterna visibilidade da lista de usuários
function toggleUserList() {
    const userMenu = document.getElementById("user-menu");
    const settingsMenu = document.getElementById("settings-menu");

    // Fecha o menu de configurações se estiver aberto
    if (settingsMenu.classList.contains("show")) {
        settingsMenu.classList.remove("show");
    }

    // Alterna a lista de usuários
    if (userMenu.style.display === "none" || userMenu.style.display === "") {
        renderUserList();
        userMenu.style.display = "block";
    } else {
        userMenu.style.display = "none";
    }
}

// Simula a verificação de login dos usuários, obtendo do localStorage
function isUserOnline(userName) {
    const storedUserName = localStorage.getItem("userName"); // Obtém o nome de usuário do localStorage
    return storedUserName === userName; // Se o usuário logado for o mesmo que o nome, então está online
}

function renderUserList() {
    const userMenu = document.getElementById("user-menu");
    const userList = userMenu.querySelector("ul");

    // Lista de usuários no sistema
    const users = [
        { name: "admin", online: isUserOnline("admin") }, // Verifica se "admin" está logado (online)
        { name: "user", online: isUserOnline("user") }, // Verifica se "user" está logado (online)
    ];

    // Limpa a lista de usuários atual
    userList.innerHTML = "<li><strong>Usuários</strong></li>";

    // Adiciona os usuários à lista
    users.forEach((user) => {
        const li = document.createElement("li");
        li.className = "user-item" + (user.online ? " online" : " offline");
        li.innerHTML = `<button>${user.name} ${user.online ? "(Online)" : "(Offline)"}</button>`;
        userList.appendChild(li);
    });
}










