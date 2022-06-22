DROP TABLE tbvendedor;

ALTER TABLE tbvendedor ADD COLUMN (DATA_ADMISSAO DATE);
ALTER TABLE tbvendedor ADD COLUMN (DE_FERIAS BIT);

CREATE TABLE tbvendedor 
(
Matricula VARCHAR(30) NULL,
NOME VARCHAR(150) NULL,
COMISSAO FLOAT NULL,
DATA_ADMISSAO DATE NULL,
DE_FERIAS VARCHAR(5) NULL
);

ALTER TABLE tbvendedor ADD PRIMARY KEY (MATRICULA);

INSERT INTO tbvendedor 
(
MATRICULA, NOME, COMISSAO, DATA_ADMISSAO, DE_FERIAS
) VALUES 
(
00235, 'Márcio Almeida Silva', 0.08, '2014-08-15', 'NÃO'
);

INSERT INTO tbvendedor 
(
MATRICULA, NOME, COMISSAO, DATA_ADMISSAO, DE_FERIAS
) VALUES 
(
00236, 'Cláudia Morais', 0.08, '2013-09-17', 'SIM'
);

INSERT INTO tbvendedor 
(
MATRICULA, NOME, COMISSAO, DATA_ADMISSAO, DE_FERIAS
) VALUES 
(
00237, 'Roberta Martins', 0.11, '2017-03-18', 'SIM'
);

INSERT INTO tbvendedor 
(
MATRICULA, NOME, COMISSAO, DATA_ADMISSAO, DE_FERIAS
) VALUES 
(
00238, 'Péricles Alves', 0.11, '2016-08-21', 'NÃO'
);


SELECT * FROM tbvendedor;