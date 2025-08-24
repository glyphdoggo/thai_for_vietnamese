import tkinter as tk

# Create a dictionary for vowel mappings
vowel_a = 'aàáạảã'
vowel_ă = 'ăằắặẳẵ'
vowel_â = 'âầấậẩẫ'
vowel_e = 'eèéẹẻẽ'
vowel_ê = 'êềếệểễ'
vowel_i = 'iìíịỉĩyỳýỵỷỹ'
vowel_o = 'oòóọỏõ'
vowel_ô = 'ôồốộổỗ'
vowel_ơ = 'ơờớợởỡ'
vowel_u = 'uùúụủũ'
vowel_ư = 'ưừứựửữ'
# vowel_y = 'yỳýỵỷỹ'

diph_ưa = ['ưa','ừa','ứa','ựa','ửa','ữa','ưà','ưá','ưạ','ưả','ưã']
diph_ươ = ['ươ','ừơ','ứơ','ựơ','ửơ','ữơ','ườ','ướ','ượ','ưở','ưỡ']
diph_ia = ['ia','ìa','ía','ịa','ỉa','ĩa','ià','iá','iạ','iả','iã']  # 'yà','yá','yã','yả','ya','ỳa','ýa','ỵa','ỷa','ỹa','yạ'
diph_iê = ['iê','ìê','íê','ịê','ỉê','ĩê','iề','iế','iệ','iể','iễ','yề','yể','yệ','yế','yê','ỳê','ýê','ỵê','ỷê','ỹê','yễ']
diph_ua = ['ua','ùa','úa','ụa','ủa','ũa','uà','uá','uạ','uả','uã']
diph_uô = ['uô','ùô','úô','ụô','ủô','ũô','uồ','uố','uộ','uổ','uỗ']

diph_ay = ['ay','aỳ','aý','aỵ','aỷ','aỹ','ày','áy','ạy','ảy','ãy']
diph_au = ['au','aù','aú','aụ','aủ','aũ','àu','áu','ạu','ảu','ãu']
diph_ây = ['ây','âỳ','âý','âỵ','âỷ','âỹ','ầy','ấy','ậy','ẩy','ẫy']

diph_oă = ['oă','oằ','oắ','oặ','oẳ','oẵ','òă','óă','ọă','ỏă','õă']  # (q)uă
diph_oa = ['oa','oà','oá','oạ','oả','oã','òa','óa','ọa','ỏa','õa']  # (q)ua
diph_oe = ['oe','oè','oé','oẹ','oẻ','oẽ','òe','óe','ọe','ỏe','õe']  # (q)ue
diph_uâ = ['uâ','uầ','uấ','uậ','uẩ','uẫ','ùâ','úâ','ụâ','ủâ','ũâ']  # (q)uâ
diph_uơ = ['uơ','uờ','uớ','uợ','uở','uỡ','ùơ','úơ','ụơ','ủơ','ũơ']  # (q)uơ /wə/
diph_uê = ['uê','uề','uế','uệ','uể','uễ','ùê','úê','ụê','ủê','ũê']  # (q)uê /we/
diph_uy = ['uy','uỳ','uý','uỵ','uỷ','uỹ','ùy','úy','ụy','ủy','ũy']  # (q)uy /wi/
diph_ơi = ['ơi','ơì','ơí','ơị','ơỉ','ơĩ','ời','ới','ợi','ởi','ỡi','ờy','ởy','ợy','ớy','ơy','ơỳ','ơý','ơỵ','ơỷ','ơỹ','ỡy']
diph_uyê = ['uyê','uyề','uyế','uyệ','uyể','uyễ','uỳê','uýê','uỵê','uỷê','uỹê','ùyê','úyê','ụyê','ủyê','ũyê']  # (q)uyê /wiə/
diph_uya = ['uya','uyà','uyá','uyạ','uyả','uyã','uỳa','uýa','uỵa','uỷa','uỹa','ùya','úya','ụya','ủya','ũya']  # (q)uya /wiə/
diph_oay = ['oay','òay','óay','ọay','ỏay','õay','oày','oáy','oạy','oảy','oãy','oaỳ','oaý','oaỵ','oaỷ','oaỹ']  # (q)uyê /wiə/
diph_uây = ['uây','ùây','úây','ụây','ủây','ũây','uầy','uấy','uậy','uẩy','uẫy','uâỳ','uâý','uâỵ','uâỷ','uâỹ']  # (q)uya /wiə/

b_tones = 'áắấíóớúứýéếốạặậịọợụựỵẹệộ'
c_tones = 'ảẳẩỉỏởủửỷẻểổãẵẫĩõỡũữỹẽễỗ'
high_vowels = 'aăâioơuưyeêôáắấíóớúứýéếốảẳẩỉỏởủửỷẻểổ'
low_vowels = 'àằầìòờùừỳèềồạặậịọợụựỵẹệộãẵẫĩõỡũữỹẽễỗ'

vowels = low_vowels + high_vowels
consonants = 'bcdđfghjklmnpqrstvwxz'
letters = consonants + vowels

vowel_mappings = {}

for char in vowel_e:
    vowel_mappings[char] = ('แ', '', '')
for char in vowel_ê:
    vowel_mappings[char] = ('เ', '', '')
for char in vowel_ơ:
    vowel_mappings[char] = ('เ', 'ิ', '')
for char in vowel_ô:
    vowel_mappings[char] = ('โ', '', '')
for char in vowel_o:
    vowel_mappings[char] = ('', '', '')
for char in vowel_a:
    vowel_mappings[char] = ('', '', 'า')
for char in vowel_ă:
    vowel_mappings[char] = ('', 'ั', '')
for char in vowel_â:
    vowel_mappings[char] = ('', 'ึ', '')
for char in vowel_i:
    vowel_mappings[char] = ('', 'ิ', '')
for char in vowel_ư:
    vowel_mappings[char] = ('', 'ื', '')
for char in vowel_u:
    vowel_mappings[char] = ('', 'ุ', '')

for char in diph_ươ:
    vowel_mappings[char] = ('เ', 'ื', 'อ')
for char in diph_ưa:
    vowel_mappings[char] = ('เ', 'ื', 'อ')
for char in diph_iê:
    vowel_mappings[char] = ('เ', 'ี', 'ย')
for char in diph_ia:
    vowel_mappings[char] = ('เ', 'ี', 'ย')
for char in diph_uô:
    vowel_mappings[char] = ('', 'ั', 'ว')
for char in diph_ua:
    vowel_mappings[char] = ('', 'ั', 'ว')

for char in diph_ay:
    vowel_mappings[char] = ('', 'ั', 'า')
for char in diph_au:
    vowel_mappings[char] = ('เ', '', 'า')
for char in diph_ây:
    vowel_mappings[char] = ('', 'ึ', 'ย')

for char in diph_oă:
    vowel_mappings[char] = ('', 'วั', '')
for char in diph_oa:
    vowel_mappings[char] = ('', 'ว', 'า')
for char in diph_oe:
    vowel_mappings[char] = ('แ', 'ว', '')
for char in diph_uâ:
    vowel_mappings[char] = ('', 'วึ', '')
for char in diph_uơ:
    vowel_mappings[char] = ('เ', 'วิ', '')
for char in diph_uê:
    vowel_mappings[char] = ('เ', 'ว', '')
for char in diph_uy:
    vowel_mappings[char] = ('', 'วิ', '')
for char in diph_ơi:
    vowel_mappings[char] = ('เ', '', 'ย')
for char in diph_uyê:
    vowel_mappings[char] = ('เ', 'วี', 'ย')
for char in diph_uya:
    vowel_mappings[char] = ('เ', 'วี', 'ย')
for char in diph_oay:
    vowel_mappings[char] = ('', 'วั', 'ย')
for char in diph_uây:
    vowel_mappings[char] = ('', 'วึ', 'ย')

consonant_mappings = {
    'm': ('ม', 'หม'),
    'n': ('น', 'หน'),
    'nh': ('ญ', 'หญ'),
    'ng': ('ง', 'หง'),
    'ngh': ('ง', 'หง'),

    'b': ('พ', 'บ'),
    'đ': ('ฑ', 'ฎ'),
    'p': ('ภ', 'ป'),
    't': ('ท', 'ด'),
    'th': ('ธ', 'ถ'),
    'tr': ('ฒ', 'ฐ'),
    'ch': ('ช', 'จ'),
    'c': ('ค', 'ก'),
    'k': ('ค', 'ก'),
    'q': ('ค', 'ก'),
    'qu': ('คว', 'กว'),

    'f': ('ฟ', 'ผ'),
    'ph': ('ฟ', 'ผ'),
    'x': ('ฌ', 'ฉ'),
    's': ('ซ', 'ส'),
    'kh': ('ฆ', 'ข'),
    'h': ('ฮ', 'ห'),

    'v': ('ว', 'หว'),
    'w': ('ว', 'หว'),
    'gi': ('ย', 'หย'),
    'j': ('ย', 'หย'),
    'z': ('ย', 'หย'),
    'd': ('ย', 'หย'),
    'g': ('ฅ', 'ฃ'),
    'gh': ('ฅ', 'ฃ'),
    'l': ('ล', 'หล'),
    'r': ('ร', 'หร'),
}

# Define the det_vowel_class function
def det_vowel_class(consonant, following_vowel):
    consonant_series = consonant_mappings
    consonant_series_index = None
    for i, series in enumerate(consonant_series):
        if consonant in series:
            consonant_series_index = i
            break
    following_vowels = individual_strings = [char for char in following_vowel]
    if consonant_series_index is not None:
        if any(vowel in low_vowels for vowel in following_vowels):
            return 0
        else:
            return 1

    return None

# Define the viet_to_thai function
def viet_to_thai(input_text):
    input_text = input_text.lower()
    result = ''
    i = 0
    while i < len(input_text):
        char = input_text[i]
        if char == ' ':
            result += ' '
            i += 1
            continue
        for length in range(3, 0, -1):
            substring = input_text[i : i + length]
            if substring in consonant_mappings:
                triph_substring = input_text[i + length : i + length + 3]
                diph_substring = input_text[i + length : i + length + 2]
                vowel_substring = input_text[i + length : i + length + 1]
                max_vowel_length = 3  # Adjust this value as needed
                for v_length in range(max_vowel_length, 0, -1):
                    if i < len(input_text) - length - v_length and triph_substring in vowel_mappings:
                        vowel_class = det_vowel_class(substring, triph_substring)
                        result += vowel_mappings[triph_substring][0] + consonant_mappings[substring][vowel_class] + vowel_mappings[triph_substring][1]
                        if triph_substring in c_tones:
                            result += '้'
                        elif triph_substring not in b_tones or triph_substring in b_tones and i + length < len(input_text) and (input_text[i + length + 1] in 'pbtđckqg'):
                            result += ''
                        else:
                            result += '่'
                        result += vowel_mappings[triph_substring][2]
                        i += length + 2
                        break
                    elif i < len(input_text) - length - v_length and diph_substring in vowel_mappings:
                        vowel_class = det_vowel_class(substring, diph_substring)
                        result += vowel_mappings[diph_substring][0] + consonant_mappings[substring][vowel_class] + vowel_mappings[diph_substring][1]
                        if diph_substring in c_tones:
                            result += '้'
                        elif diph_substring not in b_tones or diph_substring in b_tones and i + length < len(input_text) and (input_text[i + length + 1] in 'pbtđckqg'):
                            result += ''
                        else:
                            result += '่'
                        result += vowel_mappings[diph_substring][2]
                        i += length + 1
                        break
                    elif i < len(input_text) - length - v_length and vowel_substring in vowel_mappings:
                        vowel_class = det_vowel_class(substring, vowel_substring)
                        result += vowel_mappings[vowel_substring][0] + consonant_mappings[substring][vowel_class] + vowel_mappings[vowel_substring][1]
                        if vowel_substring in c_tones:
                            result += '้'
                        elif vowel_substring not in b_tones or vowel_substring in b_tones and i + length < len(input_text) and (input_text[i + length + 1] in 'pbtđckqg'):
                            result += ''
                        else:
                            result += '่'
                        result += vowel_mappings[vowel_substring][2]
                        i += length
                        break

                    else:
                        if substring in ['d', 'gi', 'j', 'l', 'm', 'n', 'ng', 'nh', 'r', 'v', 'w', 'z']:
                            result += consonant_mappings[substring][0] + ' '
                            i += length
                            break
                        elif substring == 'p':
                            result += consonant_mappings['b'][1]
                        elif substring in consonant_mappings:
                            result += consonant_mappings[substring][1]
                        i += length - 1
                        break

            elif substring in vowel_mappings and input_text[i - length] not in vowel_mappings:
                if i > 0 and input_text[i - 1] not in consonant_mappings:
                    result += vowel_mappings[substring][0] + 'อ' + vowel_mappings[substring][1] + vowel_mappings[substring][2]
                else:
                    result += ''

        else:
            if char in 'ou':
                if i > 0 and input_text[i - 1] in vowel_mappings:
                    result += 'ว'
                else:
                    result += char
                    break
            elif char in 'iy':
                if i > 0 and input_text[i - 1] in vowel_mappings:
                    result += 'ย'
                else:
                    result += char
                    break
        i += 1
    return result

# Create a Tkinter application
root = tk.Tk()
root.title("Vietnamese to Thai Transcription Tool")
root.geometry("700x800")
root.config(bg='#313338')

# Create the input entry and result text widgets
input_entry = tk.Text(root, height=8, width=48, font=('Noto Serif Light', 20))
result_text = tk.Text(root, height=8, width=48, font=('Noto Serif Thai Light', 23))

# Implement the orthographic options as a set of radio buttons
ortho_frame = tk.Frame(root, bg='#313338')
radio_buttons = {}

# Define the function to create radio buttons
def create_radio_button(frame, text, variable, value, command):
    button = tk.Radiobutton(frame,
        text=text,
        variable=variable,
        value=value,
        command=command,
        bd=4,
        bg='#313338',
        fg='#EAEAEB',
        padx=8,
        pady=4,
        selectcolor='#313338',
        indicatoron=False,
        offrelief='raised',
        activebackground='#313338',
        activeforeground='#EAEAEB',
        highlightbackground='#313338',
        highlightthickness=4)
    return button

# Define orthographic options as a list
orthographic_options = [
    ("i", "◌ิ", "i curto", "i_transcription"),
    ("i", "◌ี", "i longo", "i_transcription"),
    ("u", "◌ุ", "u curto", "u_transcription"),
    ("u", "◌ู", "u longo", "u_transcription"),
    ("ư", "◌ึ", "ư longo", "ư_transcription"),
    ("ư", "◌ื", "ư curto", "ư_transcription"),
    ("â", "◌ึ", "â curto", "â_transcription"),
    ("â", "เ◌ิ", "â longo", "â_transcription"),
    ("ơ", "เ◌ิ", "ơ curto", "ơ_transcription"),
    ("ơ", "เ◌อ", "ơ longo", "ơ_transcription"),
    ("o", "◌", "o curto", "o_transcription"),
    ("o", "◌อ", "o longo", "o_transcription"),
    ("ay", "◌ัย", "ay curto", "ay_transcription"),
    ("ay", "ไ◌", "ay longo", "ay_transcription"),
    ("ây", "◌ึย", "ây curto", "ây_transcription"),
    ("ây", "ใ◌", "ây longo", "ây_transcription"),
]

# Loop through the orthographic options and create radio buttons
for i, (base, diacritic, value, callback) in enumerate(orthographic_options):
    text = f"{base} → {diacritic}"
    variable = tk.StringVar()
    variable.set(value)
    button = create_radio_button(ortho_frame, text, variable, value, lambda callback=callback: on_text_modified(callback))
    button.grid(column=i // 2, row=i % 2)
    radio_buttons[value] = button

# Implement the on_text_modified function
def on_text_modified(callback):
    input_text = input_entry.get("1.0", tk.END)
    result_text.delete(1.0, tk.END)
    result = viet_to_thai(input_text)
    result_text.insert(tk.END, result)
    root.update()

# Bind the on_text_modified function to KeyRelease event
input_entry.bind("<KeyRelease>", lambda event=None: on_text_modified(None))

# Pack widgets and start the application
input_entry.pack(expand=True)
ortho_frame.pack()
result_text.pack(expand=True)

root.mainloop()