# bu dastur testni natijalarini hisoblab chiqish uchun ishlatiladi
dataset = "fr"  # [uz,en,ru,sl] new dataset [de,es,fr,kz,ms,pl,tr,tt]
cc = 8  # cubes number 5-8

for app in range(2):
    for iteration in range(5):

        with open("result/test_"+dataset+"/test"+str(iteration), encoding="utf8") as file:  #
            lines = file.readlines()
            words_c = [line.rstrip().split(',')[0] for line in lines]
        t3 = 0
        t4 = 0
        t5 = 0
        for i in words_c:
            if len(i) == 3:
                t3 += 1
            if len(i) == 4:
                t4 += 1
            if len(i) == 5:
                t5 += 1

        with open("result/test_"+dataset+"/"+str(cc)+"cub/test_res_app"+str(app)+"_it"+str(iteration), encoding="utf8") as file: #
            lines = file.readlines()
            words_c = [line.rstrip().split(',')[0] for line in lines]
        cnt3 = 0
        cnt4 = 0
        cnt5 = 0
        for i in words_c:
            if len(i) == 3:
                cnt3 += 1
            if len(i) == 4:
                cnt4 += 1
            if len(i) == 5:
                cnt5 += 1
        print(app, '\t', iteration, '\t', (t3+t4+t5), '\t', t3, '\t', t4, '\t', t5)
        print(app, '\t', iteration, '\t', (cnt3+cnt4+cnt5), '\t', cnt3, '\t', cnt4, '\t', cnt5)
        print(app, '\t', iteration, '\t', round(len(words_c) / (t3 + t4 + t5) * 100, 1), '\t', round(cnt3 / t3 * 100, 3), '\t', round(cnt4 / t4 * 100, 3), '\t', round(cnt5 / t5 * 100, 3))
    print()