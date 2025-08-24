const vowel_mappings = {
    'e': ['แ', '', ''],
    'ê': ['เ', '', ''],
    'ơ': ['เ', '', 'อ'],
    'ô': ['โ', '', ''],
    'o': ['', '', 'อ'],
    'a': ['', '', 'า'],
    'ă': ['', '', ''],
    'â': ['เ', 'ี', ''],
    'i': ['', 'ี', ''],
    'ư': ['', 'ื', ''],
    'u': ['', 'ุ', ''],
    
    'ươ': ['เ', 'ื', 'อ'],
    'ưa': ['เ', 'ื', 'อ'],
    'iê': ['เ', 'ี', 'ย'],
    'ia': ['เ', 'ี', 'ย'],
    'uô': ['', '', 'ว'], # ['', 'ั', 'ว'],
    'ua': ['', 'ั', 'ว'],

    'ay': ['', '', 'ย'], # ['', 'ั', 'ย'],
    'au': ['เ', '', 'า'],
    'ây': ['เ', 'ี', 'ย'], # ['', 'ึ', 'ย'],

    'oă': ['', 'ว', ''], # ['', 'วั', ''],
    'oa': ['', 'ว', 'า'],
    'oe': ['แ', 'ว', ''],
    'uâ': ['เ', 'วี', ''], # ['', 'วึ', ''], # 'วิ'
    'uơ': ['เ', 'ว', 'อ'],
    'uê': ['เ', 'ว', ''],
    'uy': ['', 'วี', ''], # 'วิ'
    'ơi': ['เ', '', 'ย'],
    'uyê': ['เ', 'วี', 'ย'],
    'uya': ['เ', 'วี', 'ย'],
    'oay': ['', 'ว', 'ย'], # ['', 'วั', 'ย'],
    'uây': ['เ', 'วี', 'ย'], # ['', 'วึ', 'ย'],
};

const consonant_mappings = {
    'm': ['ม', 'หม'],
    'n': ['น', 'หน'],
    'nh': ['ญ', 'หญ'],
    'ng': ['ง', 'หง'],
    'ngh': ['ง', 'หง'],

    'b': ['พ', 'บ'], # !
    'đ': ['ฑ', 'ฎ'],
    'p': ['ภ', 'ป'], # !
    't': ['ท', 'ด'],
    'th': ['ธ', 'ถ'],
    'tr': ['ฒ', 'ฐ'],
    'ch': ['ช', 'จ'],
    'c': ['ค', 'ก'],
    'k': ['ค', 'ก'],
    'q': ['ค', 'ก'],
    'qu': ['คว', 'กว'],

    'f': ['ฟ', 'ผ'], # !
    'ph': ['ฟ', 'ผ'], # !
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
}

function transcribe() {
    let inputText = document.getElementById("input").value.toLowerCase();
    let outputText = inputText;

    // Get selected slot index (default = 0 if not using radio buttons)
    const slotIndex = 0;

    // Combine all keys with type info
    const allMappings = [];
    for (let key in vowel_mappings) allMappings.push({ key, type: 'vowel' });
    for (let key in consonant_mappings) allMappings.push({ key, type: 'consonant' });

    // Sort by length descending (to prioritize digraphs/trigraphs)
    allMappings.sort((a, b) => b.key.length - a.key.length);

    allMappings.forEach(item => {
        let regex = new RegExp(item.key, 'g');
        let value = (item.type === 'vowel')
            ? vowel_mappings[item.key][slotIndex]
            : consonant_mappings[item.key][slotIndex];
        outputText = outputText.replace(regex, value);
    });

    document.getElementById("output").value = outputText;
}
