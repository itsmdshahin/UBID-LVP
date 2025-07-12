def calculate_lvp(hours, skill_weight=1.5, region_factor=1.2):
    return round(hours * skill_weight * region_factor, 2)
