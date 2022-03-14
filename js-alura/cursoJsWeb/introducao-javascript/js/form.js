const button = document.querySelector("#adicionar-paciente");

button.addEventListener("click", function (event) {
    event.preventDefault();
    
    const form = document.querySelector("#form-adiciona");

    


    // Extraindo informações do paciente do form
    const paciente = obtemPacienteFormulario(form);

    if (!validaPaciente(paciente)) {
        console.log("Paciente invalido");
        return;
    }

    // Cria os tr e os td
    const trMontada = montaTr(paciente);

    // Adicionando o paciente na tabela
    const tabela = document.querySelector("#tabela-pacientes");
    tabela.appendChild(trMontada);

    // limpar campos
    form.reset();
});

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


function montaTd (dado, classe) {
    const td = document.createElement("td");
    td.textContent = dado;
    td.classList.add(classe);

    return td;
}

function validaPaciente (paciente) {
    if(validaPeso(paciente.peso)) {
        return true;
    }else {
        return false;
    }
}