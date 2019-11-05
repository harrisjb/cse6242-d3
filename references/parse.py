import pandas as pd


def parse():
    file_w = open('./ndcfile.tsv', 'w')
    header_out = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
        'ndc',
        'ingredient_key',
        'e77_flag',
        'no_ingredients',
        'csa_schedule',
        'un_schedule',
        'psychotropic_sched',
        'trade_product_name',
        'package_quantity',
        'package_measure',
        'drug_code',
        'salt_code',
        'ingredient_name',
        'ingredient_base_weight'
    )
    file_w.write(header_out)
    file_r = open('./National_Drug_Dictionary_ndcfile.txt', 'r')
    line_num=1
    for line in file_r:
        if line_num == 100:
            pass
        line_num +=1
        #print(line)
        if line.find("\t") != -1:
            print(line)
        ndc                    = line[0:11]    #  11                    1        11
        ingredient_key         = line[11:12]   #  1                     12       12
        e77_flag               = line[12:13]   #  1                     13       13
        no_ingredients         = line[13:14]   #  1                     14       14
        csa_schedule           = line[14:16]   #  2                     15       16
        un_schedule            = line[16:17]   #  1                     17       17
        psychotropic_sched     = line[17:18]   #  1                     18       18
        trade_product_name     = line[18:54]   #  36                    19       54
        package_quantity       = line[54:63]   #  9  (999999V999)       55       63
        package_measure        = line[63:68]   #  5                     64       68
        drug_code              = line[68:76]   #  8                     69       76
        salt_code              = line[76:80]   #  4                     77       80
        ingredient_name        = line[80:131]  #  51                    81       131
        ingredient_base_weight = line[131:144] #  13 (999999V9999999)   132      144

        line_out = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
            ndc,
            ingredient_key,
            e77_flag,
            no_ingredients,
            csa_schedule.strip(),
            un_schedule,
            psychotropic_sched,
            trade_product_name.strip(),
            package_quantity,
            package_measure.strip(),
            drug_code.strip(),
            salt_code.strip(),
            ingredient_name.strip(),
            ingredient_base_weight
        )
        #print(line_out)
        file_w.write(line_out)


if __name__=="__main__":
    parse()
    df1 = pd.read_csv('./ndcfile.tsv', sep='\t')
    print(df1.head())