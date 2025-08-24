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
vowel_y = 'yỳýỵỷỹ'

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
    vowel_mappings[char] = ('เ', '', 'อ')
for char in vowel_ô:
    vowel_mappings[char] = ('โ', '', '')
for char in vowel_o:
    vowel_mappings[char] = ('', '', 'อ')
for char in vowel_a:
    vowel_mappings[char] = ('', '', 'า')
for char in vowel_ă:
    vowel_mappings[char] = ('', '', '') # ('', 'ั', '')
for char in vowel_â:
    vowel_mappings[char] = ('เ', 'ี', '') # 'ิ'
for char in vowel_i:
    vowel_mappings[char] = ('', 'ี', '') # 'ิ'
for char in vowel_ư:
    vowel_mappings[char] = ('', 'ื', '')
for char in vowel_u:
    vowel_mappings[char] = ('', 'ุ', '') # 'ู'

for char in diph_ươ:
    vowel_mappings[char] = ('เ', 'ื', 'อ')
for char in diph_ưa:
    vowel_mappings[char] = ('เ', 'ื', 'อ')
for char in diph_iê:
    vowel_mappings[char] = ('เ', 'ี', 'ย')
for char in diph_ia:
    vowel_mappings[char] = ('เ', 'ี', 'ย')
for char in diph_uô:
    vowel_mappings[char] = ('', '', 'ว') # ('', 'ั', 'ว')
for char in diph_ua:
    vowel_mappings[char] = ('', 'ั', 'ว')

for char in diph_ay:
    vowel_mappings[char] = ('', '', 'ย') # ('', 'ั', 'ย')
for char in diph_au:
    vowel_mappings[char] = ('เ', '', 'า')
for char in diph_ây:
    vowel_mappings[char] = ('เ', 'ี', 'ย') # ('', 'ึ', 'ย')

for char in diph_oă:
    vowel_mappings[char] = ('', 'ว', '') # ('', 'วั', '')
for char in diph_oa:
    vowel_mappings[char] = ('', 'ว', 'า')
for char in diph_oe:
    vowel_mappings[char] = ('แ', 'ว', '')
for char in diph_uâ:
    vowel_mappings[char] = ('เ', 'วี', '') # ('', 'วึ', '') # 'วิ'
for char in diph_uơ:
    vowel_mappings[char] = ('เ', 'ว', 'อ')
for char in diph_uê:
    vowel_mappings[char] = ('เ', 'ว', '')
for char in diph_uy:
    vowel_mappings[char] = ('', 'วี', '') # 'วิ'
for char in diph_ơi:
    vowel_mappings[char] = ('เ', '', 'ย')
for char in diph_uyê:
    vowel_mappings[char] = ('เ', 'วี', 'ย')
for char in diph_uya:
    vowel_mappings[char] = ('เ', 'วี', 'ย')
for char in diph_oay:
    vowel_mappings[char] = ('', 'ว', 'ย') # ('', 'วั', 'ย')
for char in diph_uây:
    vowel_mappings[char] = ('เ', 'วี', 'ย') # ('', 'วึ', 'ย')

consonant_mappings = {
    'm': ('ม', 'หม'),
    'n': ('น', 'หน'),
    'nh': ('ญ', 'หญ'),
    'ng': ('ง', 'หง'),
    'ngh': ('ง', 'หง'),

    'b': ('พ', 'บ'), # !
    'đ': ('ฑ', 'ฎ'),
    'p': ('ภ', 'ป'), # !
    't': ('ท', 'ด'),
    'th': ('ธ', 'ถ'),
    'tr': ('ฒ', 'ฐ'),
    'ch': ('ช', 'จ'),
    'c': ('ค', 'ก'),
    'k': ('ค', 'ก'),
    'q': ('ค', 'ก'),
    'qu': ('คว', 'กว'),

    'f': ('ฟ', 'ผ'), # !
    'ph': ('ฟ', 'ผ'), # !
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
    input_text = '   ' + input_text.lower() + '   '
    result = ''
    i = 0
    while i < len(input_text):
        char = input_text[i]
        if char in ' ,.:;?!':
            result += char
            i += 1
            continue
        for length in [3, 2, 1]:
            substring = input_text[i : i + length]
            if substring in consonant_mappings:
                triph_substring = input_text[i + length : i + length + 3]
                diph_substring = input_text[i + length : i + length + 2]
                vowel_substring = input_text[i + length : i + length + 1]
                for v_length in [3, 2, 1]:
                    if i < len(input_text) - length - v_length and triph_substring in vowel_mappings:
                        vowel_class = det_vowel_class(substring, triph_substring)
                        result += vowel_mappings[triph_substring][0] + consonant_mappings[substring][vowel_class] + vowel_mappings[triph_substring][1]
                        if any(vowel in c_tones for vowel in triph_substring):
                            result += '้'
                        elif any(vowel in b_tones for vowel in triph_substring) and i + length < len(input_text) and (input_text[i + length + 3] in 'pbtđckqg'):
                            result += ''
                        elif any(vowel in b_tones for vowel in triph_substring):
                            result += '่'
                        else:
                            result += ''
                        result += vowel_mappings[triph_substring][2]
                        i += length + 2
                        break
                    elif i < len(input_text) - length - v_length and diph_substring in vowel_mappings:
                        vowel_class = det_vowel_class(substring, diph_substring)
                        result += vowel_mappings[diph_substring][0] + consonant_mappings[substring][vowel_class] + vowel_mappings[diph_substring][1]
                        if any(vowel in c_tones for vowel in diph_substring):
                            result += '้'
                        elif any(vowel in b_tones for vowel in diph_substring) and i + length < len(input_text) and (input_text[i + length + 2] in 'pbtđckqg'):
                            result += ''
                        elif any(vowel in b_tones for vowel in diph_substring):
                            result += '่'
                        else:
                            result += ''
                        result += vowel_mappings[diph_substring][2]
                        i += length + 1
                        break
                    elif i < len(input_text) - length - v_length and vowel_substring in vowel_mappings:
                        vowel_class = det_vowel_class(substring, vowel_substring)
                        result += vowel_mappings[vowel_substring][0] + consonant_mappings[substring][vowel_class] + vowel_mappings[vowel_substring][1]
                        if vowel_substring in c_tones:
                            result += '้'
                        elif vowel_substring in b_tones and i + length < len(input_text) and (input_text[i + length + 1] in 'pbtđckqg'):
                            result += ''
                        elif vowel_substring in b_tones:
                            result += '่'
                        else:
                            result += ''
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

            # elif substring in vowel_mappings and input_text[i - length] not in vowel_mappings:
            #     # if i > 0 and input_text[i - 1] not in consonant_mappings:
            #         # if len(substring) == 3:
            #         result += vowel_mappings[substring][0] + 'อ' + vowel_mappings[substring][1]
            #         if any(vowel in c_tones for vowel in substring):
            #             result += '้'
            #         elif any(vowel in b_tones for vowel in substring) and i + length < len(input_text) and (input_text[i + length + 1] in 'pbtđckqg'):
            #             result += ''
            #         elif any(vowel in b_tones for vowel in substring):
            #             result += '่'
            #         result += vowel_mappings[substring][2]
            #         if substring in ['d', 'gi', 'j', 'l', 'm', 'n', 'ng', 'nh', 'r', 'v', 'w', 'z']:
            #             result += consonant_mappings[substring][0] + ' '
            #             i += length
            #             break
            #         elif substring == 'p':
            #             result += consonant_mappings['b'][1]
            #         elif substring in consonant_mappings:
            #             result += consonant_mappings[substring][1]
            #         i += length - 1
            #         break
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
    return result.strip()

# Define available orthographic options
orthographic_settings = {
    "i_transcription":  "◌ิ",  # or "◌ี"
    "u_transcription":  "◌ุ",  # or "◌ู"
    "ư_transcription":  "◌ึ",  # or "◌ื"
    "â_transcription":  "เ◌ิ",  # or "◌ึ"
    "ơ_transcription":  "เ◌อ", # or "เ◌ิ"
    "o_transcription":  "◌",  # or "◌อ"
    "ay_transcription": "◌ัย", # or "ไ◌"
    "ây_transcription": "◌ึย", # or "ใ◌"
}

if __name__ == "__main__":
    print("Thai for Vietnamese Transcriber")
    print("Type Vietnamese text below, then hit Enter to convert it to Thai.\n")

    while True:
        input_text = input()# "Input (Vietnamese): "
        result = viet_to_thai(input_text)
        print(result) # "Output (Thai):", 