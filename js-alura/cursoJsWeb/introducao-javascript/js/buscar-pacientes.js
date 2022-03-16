const botaoAdicionar = document.querySelector("#buscar-pacientes");

botaoAdicionar.addEventListener("click", function () {
    console.log("buscando pacientes")

    // Responsavel por fazer a requisição, eu tenho de configurar o sistema para que ele possa reconhecer o que eu quero
    const xhr = new XMLHttpRequest();

    // Para criar a função que mostra o que e aonde do nosso elemento
    xhr.open("GET", "https://api-pacientes.herokuapp.com/pacientes");

    // Função para a partir do load cuspir nossa resposta no console
    xhr.addEventListener("load", function () {
        const erroAjax = document.querySelector("#erro-ajax");
        // Testando se nossa requisição deu certo, se ela deu certo vai ser igual a 200
        if (xhr.status == 200) {

            // Colocando a classe para que se der certo a nossa request ele possa sumir a mensagem de erro
            erroAjax.classList.add("invisivel");
            // Texto da resposta
            const resposta = xhr.responseText;
            // Parciador de json para objeto em js, JSOn parse vai ler todo o texto e me devolver um objeto no js 
            const paciente_Json = JSON.parse(resposta);

            // Adicionando na tabela nosso objeto que veio do JSON
            paciente_Json.forEach(paciente => {
                adicionaPacienteNaTabela(paciente);
            });
        } else {
            console.log( xhr.status );
            console.log( xhr.responseText );
            // Tirando a classe invisivel para que se der erro possa aparecer a mensagem
            erroAjax.classList.remove("invisivel");
        }


    });

    // Pega nossa requisição que acabamos de enviar e envia ela
    xhr.send();
});