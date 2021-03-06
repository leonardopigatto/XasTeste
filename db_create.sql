CREATE DATABASE xastreedb
default character set utf8
default collate utf8_general_ci;

use xastreedb;

-- A tabela de investimentos vem primeiro pois será adicionado a opção "Nenhum" para quando um cliente for criado
CREATE TABLE investimentos (
    id int unsigned not null auto_increment, 
    investimento varchar(30) not null, 
    primary key (id)
) charset=utf8 auto_increment=1;

INSERT INTO investimentos (investimento) VALUES ("Nenhum");

CREATE TABLE clientes (
    id int unsigned not null auto_increment, 
    nome varchar(30) not null, 
    sobrenome varchar(30) not null,
    email varchar(30) not null,
    id_investimento int unsigned not null,
    primary key (id)
) charset=utf8 auto_increment=1;

ALTER TABLE clientes 
    ADD CONSTRAINT fk_id_investimento FOREIGN KEY (id_investimento) REFERENCES investimentos (id);

-- Exemplos de investimentos (*Opcional*)
INSERT INTO investimentos (investimento) VALUES ("Renda Fixa");
INSERT INTO investimentos (investimento) VALUES ("Renda Variavel");
INSERT INTO investimentos (investimento) VALUES ("Fundos Imobiliarios");
INSERT INTO investimentos (investimento) VALUES ("Criptomoedas");

commit;