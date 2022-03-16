const button = document.querySelector("#adicionar-paciente");

button.addEventListener("click", function (event) {
    event.preventDefault();
    
    const form = document.querySelector("#form-adiciona");
    const mensagem = document.querySelector("#mensagem-erro")
    


    // Extraindo informações do paciente do form
    const paciente = obtemPacienteFormulario(form);


   
    

    // Buscar os erros e criar nosso array
    let erros = validaPaciente(paciente);

    // criar a ul e li com os erros, se nosso array tiver dados
    if (erros.length > 0) {
        exibeMensagemDeErro(erros);
        return;
    }

    // Adicionando o paciente na tabela
    adicionaPacienteNaTabela(paciente);
    
    const ul = document.querySelector("#mensagens-erro")
    

    // limpar campos
    form.reset();
    ul.innerHTML = "";
});

function adicionaPacienteNaTabela (paciente) {
    // Cria os tr e os td
    const trMontada = montaTr(paciente);
    const tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(trMontada);
}

// Responsavel por cria nosso objeto com informações do paciente
function obtemPacienteFormulario (form) {

    const paciente = {
        nome: form.nome.value,
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calculaIMC(form.peso.value, form.altura.value)
    };

    return paciente;
}

// Montar nossa tr utilizando nosso objeto paciente
function montaTr(paciente) {
    const pacienteTr = document.createElement("tr");
    pacienteTr.classList.add("paciente");

    const nomeTd = montaTd(paciente.nome, "info-nome");
    const pesoTd = montaTd(paciente.peso, "info-peso");
    const alturaTd = montaTd(paciente.altura, "info-altura");
    const gorduraTd = montaTd(paciente.gordura, "info-gordura");
    const ImcTd = montaTd(paciente.imc, "info-imc");


    pacienteTr.appendChild(nomeTd);
    pacienteTr.appendChild(pesoTd);
    pacienteTr.appendChild(alturaTd);
    pacienteTr.appendChild(gorduraTd);
    pacienteTr.appendChild(ImcTd);

    return pacienteTr;
}

// Mota nossa td e colocar classe nela 
function montaTd (dado, classe) {
    const td = document.createElement("td");
    td.textContent = dado;
    td.classList.add(classe);

    return td;
}

// Validar nosso paciente pelas informações vindas do objeto
function validaPaciente (paciente) {

    const erros = [];

    if(!validaPeso(paciente.peso)) {
        erros.push("Peso é invalido");
    }

    if(!validaAltura(paciente.altura)) {
        erros.push("Altura é invalida");
    }

    if (paciente.nome.length == 0) {
        erros.push("O nome não pode ser em branco!");
    }

    if (paciente.gordura.length == 0) {
        erros.push("A Gordura não pode ser em branco!");
    }

    if (paciente.peso.length == 0) {
        erros.push(" O Peso não pode ser em branco!");
    }

    if (paciente.altura.length == 0) {
        erros.push("A Altura não pode ser em branco!");
    }

    return erros;
}

// Cria um ul e cada li são os erros que se tem
function exibeMensagemDeErro(erros) {
    const ul = document.querySelector("#mensagens-erro");
    ul.innerHTML = "";

    erros.forEach(function (erro) {
        const li = document.createElement("li");

        li.textContent = erro;
        ul.appendChild(li)
    });
}