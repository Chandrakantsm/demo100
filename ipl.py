import csv
sum=0
sumbatter=0
sumbowler=0
sumwkeeper=0
totalsum=0
with open("C:/Users/User4/Desktop/ipl_2023_dataset.csv","r")as ipl:
    file_handle = csv.reader(ipl)

    for i in file_handle:
        
        
        if i[4]=='Chennai Super Kings' and i[4]!="Unsold":
            if i[2]=="All-Rounder":
                sum=sum+float(i[3])
            elif i[2]=="Batter":
                sumbatter=sumbatter+float(i[3])  
            elif i[2]=="Bowler": 
                sumbowler=sumbowler+float(i[3])
            elif i[2]=="Wicket-Keeper":  
                sumwkeeper=sumwkeeper+float(i[3])  
        totalsum=sum+sumbatter+sumbowler+sumwkeeper
               
                    
print("amount spent by csk on all_rounders is",sum)  
print("amount spent by csk on batters is",sumbatter) 
print("amount spent by csk on all_rounders is",sumbowler) 
print("amount spent by csk on wicketkeepers is",sumwkeeper)
print("total amount spent by csk on players" ,totalsum) 
print("csk has spent ",sum/totalsum*100,"% on allrounders.")
  
