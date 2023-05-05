import csv
# sum=0
# sumbatter=0
# sumbowler=0
# sumwkeeper=0
# totalsum=0

set1=set([])
with open("C:/Users/User4/Desktop/ipl_2023_dataset.csv","r")as ipl:
    file_handle = csv.reader(ipl)
    #  create the list of teams in ipl
    for i in file_handle:
        set1.add(i(4))
    print(set1)    
        
    # team analysis
    # for i in file_handle:
        
        
    #     if i[4]=='Punjab Kings' and i[4]!="Unsold":
    #         if i[2]=="All-Rounder":
    #             sum=sum+float(i[3])
    #         elif i[2]=="Batter":
    #             sumbatter=sumbatter+float(i[3])  
    #         elif i[2]=="Bowler": 
    #             sumbowler=sumbowler+float(i[3])
    #         elif i[2]=="Wicket-Keeper":  
    #             sumwkeeper=sumwkeeper+float(i[3])  
    #     totalsum=sum+sumbatter+sumbowler+sumwkeeper
        
        
               
    # percent= round( sum/totalsum*100)              
    # print("amount spent by csk on all_rounders is",sum)  
    # print("amount spent by csk on batters is",sumbatter) 
    # print("amount spent by csk on all_rounders is",sumbowler) 
    # print("amount spent by csk on wicketkeepers is",sumwkeeper)
    # print("total amount spent by csk on players" ,totalsum) 
    # print("csk has spent ",(percent),"% on allrounders.")
  
    # if i[4]==i[4] and i[4]!="Unsold":
    #         if i[2]=="All-Rounder":
    #             sum=sum+float(i[3])
    #         elif i[2]=="Batter":
    #             sumbatter=sumbatter+float(i[3])  
    #         elif i[2]=="Bowler": 
    #             sumbowler=sumbowler+float(i[3])
    #         elif i[2]=="Wicket-Keeper":  
    #             sumwkeeper=sumwkeeper+float(i[3])  
    #         totalsum=sum+sumbatter+sumbowler+sumwkeeper