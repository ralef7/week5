class CoinDispenser:


    coins = [25, 10, 5, 1]

    def make_change(self, amount):
        if amount <= 4:
            x = amount
            return [0,0,0,x]

        elif amount >= 5 and amount < 10:
            x = amount // 5
            y = amount % 5
            return[0,0,x,y]
        elif amount >= 10 and amount <= 24:
            y = amount //10
            x = (amount % 10)  // 5     
            z = amount -(10*y + 5*x)
            return[0,y,x,z]
        elif amount >= 25:
            w = amount // 25
            y = (amount - (w*25)) // 10
            x = (amount - ((w*25)+(y*10))) // 5
            z = (amount - ((w*25)+(y*10)+(x*5)))
            return[w,y,x,z]
            
        
            
        
    
            
        
     
          
        
    
