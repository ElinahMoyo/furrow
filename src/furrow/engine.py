class Plow:
    def __init__(self,input_data):
        self.text = input_data
        self.token = []
        self._has_run = False

    def run(self):
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

                    current_number_data = {
                        "number": number,
                        "start": number_start,
                        "end": number_end ,
                        "period_position": None
                         }
                    self.token.append(current_number_data)

                    number = ""
                    number_start = None
                    active_number = False

            if current == ".":
                period_pos = i

                if self.token:
                    last = self.token[-1]

                    distance = period_pos-last["end"]

                    if distance <=3:
                        last["period_position"] = period_pos

        self._has_run = True

    def collect(self):
        """Gathers the split text chunks into structured question nodes."""

        if not self._has_run:
            self.run()

        for item in self.token:
            if item["period_position"] is None:
                item["is_question"] = False

            else:
                distance = item["period_position"]- item["end"]

                if distance <=3:
                    item["is_question"]= True

                else:
                    item["is_question"]= False

        ## slice between

        for i in range(len(self.token)):
            if not self.token[i]["is_question"]:
                continue

            start = self.token[i]["period_position"]
            end = len(self.text)

            for j in range(i+1, len(self.token)):
                if self.token[j]["is_question"]:
                    end = self.token[j]["start"]
                    break

            self.token[i]["text"] = self.text[start:end]


        questions = []

        for item in self.token:
            if item.get("is_question"):
                questions.append({
                    "question_number": item["number"],
                    "text": item["text"]
                })

        return questions    


    def render(self):

        ### inject lines but not losing the non questions
        if not self._has_run:
            self.run()

        if not self.token:
            return self.text

        valid_questions = [item for item in self.token if item.get("is_question")]

        if not valid_questions:
            return self.text

        formatted_pieces = []
        current_index = 0

        for item in valid_questions:
            start_pos = item["start"] 
            formatted_pieces.append(self.text[current_index:start_pos])
            formatted_pieces.append("\n")
            current_index = start_pos

        formatted_pieces.append(self.text[current_index:])
        return "".join(formatted_pieces) 

