class util:
    deltas = {
        0: "=", 1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
        13: "M", 14: "N", 15: "Ñ", 16: "O", 17: "P", 18: "Q",
        19: "R", 20: "S", 21: "T", 22: "U", 23: "V", 24: "W", 25: "X", 26: "Y", 27: "Z", 28: "@", 29: "a", 30: "b",
        31: "c", 32: "d", 33: "e", 34: "f", 35: "g", 36: "h", 37: "i",
        38: "j", 39: "k", 40: "l", 41: "m", 42: "n", 43: "ñ", 44: "o", 45: "p", 46: "q", 47: "r", 48: "s", 49: "t",
        50: "u", 51: "v", 52: "w", 53: "x", 54: "y", 55: "z"
    }

    weights = {
        0: "0.0", 1: "0.1", 2: "0.2", 3: "0.3", 4: "0.4", 5: "0.5", 6: "0.6", 7: "0.7", 8: "0.8", 9: "0.9"
    }

    sbs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
    categorical_cols = ['tipo', 'ganador']
    unuseful_cols = ['fecha', 'nuevo']
    main_columns = ['n1', 'n2', 'n3', 'n4', 'n5', 'sb', 'tipo', 'ganador']

    def construir_linea(sorteo, fecha, tiposorteo, winner, nuevo, n1, n2, n3, n4, n5, sb):
        salida = str(sorteo) + "," + str(fecha) + "," + str(tiposorteo) + "," + str(winner) + "," + str(
            nuevo) + "," + str(n1) + "," + str(n2) + "," + str(n3) + "," + str(n4) + "," + str(n5) + "," + str(sb)
        return salida

    def cantidad_no_rep(singles):
        l = singles.sort_values("tupla")
        l2 = l.drop('R', 1)
        l3 = l2.drop_duplicates()
        print(l3)
        return l3

    def validar_quinteto_list(singles):
        l = singles.sort_values("tupla")
        l2 = l.drop('R', 1)
        l3 = l2.drop_duplicates()
        return l3

    def secuencelist_unbuilder(secuence):
        num = str(secuence[0])
        partido = num.split(sep='|') if (num.find('|') >= 1) else num
        return partido

    def secuencelist_builder(a, b, c, d, e):
        secuencia = []
        secuencia.append(a)
        secuencia.append(b)
        secuencia.append(c)
        secuencia.append(d)
        secuencia.append(e)
        palabra = '|'.join([str(et) for et in secuencia])
        return palabra, secuencia

    def crea_secuencias(totalconteo):
        secuencias = []
        secuence = []
        lsecuence = []
        secuencia = []
        i = 0
        a = i
        b = a + 1
        c = b + 1
        d = c + 1
        e = d + 1
        while (a <= totalconteo):
            while (b <= totalconteo):
                while (c <= totalconteo):
                    while (d <= totalconteo):
                        while (e <= totalconteo):
                            secuencia, secuence = util.secuencelist_builder(a, b, c, d, e)
                            secuencias.append(secuencia)
                            lsecuence.append(secuence)
                            e += 1
                        d += 1
                        e = d + 1
                    c += 1
                    d = c + 1
                    e = d + 1
                b += 1
                c = b + 1
                d = c + 1
                e = d + 1
            a = a + 1
            b = a + 1
            c = b + 1
            d = c + 1
            e = d + 1
        return secuencias, lsecuence

    def delta_translator(numero1, numero2, suma):
        if (suma > 0):
            return util.deltas[(suma - numero1) + numero2]
        else:
            return util.deltas[numero2 - numero1]

    def word_maker(ent1, ent2, ent3, ent4, ent5):
        valDefec = 0
        maxValBal = 43
        listik = []
        listik.append(util.delta_translator(ent1, ent2, valDefec))
        listik.append(util.delta_translator(ent2, ent3, valDefec))
        listik.append(util.delta_translator(ent3, ent4, valDefec))
        listik.append(util.delta_translator(ent4, ent5, valDefec))
        listik.append(util.delta_translator(ent5, ent1, maxValBal))
        word = "".join(listik)
        return word

    def tuple_maker(ent1, ent2, ent3, ent4, ent5, cant):
        listik = []
        if (cant >= 1):
            listik.append(str(ent1))
        if (cant >= 2):
            listik.append("|" + str(ent2))
        if (cant >= 3):
            listik.append("|" + str(ent3))
        if (cant >= 4):
            listik.append("|" + str(ent4))
        if (cant >= 5):
            listik.append("|" + str(ent5))
        palabra = "".join(listik)
        return palabra

    def addcolumntuplas(df, cant):
        tupla = []
        val_defecto = 0
        df.to_frame()
        df2 = df.rename(None).to_frame().T
        for index, row in df2.iteritems():
            if (cant == 1):
                tupla.append(util.tuple_maker(index, val_defecto, val_defecto, val_defecto, val_defecto, cant))
            if (cant == 2):
                tupla.append(util.tuple_maker(index[0], index[1], val_defecto, val_defecto, val_defecto, cant))
            if (cant == 3):
                tupla.append(util.tuple_maker(index[0], index[1], index[2], val_defecto, val_defecto, cant))
            if (cant == 4):
                tupla.append(util.tuple_maker(index[0], index[1], index[2], index[3], val_defecto, cant))
            if (cant == 5):
                tupla.append(util.tuple_maker(index[0], index[1], index[2], index[3], index[4], cant))
        dft = df2.T
        dft['tupla'] = tupla
        dft = dft.reset_index(drop=True)
        return dft