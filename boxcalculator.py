# Sizes 
Length = int(input("\n_LENGTH of box in mm_\n"))
Width = int(input("\n_WIDTH of box in mm_\n"))
Height = int(input("\n_HEIGHT of box in mm_\n"))
#decal
decal = (Width  + Height )
print("DECAL\n=")
print(decal)
#sheet size
Sheet_size= 2*(Length+Width)+50
print("SHEET SIZE\n")
print(Sheet_size)
#No_OF_PLIES
No_OF_PLIES =int(input("NO_OF_PLY\n="))
if No_OF_PLIES == 3:
    Ply1=int(input("GSM-1=\n"))
    Ply2=int(input("GSM-2=\n"))
    Ply3=int(input("GSM-3=\n"))
    Board_GSM= (Ply1+(1.5*Ply3)+Ply3)
    print("Board_GSM")
    print(Board_GSM)   
elif No_OF_PLIES == 5:
    Ply1=int(input("GSM-1=\n"))
    Ply2=int(input("GSM-2=\n"))
    Ply3=int(input("GSM-3=\n"))
    Ply4=int(input("GSM-4=\n"))
    Ply5=int(input("GSM-5=\n"))
    Board_GSM=(Ply1+(Ply2*1.5)+Ply3+(Ply4*1.5)+Ply5)
    print("Board_GSM")
    print(Board_GSM)  
Weight=((decal*Sheet_size*Board_GSM)/1550)/1000#To_covert_amount_of_weight_into_grams.
print("WEIGHT")
print(Weight)
Current_Paper_Rate=int(input("Current_Papr_Rate\n"))
Conversion_rate=int(input("Conversion_rate\n"))
coversion_charges= Weight*(Conversion_rate)
Box_Rate=((Weight*Current_Paper_Rate)+Conversion_rate)/1000
print("Rate_OF_BOX\n")
print(f"Rs:.{Box_Rate}")













    
    


