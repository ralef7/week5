class CoinDispenser:


    coins = [25, 10, 5, 1]

    def make_change(self, amount):
        if amount <= 4:
            return [0,0,0,amount]

        elif amount % 5 == 0 and amount < 10:
            return[0,0,amount//5,0]

        elif amount > 5 and amount < 10: 
            return[0,0,amount//5,amount%5]
        elif amount >= 10 and amount <= 24:
            y = amount //10
            x = (amount % 10)  // 5     
            z = amount -(10*y + 5*x)
            return[0,y,x,z]
        elif amount >= 25:
            w = amount // 25
            y = (amount - (w*25)) // 10
            x = 0
            z = amount - ((w*25)+(y*10))
            return[w,y,x,z]
            
        
            
        
    
            
        
     
          
        
    
