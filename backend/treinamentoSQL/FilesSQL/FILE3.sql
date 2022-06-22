USE SUCOS;

UPDATE tbvendedor SET COMISSAO = 0.11
WHERE NOME = 'Cláudia Morais';

UPDATE tbvendedor SET NOME = 'José Geraldo da Fonseca Junior'
WHERE NOME = 'José Geraldo da Fonseca';

SELECT * FROM tbvendedor