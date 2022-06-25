class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        
        letter_log = []
        digit_log = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digit_log.append(log)
            else:
                """
                letter_log = [
                    [let1,art,can],
                    [let2,own,kit,dig],
                    [let3,art,zero],
                ]
                
                """
                letter_log.append(log.split())
        
        letter_log.sort(key = lambda x: x[0]) # Sort by their identifier
        print(letter_log)
        letter_log.sort(key = lambda x: x[1:]) # Sort by the contents right after identifier
        
        res = []
        for log in letter_log:
            
            res.append(' '.join(log))
        
        for log in digit_log:
            res.append(log)
            
        return res
            
