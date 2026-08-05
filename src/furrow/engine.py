class Plow:
    def __init__(self,text,detectors):
        self.text = text
        self.detectors = detectors
        self.token = []
        self._has_run = False

    def run(self):
        for detector in self.detectors:
            detector_instance = detector(self.text)
            detected_tokens = detector_instance.detect()

            self.token.extend(detected_tokens)

        self.token.sort(key=lambda x: x["start"])
        self._has_run = True

    def collect(self):
        """Gathers the split text chunks into structured question nodes."""

        if not self._has_run:
            self.run()

        for item in self.token:
            if item.get("period_position") is None:
                item["is_boundary"] = False ## thinking we should use item type on is_question

            else:
                distance = item["period_position"]- item["end"]

                if distance <=3:
                    item["is_boundary"]= True

                else:
                    item["is_boundary"]= False

        ## slice between

        for i in range(len(self.token)):
            if not self.token[i]["is_boundary"]:
                continue

            start = self.token[i]["period_position"]
            end = len(self.text)

            for j in range(i+1, len(self.token)):
                if self.token[j]["is_boundary"]:
                    end = self.token[j]["start"]
                    break

            self.token[i]["text"] = self.text[start:end]


        results = []

        for item in self.token:
            if item.get("is_boundary"):
                results.append({
                    "marker":item["value"],
                    "marker_type": item["type"],
                    "text": item["text"]
                })

        return results    


    def render(self):

        ### inject lines but not losing the non questions
        if not self._has_run:
            self.run()

        

        boundaries = [item for item in self.token if item.get("is_boundary")]

        if not boundaries:
            return self.text

        formatted_pieces = []
        current_index = 0

        for item in boundaries:
            start_pos = item["start"] 

            if start_pos > current_index:
                formatted_pieces.append(self.text[current_index:start_pos])
                formatted_pieces.append("\n")
                
            current_index = start_pos

        formatted_pieces.append(self.text[current_index:])
        return "".join(formatted_pieces) 

