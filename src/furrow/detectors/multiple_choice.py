class MultipleChoiceDetector():

    def __init__(self, text):
        self.text = text


    def detect(self):

        tokens = []
        mult = ""
        mult_start = None
        mult_end = None

        for i in range(len(self.text)):
            current = self.text[i]
            prev_char = self.text[i - 1] if i > 0 else " "

            ## need the next for looking ahead
            next1 = self.text[i+1] if i+1 < len(self.text) else ""
            next2 = self.text[i+2] if i+2 <len(self.text) else ""

            if current.isupper() and current in {"A", "B", "C", "D"}:
                if not (prev_char == " " or prev_char == "\n"):
                    continue

                if mult == "":
                    mult_start = i

                mult+= current

                # Scenario for when the multiple choice has no space but it has something like BTemple
                # we know its a multiple choice choice

                if next1.isupper() and next2.islower():
                    mult_end = i

                    token = {

                        "type": "multiple choice",
                        "value": mult,
                        "start": mult_start,
                        "end": mult_end,
                        "period_position": i + 1 
                    }
                    tokens.append(token)

                    mult = ""

                    mult_start = None

            else:
                if mult != "":
                    mult_end = i-1


                    token = {
                        "type":"multiple choice",
                         "value":mult,
                         "start":mult_start,
                         "end": mult_end,
                         "period_position": None
                        }


                    tokens.append(token)
                    mult = ""
                    mult_start = None

            if current == "." or current == " " or current == ")":
                period_pos = i

                if tokens:
                    last = tokens[-1]

                    distance = period_pos - last["end"]

                    if distance <= 3:
                        last["period_position"] = period_pos

        return tokens








