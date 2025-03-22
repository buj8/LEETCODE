class Solution:
    


    
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        idea    -> separate between letter logs and number logs 
                -> sort letter logs 
                -> append number logs to letter logs
        '''
        letter_logs = []
        number_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                number_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda x: x.split()[0])
        letter_logs.sort(key=lambda x: x.split()[1:])    
          

        return letter_logs + number_logs
        