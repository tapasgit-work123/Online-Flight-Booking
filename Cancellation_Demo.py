# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:53:49 2022

@author: Tapas
"""

import pymongo

if __name__=="__main__":
    client=pymongo.MongoClient("mongodb://localhost:27017")
    db=client['Refund_Details']
    collection=db['Customer_Details']
    
    db.Customer_Details.aggregate([
    {
        '$lookup': {
            'from': "Ticket_Details",
            'localField': "Passport_Id",
            'foreignField': "Passport_Id",
            'as': "Customer_Ticket_Details"
        }
    },
    {
      '$lookup': {
            'from': "Payment_Details",
            'localField': "Passport_Id",
            'foreignField': "Passport_Id",
            'as': "Customer_Payment_Details"
        }  
    },
    {'$project': {
        "_id":0,
        "Passport_Id":0,
        "Login_Id":0,

        }
    },
    {
        '$out' : "Verification_Details"                         
    },
         ])
    
    res1=db.Verification_Details.find({'Customer_Ticket_Details': {'$elemMatch': {'Passport_Id':'81-7489837'}}})
    for i in res1:
        print(i['Customer_Ticket_Details'])        ## To check cancellation and departure date
    
        
    res3=db.Payment_Details.find({"Passport_Id": "81-7489837"})
    for i in res3:
        print(i['Mode'])                                ## To check for mode of payment
        if(i['Mode']=='Card'):
            print("Amount would be credited in next 14 business days")
        else:
            print("Amount would be credited in next 3 business days")
            
            

            
        
        
       
        