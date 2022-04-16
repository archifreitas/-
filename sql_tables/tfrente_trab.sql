CREATE TABLE tfrente_trab (
	id INT PRIMARY KEY,
	cod_obra VARCHAR(10),
	estado INT,
	trabalho_noturno BINARY,
	_data DATE,
	utilizador VARCHAR(50),
	data_int DATE,
	aprovador VARCHAR(50),
	revisto_por VARCHAR(50))