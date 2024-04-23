class Pad:

    def __init__(self, s_no="", pad_eng_name="", pad_hin_guj_name="", mp3_url="", pdf_url=""):
        self.s_no = s_no
        self.pad_hin_guj_name = pad_hin_guj_name
        self.pad_eng_name = pad_eng_name
        self.mp3_url = mp3_url
        self.pdf_url = pdf_url

    def __str__(self):
        attributes = [self.s_no, self.pad_hin_guj_name, self.pad_eng_name, self.mp3_url, self.pdf_url]
        return "\n".join(str(attr) for attr in attributes if attr) + "\n\n"