CREATE TABLE temp_frente (
	id INT PRIMARY KEY,
	nome VARCHAR(100),
	horas INT,
	justificao_falta VARCHAR(1),
	deslocacao VARCHAR(2),
	obs VARCHAR(100),
	id_frente INT,
	registado_por VARCHAR(100),
	_Data Date)