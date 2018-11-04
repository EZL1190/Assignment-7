import matplotlib.pyplot as plt

def task1(data):
    p_pladser = 0
    p_pladser_højst = 0
    vej_navn = ''
    for row in data:
        if row['bydel'] == 'Indre By':
            antal_pladser = row['antal_pladser']
            p_pladser += antal_pladser
            if antal_pladser > p_pladser_højst:
                p_pladser_højst = antal_pladser
                vej_navn = row['vejnavn']

    return 'Der er ' + str(p_pladser) + ' i indre by, vejen med flest pladser er: ' + vej_navn

def task2(data):
    p_pladser_lige = 0
    p_pladser_ulige = 0
 
    p_pladser_lige_afmearkede = 0
    p_pladser_ulige_afmearkede = 0

    for row in data:
        if row['vejside'] == 'Lige husnr.':
            p_pladser_lige += int(row['antal_pladser'])
            if row['p_type'] == 'Afmærket parkering':
                p_pladser_lige_afmearkede += int(row['antal_pladser'])
        else:
            p_pladser_ulige += int(row['antal_pladser'])
            if row['p_type'] == 'Afmærket parkering':
                p_pladser_ulige_afmearkede += int(row['antal_pladser'])
    tmp_str = 'P-pladser på lige husnr. side: ' + str(p_pladser_lige) + ', '
    tmp_str += 'P-pladser på ulige husnr. side: ' + str(p_pladser_ulige) + ', '
    tmp_str += 'Afmærkede parkeringsbåse på lige husnr. side: ' + str(p_pladser_lige_afmearkede) + ', '
    tmp_str +=  'Afmærkede parkeringsbåse på ulige husnr. side: ' + str(p_pladser_ulige_afmearkede)

    return tmp_str

def task3(data):
    bydel_p_pladser_offentlig = {}
    bydel_p_pladser_privat = {}

    for row in data:
        if row['p_ordning'] == 'Privat ordning':
            bydel_p_pladser_privat.setdefault(row['bydel'], int(row['antal_pladser']))
            bydel_p_pladser_privat[row['bydel']] += int(row['antal_pladser'])
        else:
            bydel_p_pladser_offentlig.setdefault(row['bydel'], int(row['antal_pladser']))
            bydel_p_pladser_offentlig[row['bydel']] += int(row['antal_pladser'])

    bydel_p_pladser_offentlig_procent = {}
    bydel_p_pladser_privat_procent = {}

    for key in bydel_p_pladser_offentlig:
        procent_decimal = 100 / (bydel_p_pladser_offentlig[key] + bydel_p_pladser_privat[key]) * bydel_p_pladser_offentlig[key] / 100
        bydel_p_pladser_offentlig_procent[key] = round(procent_decimal, 3)

    for key in bydel_p_pladser_privat:
        procent_decimal = 100 / (bydel_p_pladser_offentlig[key] + bydel_p_pladser_privat[key]) * bydel_p_pladser_privat[key] / 100
        bydel_p_pladser_privat_procent[key] = round(procent_decimal, 3)

    #print(bydel_p_pladser_offentlig_procent)
    #print(bydel_p_pladser_privat_procent)

    bydel_procent_offentlig_list = []
    bydel_procent_privat_list = []
    bydel_text = ['','Amager Vest','Amager Øst','Bispebjerg','Brønshøj-Husum','Indre By','Nørrebro','Valby','Vanløse','Vesterbro-Kongens Enghave','Østerbro']

    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent[''])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Amager Vest'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Amager Øst'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Bispebjerg'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Brønshøj-Husum'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Indre By'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Nørrebro'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Valby'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Vanløse'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Vesterbro-Kongens Enghave'])
    bydel_procent_offentlig_list.append(bydel_p_pladser_offentlig_procent['Østerbro'])

    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent[''])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Amager Vest'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Amager Øst'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Bispebjerg'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Brønshøj-Husum'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Indre By'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Nørrebro'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Valby'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Vanløse'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Vesterbro-Kongens Enghave'])
    bydel_procent_privat_list.append(bydel_p_pladser_privat_procent['Østerbro'])
    
    plt.bar(bydel_text, bydel_procent_offentlig_list, 1/1.5, color="blue")
    plt.bar(bydel_text, bydel_procent_privat_list, 1/1.5, color="red")
    plt.title('Offentlig = blå, Privat = rød', fontsize=12)
    plt.xlabel('Bydel', fontsize=12)
    plt.ylabel('Procent', fontsize=12)
    plt.show()

def task4(data, data2):
    my_dict = {}
    my_dict2 = {}
    for row in data:
        my_dict.setdefault(row['bydel'], 0)
        my_dict[row['bydel']] += row['antal_pladser']
    for row in data2:
        if 'sterbro' == row['distriktsnavn']:
            my_dict2.setdefault(row['familietype'], 0)
            my_dict2[row['familietype']] += 1
    print(my_dict2)


def taskt5(data, data2):
    
    gennemsnitlig_bruttoindkomst = {}
    antal_per_bydel = {}
    
    for row in data2:
        gennemsnitlig_bruttoindkomst.setdefault(row['distriktsnavn'], 0)
        gennemsnitlig_bruttoindkomst[row['distriktsnavn']] += int(row['bruttoindkom'])

    for row in data2:
        antal_per_bydel.setdefault(row['distriktsnavn'], 0)
        antal_per_bydel[row['distriktsnavn']] += 1

    print(gennemsnitlig_bruttoindkomst)
    return














