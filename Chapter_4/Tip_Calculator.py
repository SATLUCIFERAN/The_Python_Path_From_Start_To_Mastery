

def calculate_total_bill(total_bill, tip_percentage):
    
    tip_amount = total_bill * (tip_percentage / 100)
    final_amount = total_bill + tip_amount  
    return final_amount

dinner_at_mos_eisley = calculate_total_bill(100, 15)
jabba_the_hutts_tab = calculate_total_bill(5000, 20)


print(f"Your bill at Mos Eisley is: {dinner_at_mos_eisley} credits.")
print(f"Jabba the Hutt's final bill is: {jabba_the_hutts_tab} credits.")