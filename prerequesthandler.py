
def prepare(input_data):
        instruction = "Please summarize the following text and provide key points."
      #  summary = "This text discusses the importance of data privacy and security in modern applications."
        summary = input_data.summary
        example = input_data.example

        #"For example, companies must ensure that user data is encrypted and access is restricted to authorized personnel only."
        #cues = "Key points to consider: encryption, access control, user consent."
        prompt = "for age group below "+input_data.age+" and place "+input_data.place+ " and language "+input_data.language
        cues = input_data.cues
        prepared_prompt = f"{instruction}\n\nSummary:\n{summary}\n\nExample:\n{example}\n\nCues:\n{cues}\n\n{prompt.strip()}"
        return prepared_prompt
