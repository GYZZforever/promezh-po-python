import math

def calculate_material(prod_type_id, mat_type_id, count, param1, param2):
    product_coeffs = {1: 1.1, 2: 2.5, 3: 8.43}
    material_scraps = {1: 0.003, 2: 0.012} # 0.3% и 1.2%
    
    if prod_type_id not in product_coeffs or mat_type_id not in material_scraps:
        return -1
    
    if count <= 0 or param1 <= 0 or param2 <= 0:
        return -1

    # (параметры * коэффициент) * количество
    one_unit = param1 * param2 * product_coeffs[prod_type_id]
    total_needed = one_unit * count
    
    # добавляем брак
    total_with_scrap = total_needed / (1 - material_scraps[mat_type_id])
    
    return math.ceil(total_with_scrap)
