number_of_flat = int(input('Введите номер квартиры \n'))
etazh = int(input('Введи количество этажей \n'))
kol_vo_kvartir = int(input('Введи количество квартир на этаже \n'))
kvartir_v_padike = etazh * kol_vo_kvartir
if number_of_flat%kvartir_v_padike ==0:
    nomer_padika = number_of_flat // kvartir_v_padike
else:
    nomer_padika = number_of_flat // kvartir_v_padike + 1

etazh = (number_of_flat - (nomer_padika - 1) * kvartir_v_padike + 1) // kol_vo_kvartir

print('тебе нужен падик номер ', nomer_padika, 'и этаж номер ', etazh)