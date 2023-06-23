from filemanager import Files
from utilities import util
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, KBinsDiscretizer


class dataframes:

    df_tr = []
    df_re = []
    df_sb_tr = []
    df_sb_re = []
    dict_sb_tr = []
    dict_sb_re = []
    dict_sb = []
    df_tr_fusion = []
    df_re_fusion = []
    df_tr_fu_filt = []
    df_re_fu_filt = []
    Y_tr = []
    Y_re = []
    filas = 0
    delta = []

    def __init__(self, df):
        self._df = df

    def grouping_and_ordering(self, df):
        conteo_agrupados = df.groupby(['n1', 'n2', 'n3', 'n4', 'n5', 'sb']).size()
        conteo_agrupados[conteo_agrupados > 1].sort_values(ascending=False).head(10)
        return conteo_agrupados

    def create_filtered_dataframes(self, df):
        propiedades = ["Tr"]
        self.df_tr = df[df.tipo.isin(propiedades)]
        propiedades = ["Re"]
        self.df_re = df[df.tipo.isin(propiedades)]
        return self.df_tr, self.df_re

    def filtering_new_raffles(self):
        self.df_sb_tr = self.df_tr[self.df_tr.sb.isin(util.sbs)]
        self.df_sb_re = self.df_re[self.df_re.sb.isin(util.sbs)]

    def counting_and_ordering(self):
        self.dict_sb_tr = dict(self.df_tr.sb.value_counts())
        self.dict_sb_re = dict(self.df_re.sb.value_counts())
        self.dict_sb = dict(self.df.sb.value_counts())

    def categorical_values(self):
        le = LabelEncoder()
        for item in util.categorical_cols[:]:
            if item == 'tipo' or item == 'ganador':
                nombre_col = str(item) + str('Tr')
                self.df_tr[nombre_col] = le.fit_transform(self.df_tr[item])
                nombre_col = str(item) + str('Re')
                self.df_re[nombre_col] = le.fit_transform(self.df_re[item])

    def removing_unuseful_cols(self):
        # print(df_tr)
        self.df_tr_fusion = self.df_tr.drop(util.unuseful_cols, axis=1)
        self.df_re_fusion = self.df_re.drop(util.unuseful_cols, axis=1)
        # print(df_tr_fusion)
        self.df_tr_fu_filt = self.df_tr_fusion.iloc[:, [0, 3, 4, 5, 6, 7, 8]]
        self.df_re_fu_filt = self.df_re_fusion.iloc[:, [0, 3, 4, 5, 6, 7, 8]]
        self.Y_tr = self.df_tr_fusion.iloc[:, 10]
        self.Y_re = self.df_re_fusion.iloc[:, 10]
        self.filas = int(self.df_sb_tr.shape[0])

    def addcolumn(df):
        for index, row in df.iterrows():
            dataframes.delta.append(util.word_maker(row.n1, row.n2, row.n3, row.n4, row.n5))
        df['delta'] = dataframes.delta
        return df

    def add_deltacolumn(self):
        self.df_tr_fu_filt = dataframes.addcolumn(self.df_tr_fu_filt)
        self.df_re_fu_filt = dataframes.addcolumn(self.df_re_fu_filt)

    def delta_count(self):
        self.df_tr_fu_filt.delta.value_counts()
        self.df_re_fu_filt.delta.value_counts()

    def cortasbs(df, sb):
        df_filt = df.iloc[0::1, [0, 6]]
        print(df_filt)
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortasingles(df, col0, col1):
        df_filt = df.iloc[0::1, [col0, col1]]
        print(df_filt)
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortasinglessb(df, col0, col1, sb):
        df_filt = df.iloc[0::1, [col0, col1, sb]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortaduplas(df, col0, col1, col2):
        df_filt = df.iloc[0::1, [col0, col1, col2]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortaduplassb(df, col0, col1, col2, sb):
        df_filt = df.iloc[0::1, [col0, col1, col2, sb]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortatrios(df, col0, col1, col2, col3):
        df_filt = df.iloc[0::1, [col0, col1, col2, col3]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortatriossb(df, col0, col1, col2, col3, sb):
        df_filt = df.iloc[0::1, [col0, col1, col2, col3, sb]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortacuartetos(df, col0, col1, col2, col3, col4):
        df_filt = df.iloc[0::1, [col0, col1, col2, col3, col4]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortacuartetossb(df, col0, col1, col2, col3, col4, sb):
        df_filt = df.iloc[0::1, [col0, col1, col2, col3, col4, sb]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortaquintetos(df, col0, col1, col2, col3, col4, col5):
        df_filt = df.iloc[0::1, [col0, col1, col2, col3, col4, col5]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    def cortaquintetossb(df, col0, col1, col2, col3, col4, col5, sb):
        df_filt = df.iloc[0::1, [col0, col1, col2, col3, col4, col5, sb]]
        df_filt = df_filt.rename(columns={'n1': 'num', 'n2': 'num', 'n3': 'num', 'n4': 'num', 'n5': 'num'})
        return df_filt

    #
    def concatenador_sbs(df, sb):
        colid = 0
        df_1d_sb_tr = dataframes.cortasbs(df, sb)  # if sb > 0 else cortasingles(df,colid,1)
        df_1d_sb_tr.columns = ['idSorteo', 'sb']  # if sb > 0 else ['idSorteo', 'num1']
        #print("final: ", df_1d_sb_tr)
        return df_1d_sb_tr

    def concatenador_singles(df, sb):
        colid = 0
        df_1d_fu_tr = dataframes.cortasinglessb(df, colid, 1, sb) if sb > 0 else dataframes.cortasingles(df, colid, 1)
        print(df_1d_fu_tr)
        inicial = 0
        for i in range(1, 6):
            df_temp_fusion = dataframes.cortasinglessb(df, colid, i, sb) if sb > 0 else dataframes.cortasingles(df, colid, i)
            if (inicial == 0):
                df_1d_fu_tr = df_temp_fusion
                inicial += 1
            else:
                df_1d_fu_tr = dataframes.pd.concat([df_1d_fu_tr, df_temp_fusion], ignore_index=True)
        df_1d_fu_tr.columns = ['idSorteo', 'num1', 'sb'] if sb > 0 else ['idSorteo', 'num1']
        return df_1d_fu_tr

    def concatenador_duplas(df, sb):
        colid = 0
        inicial = 0
        for i in range(1, 6):
            for ii in range(i + 1, 6):
                df_temp_fusion = dataframes.cortaduplassb(df, colid, i, ii, sb) if sb > 0 else dataframes.cortaduplas(df, colid, i, ii)
                if (inicial == 0):
                    df_2d_fu_tr = df_temp_fusion
                    inicial += 1
                else:
                    df_2d_fu_tr = dataframes.pd.concat([df_2d_fu_tr, df_temp_fusion], ignore_index=True)
        df_2d_fu_tr.columns = ['idSorteo', 'num1', 'num2', 'sb'] if sb > 0 else ['idSorteo', 'num1', 'num2']
        return df_2d_fu_tr

    def concatenador_trios(df, sb):
        colid = 0
        df_3d_fu_tr = dataframes.cortatriossb(df, colid, 1, 2, 3, sb) if sb > 0 else dataframes.cortatrios(df, colid, 1, 2, 3)
        inicial = 0
        for i in range(1, 6):
            for ii in range(i + 1, 6):
                for iii in range(ii + 1, 6):
                    df_temp_fusion = dataframes.cortatriossb(df, colid, i, ii, iii, sb) if sb > 0 else dataframes.cortatrios(df, colid, i, ii,
                                                                                                       iii)
                    if (inicial == 0):
                        df_3d_fu_tr = df_temp_fusion
                        inicial += 1
                    else:
                        df_3d_fu_tr = dataframes.pd.concat([df_3d_fu_tr, df_temp_fusion], ignore_index=True)
        df_3d_fu_tr.columns = ['idSorteo', 'num1', 'num2', 'num3', 'sb'] if sb > 0 else ['idSorteo', 'num1', 'num2',
                                                                                         'num3']
        return df_3d_fu_tr

    def concatenador_cuartetos(df, sb):
        colid = 0
        inicial = 0
        for i in range(1, 6):
            for ii in range(i + 1, 6):
                for iii in range(ii + 1, 6):
                    for iiii in range(iii + 1, 6):
                        df_temp_fusion = dataframes.cortacuartetossb(df, colid, i, ii, iii, iiii,
                                                          sb) if sb > 0 else dataframes.cortacuartetos(df, colid, i, ii, iii, iiii)
                        if (inicial == 0):
                            df_4d_fu_tr = df_temp_fusion
                            inicial += 1
                        else:
                            df_4d_fu_tr = dataframes.pd.concat([df_4d_fu_tr, df_temp_fusion], ignore_index=True)
        df_4d_fu_tr.columns = ['idSorteo', 'num1', 'num2', 'num3', 'num4', 'sb'] if sb > 0 else ['idSorteo', 'num1',
                                                                                                 'num2', 'num3', 'num4']
        return df_4d_fu_tr

    def concatenador_quintetos(df, sb):
        colid = 0
        df_5d_fu_tr = dataframes.cortaquintetossb(df, colid, 1, 2, 3, 4, 5, sb) if sb > 0 else dataframes.cortaquintetos(df, colid, 1, 2, 3,
                                                                                                   4, 5)
        df_5d_fu_tr.columns = ['idSorteo', 'num1', 'num2', 'num3', 'num4', 'num5', 'sb'] if sb > 0 else ['idSorteo',
                                                                                                         'num1', 'num2',
                                                                                                         'num3', 'num4',
                                                                                                         'num5']
        return df_5d_fu_tr

    def agrupa_sbs(df):
        conteo_nums = df.groupby(['sb']).size()
        tupla = []
        df = util.addcolumntuplas(conteo_nums, 1)
        df.columns = ['conteo', 'tupla']
        return df

    def agrupa_singles(df):
        conteo_nums = df.groupby(['num1']).size()
        tupla = []
        df =  util.addcolumntuplas(conteo_nums, 1)
        df.columns = ['conteo', 'tupla']
        return df

    def agrupa_duplas(df):
        conteo_nums = df.groupby(['num1', 'num2']).size()
        tupla = []
        df =  util.addcolumntuplas(conteo_nums, 2)
        df.columns = ['conteo', 'tupla']
        return df

    def agrupa_trios(df):
        conteo_nums = df.groupby(['num1', 'num2', 'num3']).size()
        tupla = []
        df =  util.addcolumntuplas(conteo_nums, 3)
        df.columns = ['conteo', 'tupla']
        return df

    def agrupa_cuartetos(df):
        conteo_nums = df.groupby(['num1', 'num2', 'num3', 'num4']).size()
        tupla = []
        df =  util.addcolumntuplas(conteo_nums, 4)
        df.columns = ['conteo', 'tupla']
        return df

    def agrupa_quintetos(df):
        conteo_nums = df.groupby(['num1', 'num2', 'num3', 'num4', 'num5']).size()
        tupla = []
        df =  util.addcolumntuplas(conteo_nums, 5)
        df.columns = ['conteo', 'tupla']
        return df

    def counting_sbs(self):
        df_1d_sb_tr = dataframes.concatenador_sbs(self.df_tr_fu_filt, 0)
        conteos_1d_sb_tr = dataframes.agrupa_sbs(df_1d_sb_tr)
        conteos_1d_sb_tr = Files.conteo_files_saver( self, 'conteos_1d_sb_tr.csv', conteos_1d_sb_tr)
        df_1d_sb_re = dataframes.concatenador_sbs(self.df_re_fu_filt, 0)
        conteos_1d_sb_re = dataframes.agrupa_sbs(df_1d_sb_re)
        conteos_1d_sb_re = Files.conteo_files_saver(self, 'conteos_1d_sb_re.csv', conteos_1d_sb_re)
        return conteos_1d_sb_tr, conteos_1d_sb_re

    def counting_singles(self):
        df_1d_fusion_tr = dataframes.concatenador_singles(self.df_tr_fu_filt, 0)
        conteos_1d_tr = dataframes.agrupa_singles(df_1d_fusion_tr)
        conteos_1d_tr = Files.conteo_files_saver(self, 'conteos_1d_tr.csv', conteos_1d_tr)
        df_1d_fusion_re = dataframes.concatenador_singles(self.df_re_fu_filt, 0)
        conteos_1d_re = dataframes.agrupa_singles(df_1d_fusion_re)
        conteos_1d_re = Files.conteo_files_saver(self, 'conteos_1d_re.csv', conteos_1d_re)
        return conteos_1d_tr, conteos_1d_re

    def counting_duplas(self):
        df_2d_fusion_tr = dataframes.concatenador_duplas(self.df_tr_fu_filt, 0)
        conteos_2d_tr = dataframes.agrupa_duplas(df_2d_fusion_tr)
        conteos_2d_tr = Files.conteo_files_saver(self, 'conteos_2d_tr.csv', conteos_2d_tr)
        df_2d_fusion_re = dataframes.concatenador_duplas(self.df_re_fu_filt, 0)
        conteos_2d_re = dataframes.agrupa_duplas(df_2d_fusion_re)
        conteos_2d_re = Files.conteo_files_saver(self, 'conteos_2d_re.csv', conteos_2d_re)
        return conteos_2d_tr, conteos_2d_re

    def counting_trios(self):
        df_3d_fusion_tr = dataframes.concatenador_trios(self.df_tr_fu_filt, 0)
        conteos_3d_tr = dataframes.agrupa_trios(df_3d_fusion_tr)
        conteos_3d_tr = Files.conteo_files_saver(self, 'conteos_3d_tr.csv', conteos_3d_tr)
        df_3d_fusion_re = dataframes.concatenador_trios(self.df_re_fu_filt, 0)
        conteos_3d_re = dataframes.agrupa_trios(df_3d_fusion_re)
        conteos_3d_re = Files.conteo_files_saver(self, 'conteos_3d_re.csv', conteos_3d_re)
        return  conteos_3d_tr, conteos_3d_re

    def counting_cuartetos(self):
        df_4d_fusion_tr = dataframes.concatenador_cuartetos(self.df_tr_fu_filt, 0)
        conteos_4d_tr = dataframes.agrupa_cuartetos(df_4d_fusion_tr)
        conteos_4d_tr = Files.conteo_files_saver(self, 'conteos_4d_tr.csv', conteos_4d_tr)
        df_4d_fusion_re = dataframes.concatenador_cuartetos(self.df_re_fu_filt, 0)
        conteos_4d_re = dataframes.agrupa_cuartetos(df_4d_fusion_re)
        conteos_4d_re = Files.conteo_files_saver(self, 'conteos_4d_re.csv', conteos_4d_re)
        return conteos_4d_tr, conteos_4d_re

    def counting_quintetos(self):
        df_5d_fusion_tr = dataframes.concatenador_quintetos(self.df_tr_fu_filt, 0)
        conteos_5d_tr = dataframes.agrupa_quintetos(df_5d_fusion_tr)
        conteos_5d_tr = Files.conteo_files_saver(self, 'conteos_5d_tr.csv', conteos_5d_tr)
        df_5d_fusion_re = dataframes.concatenador_quintetos(self.df_re_fu_filt, 0)
        conteos_5d_re = dataframes.agrupa_quintetos(df_5d_fusion_re)
        conteos_5d_re = Files.conteo_files_saver(self, 'conteos_5d_re.csv', conteos_5d_re)
        return conteos_5d_tr, conteos_5d_re
