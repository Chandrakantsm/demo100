import csv
# sum_allrounder=0
# sum_batter=0
# sum_bowler=0
# sum_wkeeper=0
# total_sum=0

set1=set()
with open("C:/Users/User4/Desktop/ipl_2023_dataset.csv","r")as ipl:
    file_handle = csv.reader(ipl)
    
    #  create the list of teams in ipl
    
    for i in file_handle:
        if i[4]!="Team" and i[4]!="Unsold":
            set1.add(i[4])
    print("\n****The list of teams in IPL-2020 are as below****\n\n", set1,"\n")  
    list1=list(set1) 
    print(list1)
    
    # # findings of amount spent  per skill set per team
    for i in list1:
        calculate(i)
        def calculate():
            for i in file_handle:
            
        
                if i[4]=='Punjab Kings' and i[4]!="Unsold":
                    if i[2]=="All-Rounder":
                        sum_allrounder=sum_allrounder+float(i[3])
                    elif i[2]=="Batter":
                        sum_batter=sum_batter+float(i[3])  
                    elif i[2]=="Bowler": 
                        sum_bowler=sum_bowler+float(i[3])
                    elif i[2]=="Wicket-Keeper":  
                        sum_wkeeper=sum_wkeeper+float(i[3])  
            total_sum=sum_allrounder+sum_batter+sum_bowler+sum_wkeeper
       
        
    
    # for i in list1:
    #     sum_allrounder=0
    #     sum_batter=0
    #     sum_bowler=0
    #     sum_wkeeper=0
    #     total_sum=0
    #     for k in file_handle:
    #         if k[2]=="All-Rounder":
    #             sum_allrounder=sum_allrounder+float(k[3])
    #         elif k[2]=="Batter":
    #             sum_batter=sum_batter+float(k[3])  
    #         elif k[2]=="Bowler": 
    #             sum_bowler=sum_bowler+float(k[3])
    #         elif k[2]=="Wicket-Keeper":  
    #             sum_wkeeper=sum_wkeeper+float(k[3])  
    #     total_sum=sum_allrounder+sum_batter+sum_bowler+sum_wkeeper
    #     print(k,total_sum)
      
        # if i[2]=="All-Rounder":
        #     sum_allrounder=sum_allrounder+float(i[3])
        # elif i[2]=="Batter":
        #         sum_batter=sum_batter+float(i[3])  
        # elif i[2]=="Bowler": 
        #         sum_bowler=sum_bowler+float(i[3])
        # elif i[2]=="Wicket-Keeper":  
        #         sum_wkeeper=sum_wkeeper+float(i[3])  
        # total_sum=sum_allrounder+sum_batter+sum_bowler+sum_wkeeper
        # print(i,sum_allrounder,sum_batter,sum_bowler,sum_wkeeper,total_sum)
        
    
        
    # team analysis    this code is giving result
    # for i in file_handle:
        
        
    #     if i[4]=='Punjab Kings' and i[4]!="Unsold":
    #         if i[2]=="All-Rounder":
    #             sum_allrounder=sum_allrounder+float(i[3])
    #         elif i[2]=="Batter":
    #             sum_batter=sum_batter+float(i[3])  
    #         elif i[2]=="Bowler": 
    #             sum_bowler=sum_bowler+float(i[3])
    #         elif i[2]=="Wicket-Keeper":  
    #             sum_wkeeper=sum_wkeeper+float(i[3])  
    #     total_sum=sum_allrounder+sum_batter+sum_bowler+sum_wkeeper
        
        
               
    # percent= round( sum_allrounder/total_sum*100)              
    # print("amount spent by csk on all_rounders is",sum_allrounder)  
    # print("amount spent by csk on batters is",sum_batter) 
    # print("amount spent by csk on all_rounders is",sum_bowler) 
    # print("amount spent by csk on wicketkeepers is",sum_wkeeper)
    # print("total amount spent by csk on players" ,total_sum) 
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