class NumberDetector:
    def __init__(self,text):
        self.text = text

    def detect(self):
        tokens = []
        #oky now we search ch boundaried to find indexes
        number = ""
        number_start = None
        number_end = None
        period_pos = None

        active_number = False

        for i in range(len(self.text)):
            current = self.text[i]

            if current.isdigit():
                if not active_number:
                    number_start = i
                    active_number = True

                number+= current
            else:
                if number != "":
                    number_end = i-1

                    token = {
                        "type": "number",
                        "value": number,
                        "start": number_start,
                        "end": number_end ,
                        "period_position": None
                         }
                    tokens.append(token)

                    number = ""
                    number_start = None
                    active_number = False

            if current == "." or current == ")":
                period_pos = i

                if tokens:
                    last = tokens[-1]

                    distance = period_pos-last["end"]

                    if distance <=3:
    
                        last["period_position"] = period_pos

        
        return tokens



            