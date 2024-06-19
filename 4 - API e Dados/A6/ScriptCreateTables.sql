Use db_py_motim;

DROP TABLE IF EXISTS TB_Categoria;
DROP TABLE IF EXISTS TB_Item;
DROP TABLE IF EXISTS TB_Ordem;
DROP TABLE IF EXISTS TB_CLIENTE;
DROP TABLE IF EXISTS tb_produto;

GO

Create Table TB_PRODUTO(
	ID INT PRIMARY KEY,
	Nome NVARCHAR(255),
	Preco Money,
	ID_Categoria INT
)

Create Table TB_CLIENTE(
	ID			INT PRIMARY KEY,
	Dt_Criacao datetime,
	nome nvarchar(255),
	sobrenome  nvarchar(255),
	email nvarchar(100),
	telefone nvarchar(30),
	pais nvarchar(30),
	uf varchar(30),
	rua nvarchar(255),
	numero  nvarchar(10),
	complemento  nvarchar(255)
)

Create Table TB_CATEGORIA (
	ID INT PRIMARY KEY,
	Categoria NVARCHAR(255)
)

Create table TB_ITEM(
	ID			INT PRIMARY KEY,
	Id_Ordem   int,
	id_produto  int,
	Quantidade  int,
	preco_total money
)

Create Table TB_ORDEM(
	ID			 INT PRIMARY KEY,
	dt_Criacao   datetime,
	id_cliente   int,
	ds_status    nvarchar(255)
)








