def get_btn_category() -> list:

    btn, kb = [], []
    with open('category.txt', 'r') as cat:
        cat_lst = cat.readlines()
        #print(cat_lst)
        for i in range(2, len(cat_lst)):
            if i not in [2, 5, 8, 11, 14, 17, 20, 23, 26]:
                continue
            else:
                btn1 = str(cat_lst[i-2].split('\t')[0])
                btn2 = str(cat_lst[i-1].split('\t')[0])
                btn3 = str(cat_lst[i].split('\t')[0])
                btn = [btn1, btn2, btn3]
                kb.append(btn)
            
    return kb
