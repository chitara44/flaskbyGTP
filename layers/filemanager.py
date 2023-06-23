from datetime import datetime as dt
from dfs_data_class import dfs_data_class as dfs
from dfs_count_class import dfs_count_class as dfc
import pandas as pd
import os


class Files:


    def path_generator(tipo, name):
        prepath = str(os.getcwd())
        if (tipo == "I"):
            path = prepath + '\\origin\\' + name
        else :
            path = prepath + '\\generated\\' + name
        return path

    def initial_load(self):
        pd.set_option('display.float_format', lambda x: '%.3f' % x)
        dtm = lambda x: dt.strptime(str(x), "%d/%m/%y")
        df = pd.read_csv(Files.path_generator('I', 'expdata2.csv'))
        df.fecha.apply(dtm)
        return df

    def  files_loader(self):
        dfs.df_cq_tr = pd.read_csv(Files.path_generator('O', 'df_cq_tr.csv'))
        dfs.df_cq_re = pd.read_csv(Files.path_generator('O', 'df_cq_re.csv'))

        dfs.df_cc_tr = pd.read_csv(Files.path_generator('O', 'df_cc_tr.csv'))
        dfs.df_cc_re = pd.read_csv(Files.path_generator('O', 'df_cc_re.csv'))

        dfs.df_ct_tr = pd.read_csv(Files.path_generator('O', 'df_ct_tr.csv'))
        dfs.df_ct_re = pd.read_csv(Files.path_generator('O', 'df_ct_re.csv'))

        dfs.df_cd_tr = pd.read_csv(Files.path_generator('O', 'df_cd_tr.csv'))
        dfs.df_cd_re = pd.read_csv(Files.path_generator('O', 'df_cd_re.csv'))

        dfs.df_cs_tr = pd.read_csv(Files.path_generator('O', 'df_cs_tr.csv'))
        dfs.df_cs_re = pd.read_csv(Files.path_generator('O', 'df_cs_re.csv'))

        dfs.df_cs_tr_sb = pd.read_csv(Files.path_generator('O', 'df_cs_tr_sb.csv'))
        dfs.df_cs_re_sb = pd.read_csv(Files.path_generator('O', 'df_cs_re_sb.csv'))

        dfs.df_sel_sb_tr = pd.read_csv(Files.path_generator('O', 'df_sel_sb_tr.csv'))
        dfs.df_sel_sb_re = pd.read_csv(Files.path_generator('O', 'df_sel_sb_re.csv'))

        dfs.df_sel_si_tr = pd.read_csv(Files.path_generator('O', 'df_sel_si_tr.csv'))
        dfs.df_sel_si_re = pd.read_csv(Files.path_generator('O', 'df_sel_si_re.csv'))

        dfs.sbs = pd.read_csv(Files.path_generator('O', 'sbs.csv'))
        dfs.singles = pd.read_csv(Files.path_generator('O', 'singles.csv'))

        dfs.df_tr_fu_filt = pd.read_csv(Files.path_generator('O', 'df_tr_fu_filt_delta.csv'))
        dfs.df_re_fu_filt = pd.read_csv(Files.path_generator('O', 'df_re_fu_filt_delta.csv'))

        return dfs

    def savers(self, df_tr_fu_filt, df_re_fu_filt):
        df_tr_fu_filt.to_csv(Files.path_generator('O', 'df_tr_fu_filt_delta.csv'), header=['idSorteo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb', 'delta'], index=None, sep=',', mode='w')
        df_re_fu_filt.to_csv(Files.path_generator('O', 'df_re_fu_filt_delta.csv'), header=['idSorteo', 'n1', 'n2', 'n3', 'n4', 'n5', 'sb', 'delta'], index=None, sep=',', mode='w')
        return df_tr_fu_filt, df_re_fu_filt

    def conteo_files_saver(self, filename, df):
        df.to_csv(Files.path_generator('O', filename), header=['conteo', 'tupla'], index=None, sep=',', mode='w')
        return df

    def counting_readers(self):
        dfc.df_tr_fu_filt_delta = pd.read_csv(Files.path_generator('O', 'df_tr_fu_filt_delta.csv'))
        dfc.df_re_fu_filt_delta = pd.read_csv(Files.path_generator('O', 'df_re_fu_filt_delta.csv'))

        dfc.conteos_1d_sb_tr = pd.read_csv(Files.path_generator('O', 'conteos_1d_sb_tr.csv'))
        dfc.conteos_1d_sb_re = pd.read_csv(Files.path_generator('O', 'conteos_1d_sb_re.csv'))

        dfc.conteos_1d_tr = pd.read_csv(Files.path_generator('O', 'conteos_1d_tr.csv'))
        dfc.conteos_1d_re = pd.read_csv(Files.path_generator('O', 'conteos_1d_re.csv'))

        dfc.conteos_2d_tr = pd.read_csv(Files.path_generator('O', 'conteos_2d_tr.csv'))
        dfc.conteos_2d_re = pd.read_csv(Files.path_generator('O', 'conteos_2d_re.csv'))

        dfc.conteos_3d_tr = pd.read_csv(Files.path_generator('O', 'conteos_3d_tr.csv'))
        dfc.conteos_3d_re = pd.read_csv(Files.path_generator('O', 'conteos_3d_re.csv'))

        dfc.conteos_4d_tr = pd.read_csv(Files.path_generator('O', 'conteos_4d_tr.csv'))
        dfc.conteos_4d_re = pd.read_csv(Files.path_generator('O', 'conteos_4d_re.csv'))

        dfc.conteos_5d_tr = pd.read_csv(Files.path_generator('O', 'conteos_5d_tr.csv'))
        dfc.conteos_5d_re = pd.read_csv(Files.path_generator('O', 'conteos_5d_re.csv'))

        return dfc