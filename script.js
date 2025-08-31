// Create arrays for vowel mappings
const vowel_a  = ['a','à','á','ạ','ả','ã'];
const vowel_ă  = ['ă','ằ','ắ','ặ','ẳ','ẵ'];
const vowel_â  = ['â','ầ','ấ','ậ','ẩ','ẫ'];
const vowel_e  = ['e','è','é','ẹ','ẻ','ẽ'];
const vowel_ê  = ['ê','ề','ế','ệ','ể','ễ'];
const vowel_i  = ['i','ì','í','ị','ỉ','ĩ','y','ỳ','ý','ỵ','ỷ','ỹ'];
const vowel_o  = ['o','ò','ó','ọ','ỏ','õ'];
const vowel_ô  = ['ô','ồ','ố','ộ','ổ','ỗ'];
const vowel_ơ  = ['ơ','ờ','ớ','ợ','ở','ỡ'];
const vowel_u  = ['u','ù','ú','ụ','ủ','ũ'];
const vowel_ư  = ['ư','ừ','ứ','ự','ử','ữ'];
const vowel_y  = ['y','ỳ','ý','ỵ','ỷ','ỹ'];

const diph_ưa  = ['ưa','ừa','ứa','ựa','ửa','ữa','ưà','ưá','ưạ','ưả','ưã'];
const diph_ươ  = ['ươ','ừơ','ứơ','ựơ','ửơ','ữơ','ườ','ướ','ượ','ưở','ưỡ'];
const diph_ia  = ['ia','ìa','ía','ịa','ỉa','ĩa','ià','iá','iạ','iả','iã','yà','yá','yã','yả','ya','ỳa','ýa','ỵa','ỷa','ỹa','yạ'];
const diph_iê  = ['iê','ìê','íê','ịê','ỉê','ĩê','iề','iế','iệ','iể','iễ','yề','yể','yệ','yế','yê','ỳê','ýê','ỵê','ỷê','ỹê','yễ'];
const diph_ua  = ['ua','ùa','úa','ụa','ủa','ũa','uà','uá','uạ','uả','uã'];
const diph_uô  = ['uô','ùô','úô','ụô','ủô','ũô','uồ','uố','uộ','uổ','uỗ'];

const diph_ay  = ['ay','aỳ','aý','aỵ','aỷ','aỹ','ày','áy','ạy','ảy','ãy'];
const diph_au  = ['au','aù','aú','aụ','aủ','aũ','àu','áu','ạu','ảu','ãu'];
const diph_ây  = ['ây','âỳ','âý','âỵ','âỷ','âỹ','ầy','ấy','ậy','ẩy','ẫy'];

const diph_oe  = ['oe','oè','oé','oẹ','oẻ','oẽ','òe','óe','ọe','ỏe','õe','ue','uè','ué','uẹ','uẻ','uẽ','ùe','úe','ụe','ủe','ũe'];  // oe, (q)ue /wɛ/
const diph_uê  = ['uê','uề','uế','uệ','uể','uễ','ùê','úê','ụê','ủê','ũê'];  // (q)uê /we/
const diph_uy  = ['uy','uỳ','uý','uỵ','uỷ','uỹ','ùy','úy','ụy','ủy','ũy'];  // (q)uy /wi/
const diph_uyê = ['uyê','uyề','uyế','uyệ','uyể','uyễ','uỳê','uýê','uỵê','uỷê','uỹê','ùyê','úyê','ụyê','ủyê','ũyê'];  // (q)uyê /wiə/
const diph_uya = ['uya','uyà','uyá','uyạ','uyả','uyã','uỳa','uýa','uỵa','uỷa','uỹa','ùya','úya','ụya','ủya','ũya'];  // (q)uya /wiə/
const diph_oa  = ['oa','oà','oá','oạ','oả','oã','òa','óa','ọa','ỏa','õa','ua','uà','uá','uạ','uả','uã','ùa','úa','ụa','ủa','ũa'];  // oa, (q)ua /wa:/
const diph_oă  = ['oă','oằ','oắ','oặ','oẳ','oẵ','òă','óă','ọă','ỏă','õă','uă','uằ','uắ','uặ','uẳ','uẵ','ùă','úă','ụă','ủă','ũă'];  // oă, (q)uă /wa/
const diph_uâ  = ['uâ','uầ','uấ','uậ','uẩ','uẫ','ùâ','úâ','ụâ','ủâ','ũâ'];  // (q)uâ /wə/
const diph_uơ  = ['uơ','uờ','uớ','uợ','uở','uỡ','ùơ','úơ','ụơ','ủơ','ũơ'];  // (q)uơ /wə:/

const diph_ơi  = ['ơi','ơì','ơí','ơị','ơỉ','ơĩ','ời','ới','ợi','ởi','ỡi','ờy','ởy','ợy','ớy','ơy','ơỳ','ơý','ơỵ','ơỷ','ơỹ','ỡy'];
const diph_oay = ['oay','òay','óay','ọay','ỏay','õay','oày','oáy','oạy','oảy','oãy','oaỳ','oaý','oaỵ','oaỷ','oaỹ'];
const diph_uây = ['uây','ùây','úây','ụây','ủây','ũây','uầy','uấy','uậy','uẩy','uẫy','uâỳ','uâý','uâỵ','uâỷ','uâỹ'];

const b_tones = 'áắấíóớúứýéếốạặậịọợụựỵẹệộ';
const c_tones = 'ảẳẩỉỏởủửỷẻểổãẵẫĩõỡũữỹẽễỗ';
const high_vowels = 'aăâioơuưyeêôáắấíóớúứýéếốảẳẩỉỏởủửỷẻểổ';
const low_vowels  = 'àằầìòờùừỳèềồạặậịọợụựỵẹệộãẵẫĩõỡũữỹẽễỗ';

const vowels = low_vowels + high_vowels;
const consonants = 'bcdđfghjklmnpqrstvwxz';
const letters = consonants + vowels;

// Initialize an empty object for vowel mappings
const vowel_mappings = {};

// Populate vowel_mappings using loops
for (const char of vowel_e) {
    vowel_mappings[char] = ['แ', '', ''];
}
for (const char of vowel_ê) {
    vowel_mappings[char] = ['เ', '', ''];
}
for (const char of vowel_ơ) {
    vowel_mappings[char] = ['เ', '', 'อ']; // เ◌อ
}
for (const char of vowel_ô) {
    vowel_mappings[char] = ['โ', '', ''];
}
for (const char of vowel_o) {
    vowel_mappings[char] = ['', '', 'อ'];
}
for (const char of vowel_a) {
    vowel_mappings[char] = ['', '', 'า']; // only one option: า
}
for (const char of vowel_ă) {
    vowel_mappings[char] = ['', 'ั', '']; // ◌ั or ◌ะ or nothing
}
for (const char of vowel_â) {
    vowel_mappings[char] = ['เ', 'ิ', '']; // เ◌ี or เ◌ิ
}
for (const char of vowel_i) {
    vowel_mappings[char] = ['', 'ี', '']; // ◌ี or ◌ิ
}
for (const char of vowel_ư) {
    vowel_mappings[char] = ['', 'ื', '']; // ◌ื or ◌ึ
}
for (const char of vowel_u) {
    vowel_mappings[char] = ['', 'ุ', '']; // ◌ุ or ◌ู
}

// Diphthongs
for (const char of diph_ươ) {
    vowel_mappings[char] = ['เ', 'ื', 'อ']; // เ◌ือ
}
for (const char of diph_ưa) {
    vowel_mappings[char] = ['เ', 'ื', 'อ']; // เ◌ือ
}
for (const char of diph_iê) {
    vowel_mappings[char] = ['เ', 'ี', 'ย']; // เ◌ีย
}
for (const char of diph_ia) {
    vowel_mappings[char] = ['เ', 'ี', 'ย']; // เ◌ีย
}
for (const char of diph_uô) {
    vowel_mappings[char] = ['', 'ั', 'ว']; // ◌ัว or ◌ว
}
for (const char of diph_ua) {
    vowel_mappings[char] = ['', 'ั', 'ว']; // ◌ัว or ◌ว
}

for (const char of diph_ay) {
    vowel_mappings[char] = ['ไ', '', '']; // ไ◌ or ◌ัย
}
for (const char of diph_au) {// /a:w/ <ao> = ◌าว
    vowel_mappings[char] = ['เ', '', 'า']; // เ◌า
}
for (const char of diph_ây) {
    vowel_mappings[char] = ['ใ', '', '']; // ใ◌ or เ◌ิย
}
for (const char of diph_ơi) {
    vowel_mappings[char] = ['เ', '', 'ย']; // เ◌ย
}

// /W/ ON-GLIDES
for (const char of diph_oe) { // /wɛ/ <oe/(q)ue*>
    vowel_mappings[char] = ['แ', 'ว', '']; // แ◌ว◌?
}
for (const char of diph_uê) {// /we/ <uê>
    vowel_mappings[char] = ['เ', 'ว', '']; // เ◌ว◌?
}
for (const char of diph_uy) {// /wi/ <uy>
    vowel_mappings[char] = ['', 'วี', '']; // ◌วี◌?
}
for (const char of diph_uyê) {// /wiə̯/ <uyê>
    vowel_mappings[char] = ['เ', 'วี', 'ย']; // เ◌วีย?
}
for (const char of diph_uya) {// /wiə̯/ <uya>
    vowel_mappings[char] = ['เ', 'วี', 'ย']; // เ◌วีย?
}
for (const char of diph_oa) {// /wa:/ <oa/(q)ua>
    vowel_mappings[char] = ['', 'ว', 'า']; // ◌วา◌?
}
for (const char of diph_oă) {// /wa/ <oă/(q)uă>
    vowel_mappings[char] = ['', 'วั', '']; // ◌ัว◌ or ◌ว◌
}
for (const char of diph_uâ) {// /wə/ <uâ>
    vowel_mappings[char] = ['เ', 'วี', '']; // เ◌ีว◌?
}
for (const char of diph_uơ) {// /wə:/ <uơ>
    vowel_mappings[char] = ['เ', 'ว', 'อ']; // เ◌ีวอ◌?
}

// /wiw/ <uyu>

// /wɛw/ <oeo/(q)ueo>

// for (const char of diph_oai) {// /wa:j/ <oai, (q)uai>
//     vowel_mappings[char] = ['', 'ว', 'าย']; // ?
// }

// for (const char of diph_oao) {// /wa:w/ <oao/(q)uao>
//     vowel_mappings[char] = ['', 'ว', 'าว']; // ?
// }

for (const char of diph_oay) {// /waj/ <oay/(q)uay>
    vowel_mappings[char] = ['', 'วั', 'ย']; // ◌ัวย
}
for (const char of diph_uây) {// /wə̆j/ <uây>
    vowel_mappings[char] = ['เ', 'วี', 'ย']; // เ◌ีวย?
}

// Consonants
const consonant_mappings = {
    'm': ['ม', 'หม'],
    'n': ['น', 'หน'],
    'nh': ['ญ', 'หญ'],
    'ng': ['ง', 'หง'],
    'ngh': ['ง', 'หง'],

    'b': ['พ', 'บ'], // !
    'đ': ['ฑ', 'ฎ'],
    'p': ['ภ', 'ป'], // !
    't': ['ท', 'ด'],
    'th': ['ธ', 'ถ'],
    'tr': ['ฒ', 'ฐ'],
    'ch': ['ช', 'จ'],
    'c': ['ค', 'ก'],
    'k': ['ค', 'ก'],
    'q': ['ค', 'ก'],
    'qu': ['คว', 'กว'],

    'f': ['ฟ', 'ผ'], // !
    'ph': ['ฟ', 'ผ'], // !
    'x': ['ฌ', 'ฉ'],
    's': ['ซ', 'ส'],
    'kh': ['ฆ', 'ข'],
    'h': ['ฮ', 'ห'],

    'v': ['ว', 'หว'],
    'w': ['ว', 'หว'],
    'gi': ['ย', 'หย'],
    'j': ['ย', 'หย'],
    'z': ['ย', 'หย'],
    'd': ['ย', 'หย'],
    'g': ['ฅ', 'ฃ'],
    'gh': ['ฅ', 'ฃ'],
    'l': ['ล', 'หล'],
    'r': ['ร', 'หร'],
};

function transcribe() {
    // Get input text
    let inputText = document.getElementById("input").value.trim();

    // Call your viet_to_thai function
    let result = viet_to_thai(inputText);

    // Output result
    document.getElementById("output").value = result;
}

function det_register(consonant, following_vowel) {
    if (!(consonant in consonant_mappings)) {
        return null; // consonant not found
    }

    const following_vowels = Array.from(following_vowel); // split into characters

    if (following_vowels.some(vowel => low_vowels.includes(vowel))) {
        return 0; // low vowel → choose low consonant
    } else {
        return 1; // high vowel → choose high consonant
    }
}

function viet_to_thai(input_text) {
    input_text = '   ' + input_text.toLowerCase() + '   ';
    let result = '';
    let i = 0;

    while (i < input_text.length) {
        let char = input_text[i];

        if (' ,.:;?\"01234567890!@#$%&*()_+=[]{}/<>\\¿€®©§\t\n\r'.includes(char)) {
            result += char;
            i++;
            continue;
        } else if ('\''.includes(char)) {
            result += '์';
            i++;
            continue;
        }

        let matched = false;
        let matchedLength = 1; // default increment if nothing matches

        for (const length of [3, 2, 1]) {
            let substring = input_text.slice(i, i + length);

            if (consonant_mappings.hasOwnProperty(substring)) {
                let triph_substring = input_text.slice(i + length, i + length + 3);
                let diph_substring = input_text.slice(i + length, i + length + 2);
                let vowel_substring = input_text.slice(i + length, i + length + 1);

                for (const v_length of [3, 2, 1]) {
                    if ((i < input_text.length - length - v_length) && vowel_mappings.hasOwnProperty(triph_substring)) {
                        let register = det_register(substring, triph_substring);
                        result += vowel_mappings[triph_substring][0] + consonant_mappings[substring][register] + vowel_mappings[triph_substring][1];

                        if ([...triph_substring].some(v => c_tones.includes(v))) {
                            result += '้';
                        } else if ([...triph_substring].some(v => b_tones.includes(v)) && (i + length < input_text.length) && 'pbtđckqg'.includes(input_text[i + length + 3])) {
                            result += '';
                        } else if ([...triph_substring].some(v => b_tones.includes(v))) {
                            result += '่';
                        }
                        result += vowel_mappings[triph_substring][2];
                        matchedLength = length + 3;
                        matched = true;
                        break;

                    } else if ((i < input_text.length - length - v_length) && vowel_mappings.hasOwnProperty(diph_substring)) {
                        let register = det_register(substring, diph_substring);
                        result += vowel_mappings[diph_substring][0] + consonant_mappings[substring][register] + vowel_mappings[diph_substring][1];

                        if ([...diph_substring].some(v => c_tones.includes(v))) {
                            result += '้';
                        } else if ([...diph_substring].some(v => b_tones.includes(v)) && (i + length < input_text.length) && 'pbtđckqg'.includes(input_text[i + length + 2])) {
                            result += '';
                        } else if ([...diph_substring].some(v => b_tones.includes(v))) {
                            result += '่';
                        }
                        result += vowel_mappings[diph_substring][2];
                        matchedLength = length + 2;
                        matched = true;
                        break;

                    } else if ((i < input_text.length - length - v_length) && vowel_mappings.hasOwnProperty(vowel_substring)) {
                        let register = det_register(substring, vowel_substring);
                        result += vowel_mappings[vowel_substring][0] + consonant_mappings[substring][register] + vowel_mappings[vowel_substring][1];

                        if (c_tones.includes(vowel_substring)) {
                            result += '้';
                        } else if (b_tones.includes(vowel_substring) && (i + length < input_text.length) && 'pbtđckqg'.includes(input_text[i + length + 1])) {
                            result += '';
                        } else if (b_tones.includes(vowel_substring)) {
                            result += '่';
                        }
                        result += vowel_mappings[vowel_substring][2];
                        matchedLength = length + 1;
                        matched = true;
                        break;

                    } else {
                        if (['d', 'gi', 'j', 'l', 'm', 'n', 'ng', 'nh', 'r', 'v', 'w', 'z'].includes(substring)) {
                            result += consonant_mappings[substring][0];
                            matchedLength = length;
                            matched = true;
                            break;
                        } else if (substring === 'p') {
                            result += consonant_mappings['b'][1];
                            matchedLength = length;
                            matched = true;
                            break;
                        } else if (consonant_mappings.hasOwnProperty(substring)) {
                            result += consonant_mappings[substring][1];
                            matchedLength = length;
                            matched = true;
                            break;
                        }
                    }
                }
            } else if (vowel_mappings.hasOwnProperty(substring) && !vowel_mappings.hasOwnProperty(input_text[i - length])) {
                if (i > 0 && !consonant_mappings.hasOwnProperty(input_text[i - 1])) {
                    // Add the vowel parts
                    result += vowel_mappings[substring][0] + 'อ' + vowel_mappings[substring][1];

                    // --- Tone handling for vowel-initial syllables ---
                    if ([...substring].some(v => c_tones.includes(v))) {
                        result += '้';
                    } else if ([...substring].some(v => b_tones.includes(v))) {
                        result += '่';
                    }
                    result += vowel_mappings[substring][2];
                }
                matchedLength = length;
                matched = true;
            }

            if (matched) break;
        }

        if (!matched) {
            if ('ou'.includes(char)) {
                if (i > 0 && vowel_mappings.hasOwnProperty(input_text[i - 1])) {
                    result += 'ว';
                } else {
                    result += char;
                }
            } else if ('iy'.includes(char)) {
                if (i > 0 && vowel_mappings.hasOwnProperty(input_text[i - 1])) {
                    result += 'ย';
                } else {
                    result += char;
                }
            }
        }

        i += matchedLength;
    }

    return result.trim();
}
