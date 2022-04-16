CREATE TABLE tequip_frente (
	id INT PRIMARY KEY,
	id_equip INT,
	descricao VARCHAR(100),
	hrs_trab INT,
	hrs_par INT,
	hrs_avar INT,
	avaria BINARY,
	obs VARCHAR(100),
	id_frente INT,
	obra VARCHAR(10),
	registado_por VARCHAR(50))