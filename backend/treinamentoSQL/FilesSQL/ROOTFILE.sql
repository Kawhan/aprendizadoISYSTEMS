# Criando nossa databse
CREATE DATABASE SUCOS;

# Double click
USE SUCOS;

# Criando tabela
CREATE TABLE tdcliente
( CPF VARCHAR(11),
NOME VARCHAR(100),
ENDERECO1 VARCHAR(150),
ENDERECO2 VARCHAR(150),
BAIRRO VARCHAR(50),
CIDADE VARCHAR(50),
ESTADO VARCHAR(50),
CEP VARCHAR(8),
IDADE SMALLINT,
SEXO VARCHAR(1),
LIMITE_CREDITO FLOAT,
VOLUME_COMPRA FLOAT,
PRIMEIRA_COMPRA BIT(1)
);

CREATE TABLE tbproduto
( 
PRODUTO VARCHAR(20) NULL,
NOME  VARCHAR(150) NULL,
EMBALAGEM VARCHAR(50) NULL,
TAMANHO VARCHAR(50) NULL,
SABOR VARCHAR(50) NULL,
PRECO_LISTA FLOAT NULL
);tdclientetdcliente

# Apagando tabela
DROP TABLE tdproduto;

# Inserindo informações na tabela
INSERT INTO tbproduto (
PRODUTO,  NOME, EMBALAGEM, TAMANHO, SABOR,
PRECO_LISTA) VALUES (
'1040107', 'Light - 350 ml - Melância',
'Lata', '350 ml', 'Melância', 4.56);

# Selecionando valores
SELECT * FROM tbproduto;

CREATE TABLE tbvendedor
( MATRICULA VARCHAR(20),
NOME VARCHAR(100),
COMISSAO FLOAT
);

DROP TABLE tbvendedor;

INSERT INTO tbvendedor (
MATRICULA, NOME, COMISSAO) VALUES 
(
'00233', 'JOÃO GERALDO DA FONSECA', 0.10
);


INSERT INTO tbvendedor (
MATRICULA, NOME, COMISSAO) VALUES 
(
'00235', 'Márcio Almeida Silva', 0.08
);

INSERT INTO tbvendedor (
MATRICULA, NOME, COMISSAO) VALUES 
(
'00236', 'Cláudia Morais', 0.08
);

SELECT * FROM tbvendedor;

INSERT INTO tbproduto (
PRODUTO,  NOME, EMBALAGEM, TAMANHO, SABOR,
PRECO_LISTA) VALUES (
'1037797', 'Clean - 2Litros - Laranja',
'Pet', '2 L', 'Laranja', 16.01);

INSERT INTO tbproduto (
PRODUTO,  NOME, EMBALAGEM, TAMANHO, SABOR,
PRECO_LISTA) VALUES (
'1000889', 'Sabor da Montanha - 700 ml',
'Garafa', '700 ml', 'Uva', 6.31);


INSERT INTO tbproduto (
PRODUTO,  NOME, EMBALAGEM, TAMANHO, SABOR,
PRECO_LISTA) VALUES (
'1004327', 'Videira do Campo - 1,5 Litros - Melância',
'Pet', '1,5 L', 'Melância', 19.51);


﻿USE sucos;

INSERT INTO tbproduto (
PRODUTO,  NOME, EMBALAGEM, TAMANHO, SABOR,
PRECO_LISTA) VALUES
('544931', 'Frescor do Verão - 350 ml - Limão', 'PET', '350 ml','Limão',3.20);

INSERT INTO tbproduto (
PRODUTO,  NOME, EMBALAGEM, TAMANHO, SABOR,
PRECO_LISTA) VALUES
('1078680', 'Frescor do Verão - 470 ml - Manga', 'Lata', '470 ml','Manga',5.18);

