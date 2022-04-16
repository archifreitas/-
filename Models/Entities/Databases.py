


class Databases:
    '''Class for Databases constants'''

    database_dict = {
        'Evento': ['RegistoDiarioId', 
                   'TipoEventoId', 
                   'ObraCodigo', 
                   'ProdutoServicoTarefa', 
                   'Quantidade', 
                   'UnidadeId', 
                   'Observacoes'],
        'RegistoDiario': ['Id',
                          'Data', 
                          'MotoristaId', 
                          'KmsInicio', 
                          'KmsFim', 
                          'TipoDeslocacaoId'],
        'tcap_frente': ['id_cap', 
                        'quantidade', 
                        'unidade', 
                        'obs'],
        'temp_frente': ['id_emp', 
                        'horas', 
                        'deslocação', 
                        'justificacao_falta', 
                        'obs'],
        'tequip_frente': ['id_equip', 
                          'hrs_trab', 
                          'hrs_par', 
                          'hrs_avar', 
                          'avaria', 
                          'obs'],
        'tfrente_trab': ['cod_obra', 
                         'trabalho_noturno', 
                         'observações', 
                         'data']
    }

    database_keys = {
        'Evento': {'RegistoDiario': ['RegistoDiarioId', 'Id']},
        'temp_frente': {'tcap_frente': ['id_frente', 'id'],
                        'tequip_frente': ['id_frente', 'id'],
                        'tfrente_trab': ['id_frente', 'id']}
    }

    def __init__(self):
        self.data_dict = self.database_dict
        self.data_keys = self.database_keys

    def get_merge_keys(self,table):
        return self.data_keys[table]