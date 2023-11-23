import sus2ymst

with open("test.sus", "r") as f:
    sus_text = f.read()
    notation_text, error = sus2ymst.loads(sus_text)
    print(notation_text)
    print(error)
