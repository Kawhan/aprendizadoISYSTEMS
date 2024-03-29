CREATE DATABASE LOJA;

CREATE TABLE PRODUTOS
(
ID_PRODUTO INT (4) NOT NULL auto_increment,
NOME VARCHAR(255) NOT NULL,
ID_CATEGORIA INT(4) NOT NULL,
primary key(ID_PRODUTO),
Foreign key (ID_CATEGORIA) references CATEGORIA(ID_CATEGORIA)
);

CREATE TABLE CATEGORIA
(
ID_CATEGORIA INT (4) NOT NULL auto_increment,
NOME VARCHAR(255) NOT NULL,
primary key(ID_CATEGORIA)
);
