<html lang="en">
  <head>
    <title>Vietnamese Thai Transcriber</title>
    <img class="bigimg" src="https://raw.githubusercontent.com/glyphdoggo/thai-for-vietnamese/refs/heads/main/icon.png" height="400">
    <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <link rel="stylesheet" href="style.css"> -->
    <style>
    html, body {
        margin: 0;
        text-align: center;
        background-color: #333;
        color: #edc;
        height: 100%;
        font-size: 18px;
        font-family: sans-serif;
        align-content: center;
    }

    textarea {
        font-family: sans-serif;
        background-color: #edc;
        width: 65%;
        padding: 18px;
    }

    .interface {
        display: flex;
        height: 100%;
        flex-direction: column;
    }

    .two {
        align-content: center;
        flex: 2;
    }

    .one {
        align-content: center;
        flex: 1;
    }

    .bigimg {
        position: absolute;
        left: 1;
        top: 1;
        z-index: -1;
    }
    </style>
    <link rel="icon" href="https://raw.githubusercontent.com/glyphdoggo/thai-for-vietnamese/refs/heads/main/icon.png">
  </head>
  <body>
    <div class="interface">
      <div class="two"></div>
      <div class="two">
        <h3>VIETNAMESE THAI TRANSCRIBER</h3>
        <h4>A Thai Orthography for the Vietnamese Language</h4>
      </div>
      <div class="one"></div>
      <div>
        <p>Type or paste Vietnamese text below:</p>
        <textarea rows="5" id="input" placeholder="Tất cả mọi người sinh ra đều được tự do và bình đẳng về nhân phẩm và quyền lợi..." oninput="transcribe()"></textarea>
      </div>
      <div class="one"></div>
      <div>
        <p>Result:</p>
        <textarea rows="5" id="output"></textarea>
      </div>
      <div class="one"></div>
      <div class="two"></div>
      <script> // src="script.js"
        const vowel_mappings = {
          'a': ['', '', 'า'],
          'ă': ['', '', ''],
          'â': ['เ', 'ี', ''],
          'e': ['แ', '', ''],
          'ê': ['เ', '', ''],
          'i': ['', 'ี', ''],
          'o': ['', '', 'อ'],
          'ô': ['โ', '', ''],
          'ơ': ['เ', '', 'อ'],
          'u': ['', 'ุ', ''],
          'ư': ['', 'ื', ''],
          'y': ['', 'ี', ''],

          'ia': ['เ', 'ี', 'ย'],
          'iê': ['เ', 'ี', 'ย'],
          'ua': ['', 'ั', 'ว'],
          'uô': ['', 'ั', 'ว'],
          'ưa': ['เ', 'ื', 'อ'],
          'ươ': ['เ', 'ื', 'อ'],

          'au': ['เ', '', 'า'],
          'ay': ['', '', 'ย'],
          'ây': ['เ', 'ี', 'ย'],

          'oa': ['', 'ว', 'า'],
          'oă': ['', 'ว', ''],
          'oe': ['แ', 'ว', ''],
          'ơi': ['เ', '', 'ย'],
          'uâ': ['เ', 'วี', ''],
          'ue': ['แ', 'ว', ''],
          'uê': ['เ', 'ว', ''],
          'uơ': ['เ', 'ว', 'อ'],
          'uy': ['', 'วี', ''],

          'oay': ['', 'ว', 'ย'],
          'uây': ['เ', 'วี', 'ย'],
          'uya': ['เ', 'วี', 'ย'],
          'uyê': ['เ', 'วี', 'ย'],
        };

        const consonant_mappings = {
          'b': ['พ', 'บ'],
          'c': ['ค', 'ก'],
          'ch': ['ช', 'จ'],
          'd': ['ย', 'หย'],
          'đ': ['ฑ', 'ฎ'],
          'g': ['ฅ', 'ฃ'],
          'gh': ['ฅ', 'ฃ'],
          'gi': ['ย', 'หย'],
          'h': ['ฮ', 'ห'],
          'k': ['ค', 'ก'],
          'kh': ['ฆ', 'ข'],
          'l': ['ล', 'หล'],
          'm': ['ม', 'หม'],
          'n': ['น', 'หน'],
          'ng': ['ง', 'หง'],
          'ngh': ['ง', 'หง'],
          'nh': ['ญ', 'หญ'],
          'p': ['ภ', 'ป'],
          'ph': ['ฟ', 'ผ'],
          'q': ['ค', 'ก'],
          'r': ['ร', 'หร'],
          's': ['ซ', 'ส'],
          't': ['ท', 'ด'],
          'th': ['ธ', 'ถ'],
          'tr': ['ฒ', 'ฐ'],
          'v': ['ว', 'หว'],
          'x': ['ฌ', 'ฉ'],

          'f': ['ฟ', 'ผ'],
          'j': ['ย', 'หย'],
          'w': ['ว', 'หว'],
          'z': ['ย', 'หย'],

          // 'i': ['ย', 'หย'],
          // 'o': ['ว', 'หว'],
          // 'u': ['ว', 'หว'],
          // 'y': ['ย', 'หย'],
        };

        function transcribe() {
            let inputText = document.getElementById("input").value.toLowerCase().trim();
            let words = inputText.split(/\s+/);  // split by spaces
            let result = [];

            words.forEach(word => {
                let syllable = processSyllable(word);
                result.push(syllable);
            });

            document.getElementById("output").value = result.join(" ");
        }

        function processSyllable(syll) {
            let preV = '', mainC = '', postV1 = '', tone = '', postV2 = '', finalC = '';

            let consonantKeys = Object.keys(consonant_mappings).sort((a,b)=>b.length-a.length);
            let vowelKeys = Object.keys(vowel_mappings).sort((a,b)=>b.length-a.length);

            let initial = '';
            for (let key of consonantKeys) {
                if (syll.startsWith(key)) {
                    initial = key;
                    break;
                }
            }

            let remaining = syll.slice(initial.length);

            // Find vowel cluster
            let vowel = '';
            for (let key of vowelKeys) {
                if (remaining.startsWith(key)) {
                    vowel = key;
                    break;
                }
            }

            if (vowel) {
                preV = vowel_mappings[vowel][0];
                postV1 = vowel_mappings[vowel][1];
                postV2 = vowel_mappings[vowel][2];
                remaining = remaining.slice(vowel.length);
            }

            if (initial) {
                mainC = consonant_mappings[initial][1];
            } else if (vowel) {
                mainC = 'อ';
            } else {
                mainC = ''; // For spaces, punctuation, or unknown characters
            }

            let glide = '';
            if (remaining.length > 0) {
                if (remaining.endsWith('i') || remaining.endsWith('y')) {
                    glide = 'ย';
                } else if (remaining.endsWith('o') || remaining.endsWith('u')) {
                    glide = 'ว';
                }
            }

            // Handle final consonant
            let final = '';
            for (let key of consonantKeys) {
                if (remaining.endsWith(key)) {
                    final = key;
                    break;
                }
            }

            if (final) {
                if (['d','gi','j','l','m','n','ng','nh','r','v','w','z'].includes(final)) {
                    finalC = consonant_mappings[final][0]; // special coda forms (voiced/sonorants)
                } else if (final === 'p') {
                    finalC = consonant_mappings['b'][1]; // p → b in coda
                } else if (consonant_mappings[final]) {
                    finalC = consonant_mappings[final][1]; // default
                }
            }

            return preV + mainC + postV1 + postV2 + glide + finalC;
        }
      </script>
    </div>
  </body>
</html>
