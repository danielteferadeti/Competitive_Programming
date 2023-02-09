class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        dateArray = date.split(' ')
        print(dateArray)
        
        ans = dateArray.pop() + "-" + months[dateArray.pop()] + "-"
        day = dateArray.pop()
        num = ""
        for char in day:
            if char.isnumeric():
                num += char
            else: break
        
        ans = ans + num if len(num) >=2 else ans + "0" + num
        
        return ans 