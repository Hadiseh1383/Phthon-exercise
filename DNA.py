import re 

class Oct: 
    def init(self, DNA): 
        self.dna = DNA 
    
    def oct_revised_dna(self):         
        dna = str(self.dna) 
        for i in range(len(dna)): 
            if dna[i] == 'x': 
                dna += str(i) 
                break 
        for i in range(len(dna)-2): 
            if dna[i] == dna[i+1] == dna[i+2]: 
                dna = dna.replace(dna[i]+dna[i+1]+dna[i+2],'(0_0)') 
        return dna 

class Crab: 
    def init(self, DNA): 
        self.dna = DNA 
    
    def crab_revised_dna(self): 
        dna = str(self.dna)         
        dna += dna[:10] 
        dna = dna.replace('tt','o') 
        return dna 

class Bob(Crab): 
    def merge(self, left, right): 
        merged = [] 
        right_index = 0 
        left_index = 0 
        
        while left_index < len(left) and right_index < len(right): 
            if left[left_index] <= right[right_index]: 
                merged.append(left[left_index]) 
                left_index +=1 
            else: 
                merged.append(right[right_index]) 
                right_index +=1 
        
        while left_index < len(left): 
            merged.append(left[left_index]) 
            left_index +=1    
        
        while right_index < len(right): 
            merged.append(right[right_index]) 
            right_index +=1 
        
        return merged  
    
    def merge_sort(self, lst): 
        if len(lst) <= 1 : 
            return lst 
        
        mid = len(lst) // 2 
        left_half = lst[:mid] 
        right_half = lst[mid:] 
        
        left = self.merge_sort(left_half) 
        right = self.merge_sort(right_half) 
        
        return self.merge(left, right) 

dna = input() 

matched_dna = re.fullmatch('^s[^b].*', dna) 

if matched_dna != None: 
    dara = Oct(dna) 
    print(dara.oct_revised_dna()) 

else: 
    matched_dna = re.fullmatch('^m.*', dna) 
    
    if matched_dna != None: 
        dara = Crab(dna) 
        print(dara.crab_revised_dna()) 
    
    else: 
        matched_dna = re.fullmatch('^sb.*', dna) 
        
        if matched_dna != None: 
            dara = Bob(dna) 
            dna = dara.crab_revised_dna() 
            print(”.join(dara.merge_sort(list(str(len(dna)))))) 
        
        else: 
            matched_dna = re.fullmatch('^s[^b].*', dna[::-1]) 
            
            if matched_dna != None: 
                dara = Oct(dna[::-1]) 
                print(dara.oct_revised_dna()) 
            
            else: 
                matched_dna = re.fullmatch('^m.*', dna[::-1]) 
                
                if matched_dna != None: 
                    dara = Crab(dna[::-1]) 
                    print(dara.crab_revised_dna()) 
                
                else: 
                    matched_dna = re.fullmatch('^sb.*', dna[::-1]) 
                    
                    if matched_dna != None: 
                        dara = Bob(dna[::-1]) 
                        dna = dara.crab_revised_dna() 
                        print(”.join(dara.merge_sort(list(str(len(dna)))))) 
                    
                    else: 
                        print('Invalid input')
